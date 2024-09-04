import frappe

def get_context(context):
    context.issue_type2 = frappe.db.sql("""select name from `tabIssue Type`;""", as_dict=True)
    return context