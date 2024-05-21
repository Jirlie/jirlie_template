import frappe

def validate(doc, method):
    doc.route = f"news/{doc.name}"