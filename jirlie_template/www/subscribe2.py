import frappe

def get_context(context):    
    context.basic = frappe.get_doc("Subscription Plan", "Basic")
    context.basic_perks = frappe.db.sql("""select title from `tabSubscription Plan Perks` where parent="Basic";""", as_dict=True)
    context.premium = frappe.get_doc("Subscription Plan", "Premium")
    context.premium_perks = frappe.db.sql("""select title from `tabSubscription Plan Perks` where parent="Premium";""", as_dict=True)
    context.advanced = frappe.get_doc("Subscription Plan", "Advanced")
    context.advanced_perks = frappe.db.sql("""select title from `tabSubscription Plan Perks` where parent="Advanced";""", as_dict=True)
    return context