import frappe
import requests



def get_context(context):

    context.itm = frappe.form_dict.itm
    r = requests.get(f"https://tazzweed.com/api/method/tazzweed.api.product_filter?name={context.itm}")
    context.item_name = r.json()['message'][0]['item_name']
    context.description = r.json()['message'][0]['description']
    context.website_image = r.json()['message'][0]['website_image']
    context.brand = r.json()['message'][0]['brand']
    context.item_group = r.json()['message'][0]['item_group']
    context.item_code = r.json()['message'][0]['item_code']
    context.site_name = r.json()['message'][0]['site_name']
    
    print(f"##########{context.itm}##############")

    return context
