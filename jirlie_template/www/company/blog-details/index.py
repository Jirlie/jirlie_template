import frappe
import requests
from bs4 import BeautifulSoup



def get_context(context):

    context.blg = frappe.form_dict.blg
    r = requests.get(f"https://tazzweed.com/api/method/tazzweed.api.blog_filter?name={context.blg}")
    context.blogger_photo = f"https://tazzweed.com{r.json()['message'][0]['blogger_photo']}"
    context.blog_intro = r.json()['message'][0]['blog_intro']
    context.content = r.json()['message'][0]['content']

    context.title = r.json()['message'][0]['title']
    context.blogger_full_name = r.json()['message'][0]['blogger_full_name']
    context.site_name = r.json()['message'][0]['site_name']
    context.blog_category_name = r.json()['message'][0]['blog_category_name']
    
    print(f"##########{context.blg}##############")

    return context
