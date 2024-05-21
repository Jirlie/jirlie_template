import frappe

def get_context(context):
    context.page = frappe.get_doc("Web Page", frappe.form_dict.page)
    return context