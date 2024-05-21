# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

from six.moves.urllib.parse import quote, urljoin

import frappe
from frappe import _
from frappe.utils import (
	cint,
	get_fullname,
	global_date_format,
	markdown,
	sanitize_html,
	strip_html_tags,
	today,
)
from frappe.website.utils import find_first_image, get_comment_list, get_html_content_based_on_type
from frappe.utils import cstr, escape_html, get_request_site_address, now

no_cache = 1
base_template_path = "templates/www/rss.xml"


def get_blog_list(
        doctype, txt=None, filters=None, limit_start=0, limit_page_length=20, order_by=None
):
    conditions = []
    category = filters.get("blog_category") or frappe.utils.escape_html(
        frappe.local.form_dict.blog_category2 or frappe.local.form_dict.category2
    )
    blogger = filters.get("blogger") or frappe.utils.escape_html(
        frappe.local.form_dict.blogger2 or frappe.local.form_dict.blogger2
    )
    if filters:
        if filters.blogger:
            conditions.append("t1.blogger=%s" %
                              frappe.db.escape(filters.blogger))
    if category:
        conditions.append("t1.blog_category=%s" % frappe.db.escape(category))

    if txt:
        conditions.append(
            '(t1.content like {0} or t1.title like {0}")'.format(
                frappe.db.escape("%" + txt + "%"))
        )

    if conditions:
        frappe.local.no_cache = 1

    query = """\
		select
			t1.title, t1.name, t1.blog_category, t1.route, t1.published_on, t1.read_time,
				t1.published_on as creation,
				t1.read_time as read_time,
				t1.featured as featured,
				t1.meta_image as cover_image,
				t1.content as content,
				t1.content_type as content_type,
				t1.content_html as content_html,
				t1.content_md as content_md,
				ifnull(t1.blog_intro, t1.content) as intro,
				t2.full_name, t2.avatar, t1.blogger,
				(select count(name) from `tabComment`
					where
						comment_type='Comment'
						and reference_doctype='Blog Post'
						and reference_name=t1.name) as comments
		from `tabBlog Post` t1, `tabBlogger` t2
		where ifnull(t1.published,0)=1
		and t1.blogger = t2.name
		%(condition)s
		order by featured desc, published_on desc, name asc
		limit %(page_len)s OFFSET %(start)s""" % {
            "start": limit_start,
            "page_len": limit_page_length,
            "condition": (" and " + " and ".join(conditions)) if conditions else "",
    }

    posts = frappe.db.sql(query, as_dict=1)

    for post in posts:
        post.content = get_html_content_based_on_type(
            post, "content", post.content_type)
        if not post.cover_image:
            post.cover_image = find_first_image(post.content)
        post.published = global_date_format(post.creation)
        post.content = strip_html_tags(post.content)

        if not post.comments:
            post.comment_text = _("No comments yet")
        elif post.comments == 1:
            post.comment_text = _("1 comment")
        else:
            post.comment_text = _("{0} comments").format(str(post.comments))

        post.avatar = post.avatar or ""
        post.category = frappe.db.get_value(
            "Blog Category", post.blog_category, ["name", "route", "title"], as_dict=True
        )

        if (
                post.avatar
                and (not "http:" in post.avatar and not "https:" in post.avatar)
                and not post.avatar.startswith("/")
        ):
            post.avatar = "/" + post.avatar

    return posts


def get_context(context):
    """generate rss feed"""
    host = get_request_site_address(True)
    print(frappe.request.path)
    blog_list = get_blog_list("Blog Post", filters={})

    for blog in blog_list:
        blog_page = cstr(quote(blog.name.encode("utf-8")))
        blog.link = urljoin(host, blog_page)
        blog.content = escape_html(blog.content or "")

    blog_settings = frappe.get_doc("Blog Settings", "Blog Settings")

    context = {
        "blog_title": blog_settings.blog_title or "Blog",
        "blog_introduction": blog_settings.blog_introduction or "",
        "blogs": blog_list,
        "link": host + "/news",
    }

    # print context
    return context
    