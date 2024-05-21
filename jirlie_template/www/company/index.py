import frappe

def get_context(context):
#     context.companies = frappe.db.sql("""select * from `tabDirectory`;""", as_dict=True)
#     context.industry = frappe.db.sql("""select name from `tabIndustry Type`;""", as_dict=True)
#     context.country = frappe.db.sql("""select name from `tabCountry`;""", as_dict=True)
    context.all_industry = frappe.get_all("Industry Type", pluck="name")
    return context



