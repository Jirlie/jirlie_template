import frappe

def get_context(context):
        
    docname = frappe.form_dict.docname
    if docname == None:
        docname = "getting-started"
    context.learn = frappe.get_doc("Help Article", docname)
    context.learn2_cat = frappe.db.sql(""" select * from `tabHelp Article` order by `custom_order` ASC """, as_dict=True)
    return context