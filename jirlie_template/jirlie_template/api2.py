import frappe
from frappe import _
from frappe.model.document import Document


@frappe.whitelist(allow_guest=True)
def directory(company_name, company_logo, company_description, ignore_permissions=True):
    doc = frappe.new_doc("Directory")
    doc.company_name = company_name
    doc.company_logo = company_logo
    doc.company_description = company_description
    frappe.session.user = 'Administrator'
    doc.insert()
    doc.save()
    return doc

@frappe.whitelist(allow_guest=True)
def get():
    doc = frappe.get_all("Directory")
    return doc