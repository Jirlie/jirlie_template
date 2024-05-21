import frappe

def validate(doc, method):
    doc.route = f"news/news-details/{doc.name}"