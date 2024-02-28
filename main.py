from bs4 import BeautifulSoup
import requests

# URL of the webpage containing the XML data
url_seimo_kadencijos = "https://apps.lrs.lt/sip/p2b.ad_seimo_kadencijos"
url_seimo_posedziai = "https://apps.lrs.lt/sip/p2b.ad_seimo_posedziai?sesijos_id=127"
url_seimo_posedzio_eiga = "https://apps.lrs.lt/sip/p2b.ad_sp_eiga?posedzio_id=-501747"
url_balsavimo_rezultatai = (
    "https://apps.lrs.lt/sip/p2b.ad_sp_balsavimo_rezultatai?balsavimo_id=-43782"
)

# All URLs together
urls = [
    url_seimo_kadencijos,
    url_seimo_posedziai,
    url_seimo_posedzio_eiga,
    url_balsavimo_rezultatai,
]


def get_data(request):
    # List of scraped data
    scraped_data = []

    # Scraping...
    for url in urls:

        # Send a GET request to fetch the webpage content
        response = requests.get(url)

        # Parse the XML data using BeautifulSoup
        soup = BeautifulSoup(response.content, "xml")

        # Find all nodes and subnodes
        all_nodes = soup.find_all(recursive=True)

        # Read names and attributes of all nodes, put into dictionaries
        for node in all_nodes:
            d = {**{"tag": node.name}, **(node.attrs)}
            scraped_data += [d]
    return scraped_data
