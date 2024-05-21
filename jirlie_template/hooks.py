from . import __version__ as app_version

app_name = "jirlie_template"
app_title = "Jirlie Template"
app_publisher = "Mohammed Nasser"
app_description = "Jirlie Template"
app_email = "nasser@nasserx.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jirlie_template/css/jirlie_template.css"
# app_include_js = "/assets/jirlie_template/js/jirlie_template.js"

# include js, css files in header of web template
# web_include_css = "/assets/jirlie_template/css/jirlie_template.css"
# web_include_js = "/assets/jirlie_template/js/jirlie_template.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jirlie_template/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "subscribe"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "jirlie_template.utils.jinja_methods",
#	"filters": "jirlie_template.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jirlie_template.install.before_install"
# after_install = "jirlie_template.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jirlie_template.uninstall.before_uninstall"
# after_uninstall = "jirlie_template.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jirlie_template.utils.before_app_install"
# after_app_install = "jirlie_template.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jirlie_template.utils.before_app_uninstall"
# after_app_uninstall = "jirlie_template.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jirlie_template.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

website_route_rules = [
    {'from_route': '/news/news-details/<name2>', 'to_route': 'news/news-details'},
    {'from_route': '/news/<blog_category2>', 'to_route': 'news'},
    {"from_route": "/learn/learn-details/<docname>", "to_route": "learn/learn-details"},
    {"from_route": "/company/profile/<com>", "to_route": "company/profile"},
    {"from_route": "/company/product-details/<itm>", "to_route": "company/product-details"},
    {"from_route": "/company/blog-details/<blg>", "to_route": "company/blog-details"}
    
]

website_redirects = [
	{"source": r"/me(.*)", "target": r"/dashboard\1"},
]


doc_events = {
    "Blog Category": {
        "validate": "jirlie_template.events.blog_category.validate"
    },
    "Blog Post": {
        "validate": "jirlie_template.events.blog_post.validate"
    }
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"jirlie_template.tasks.all"
#	],
#	"daily": [
#		"jirlie_template.tasks.daily"
#	],
#	"hourly": [
#		"jirlie_template.tasks.hourly"
#	],
#	"weekly": [
#		"jirlie_template.tasks.weekly"
#	],
#	"monthly": [
#		"jirlie_template.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "jirlie_template.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "jirlie_template.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "jirlie_template.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jirlie_template.utils.before_request"]
# after_request = ["jirlie_template.utils.after_request"]

# Job Events
# ----------
# before_job = ["jirlie_template.utils.before_job"]
# after_job = ["jirlie_template.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"jirlie_template.auth.validate"
# ]
