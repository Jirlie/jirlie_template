import frappe

@frappe.whitelist(allow_guest=True)
def testi():
    testi = frappe.db.sql("""select * from `tabTestimonies` where `disabled`=0""", as_dict=True)
    return testi

@frappe.whitelist(allow_guest=True)
def blog():
    blog = frappe.db.sql("""select * from `tabBlog Post` where `published`=1""", as_dict=True)
    site_name = frappe.local.site
    
    # Append site_name to the products dictionary
    for blogs in blog:
        blogs['site_name'] = f"https://{site_name}"

    if not blog:
        return "No blogs in Framework, Just Ask to add some blogs.", {"alert": "if you see this response you successfully connected to api"}

    return blog


@frappe.whitelist(allow_guest=True)
def directory():
    directory = frappe.db.sql("""select * from `tabDirectory`""", as_dict=True)
    site_name = frappe.local.site
    
    # Append site_name to the products dictionary
    for dir in directory:
        dir['site_name'] = f"https://{site_name}"

    return directory

# @frappe.whitelist(allow_guest=True)
# def products():
#     products = frappe.db.sql("""select * from `tabWebsite Item` where `published`=1""", as_dict=True)
#     return {"site_name": frappe.local.site}, products

@frappe.whitelist(allow_guest=True)
def products():
    products = frappe.db.sql("""select * from `tabWebsite Item` where `published`=1 and `variant_of` is NULL""", as_dict=True)
    site_name = frappe.local.site
    
    # Append site_name to the products dictionary
    for product in products:
        product['site_name'] = f"https://{site_name}"

    return products


# @frappe.whitelist(allow_guest=True)
# def productsfilter(*args):
#     productsfilter = frappe.db.sql("""select * from `tabWebsite Item` where `published`=1 and %s""", args, as_dict=True)
#     return productsfilter


# @frappe.whitelist(allow_guest=True)
# def productsfilter(column_name, value):
#     # Ensure that the column name is safe to prevent SQL injection

#     # Build the SQL query with proper placeholders
#     sql_query = f"""select * from `tabWebsite Item` where `published`=1 and `{column_name}` = %s"""
    
#     # Execute the query with the provided value
#     productsfilter = frappe.db.sql(sql_query, (value,), as_dict=True)
    
#     return productsfilter

@frappe.whitelist(allow_guest=True)
def productsfilter(column_name, value, column_name2=None, value2=None):
    # Ensure that the column name is safe to prevent SQL injection

    # Build the SQL query with proper placeholders
    sql_query = f"""select * from `tabWebsite Item` where `published`=1 and `{column_name}` = %s"""

    # Check if an additional condition is provided
    if column_name2 and value2:
        sql_query += f" and {column_name2} = %s"
        productsfilter = frappe.db.sql(sql_query, (value, value2), as_dict=True)
    # Execute the query with the provided value
    else:
        productsfilter = frappe.db.sql(sql_query, (value,), as_dict=True)
    
    
    return productsfilter



@frappe.whitelist(allow_guest=True)
def all_industry():
    all_industry = frappe.get_all("Industry Type", pluck="name")
    return all_industry

@frappe.whitelist(allow_guest=True)
def industry():
    filters = frappe.form_dict
    if "cmd" in filters:
        filters.pop("cmd")
    # Make sure you properly sanitize user inputs to prevent SQL injection
    # Construct the SQL query with placeholders for filter values
    sql_query = """
        SELECT * FROM `tabDirectory`
        WHERE `docstatus` = 0
    """
    
    # Create a list to store the values for the placeholders
    values = []
    
    # Iterate over the filters and add them to the query and values list
    for key, value in filters.items():
        values_list = [val.strip() for val in value.split(",")]
        if values_list:
            sql_query += f" AND ({' OR '.join([f'`{key}` = %s' for _ in values_list])})"
            values.extend(values_list)
    
    # Execute the SQL query with placeholders
    productsfilter = frappe.db.sql(sql_query, values, as_dict=True)
    site_name = frappe.local.site
    
    # Append site_name to the products dictionary
    for dir in productsfilter:
        dir['site_name'] = f"https://{site_name}"
    
    # Debugging: print the filter values
    for key, value in filters.items():
        print(f"{key}: {value}")

    message_data = {
        "data": productsfilter,
        "filters": filters
    }

    # Create a separate message dictionary for the filters
    filters_message = {
        
    }

    return message_data

@frappe.whitelist(allow_guest=True)
def pricing(currency):
    price = frappe.get_all("Currency Exchange", filters={"from_currency":"GBP", "to_currency": currency},fields= {"exchange_rate"})
    return price
    
  