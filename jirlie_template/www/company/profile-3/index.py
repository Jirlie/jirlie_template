import frappe

def get_context(context):
    docname = frappe.form_dict.com
    print(docname)
    context.companies2 = frappe.get_doc("Directory", docname)
    simq = context.companies2.domain
    context.sim = frappe.db.sql("""SELECT * from `tabDirectory` WHERE `domain`= %s """, simq, as_dict=True)
    return context