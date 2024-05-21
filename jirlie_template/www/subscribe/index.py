import frappe

def get_context(context):
    testi = frappe.db.sql("""select `head_content`, `content`, `person`, `blogger_photo_link`, `blogger_bio` from `tabTestimonies` where `disabled`=0;""", as_dict=True)
    context.testi = testi
    return context
