"""
This Python code defines a function called company_name that takes a company name as an argument, queries the 
Clearbit API to find information about the company, and then prints and returns the main website URL of 
the company.
The primary functionality remains the same. It queries the Clearbit API to find information about a 
company based on the provided name. 
If it successfully retrieves data, it extracts the domain, constructs the main website URL, prints it, and 
returns it.
"""

import requests
def company_name(name):##take a name from user
    response = requests.get(
        f'https://autocomplete.clearbit.com/v1/companies/suggest?query={name}')##searching corresponding company name from google using this api
    data = response.json()
    if len(data) > 0:##if successfully found it
        domain = data[0]['domain']##add the main domain name to domain variable
        main_website="https://"+domain##add with https
        print(main_website)##print the whole main website
    else:
        print(f'No domain found for {name}')##print if not found 
    
    return main_website ##return it

