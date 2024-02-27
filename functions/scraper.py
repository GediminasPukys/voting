# import functions_framework
import xml.etree.ElementTree as ET
import requests

# url='https://apps.lrs.lt/sip/p2b.ad_seimo_kadencijos'
url = "http://apps.lrs.lt/sip/p2b.ad_seimo_kadencijos"
proxies = {
    "http": "84.15.154.202:80",
}  # change proxy to None if working from local


# @functions_framework.http
def get_kadencijos_xml():
    response = requests.get(url=url, proxies=proxies)
    return response.text


# kadencijos_xml_response = get_kadencijos_xml()

# # Parse the XML string
# root = ET.fromstring(kadencijos_xml_response)

# # Create an empty list to store the parsed data
# parsed_data = []

# # Iterate over the child elements of the root element
# for child in root:
#     # Create a dictionary to store the attributes of each child element
#     child_data = {}
#     child_data['kadencijos_id'] = child.attrib.get('kadencijos_id')
#     child_data['pavadinimas'] = child.attrib.get('pavadinimas')
#     child_data['data_nuo'] = child.attrib.get('data_nuo')
#     child_data['data_iki'] = child.attrib.get('data_iki')
#     # Append the dictionary to the parsed data list
#     parsed_data.append(child_data)

# # Print the parsed data list
# print(parsed_data)
# parsed_data[0]['kadencijos_id']

# [
#     {"kadencija":,
# 'sesija':,
# 'komitetas':,
# 'posedis':,
# 'balsavimas':[{'sirinskiene':'uz'},{'gabrielius':'registravosi'},{}]
# }
#
# ]
# kadencijos <-> sesijos <->
