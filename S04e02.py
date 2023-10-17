import requests
from bs4 import BeautifulSoup

URL = "https://divar.ir/s/tehran?q=%D8%AA%D9%88%D8%A7%D9%81%D9%82%DB%8C"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="post-list-container-id")

res_elements = results.find_all("div", class_="post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46")

for res_element in res_elements:
    # -- snip --
    links = res_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"{link_url}\n")
      