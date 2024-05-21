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

def get_context(context):
    context.get_blogger = frappe.db.sql("""select * from `tabBlog Post` where `blogger`= '{{frappe.form_dict.blogger}}'; """, as_dict=True)
    return context
   