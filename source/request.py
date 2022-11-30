from os import environ
from dotenv import load_dotenv
from requests import request


load_dotenv()
url = environ.get("URL_API")


def mega_data():
    nodes = []
    nodes_connections = []
    limit_page = False
    skip = 0

    while limit_page == False:
        params = dict(limit=100, skip=skip)
        response = request(method="GET", url=url, params=params)

        if response.status_code != 200:
            limit_page = True
        else:
            data = response.json()

            for item in data:
                nodes.append(item.get("id_link"))
                nodes.append(item.get("id_href"))
                nodes_connections.append((item.get("id_link"), item.get("id_href")))

            skip += 100

    nodes = set(nodes)

    return list(nodes), nodes_connections


def mini_data():
    nodes = []
    nodes_connections = []
    params = dict(limit=25, skip=0)
    response = request(method="GET", url=url, params=params)
    data = response.json()

    for item in data:
        nodes.append(item.get("id_link"))
        nodes.append(item.get("id_href"))
        nodes_connections.append((item.get("id_link"), item.get("id_href")))
