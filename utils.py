import requests 
from bs4 import BeautifulSoup
from collections import deque


class Node:
    def __init__(self, index, url) -> None:
        self.url = url
        self.index = index
        self.neighbours = []
        self.num_neighbours = 0


def valid_url(url: str):
    if "/wiki/" not in url: return False
    if url.count('/') != 2: return False
    if ".svg" in url: return False
    if ".png" in url: return False
    if '/wiki/Category:' in url: return False
    if "/wiki/ISBN_(identifier)" == url: return False
    if "/wiki/Doi_(identifier)" == url: return False
    if ':' in url: return False

    return True


def fill_neighbours(u: Node, num_max = 6) ->None:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
    "referer": "https://en.wikipedia.org/",
    "Accept-Language": "en-US,en;q=0.5",
    }

    page = requests.get(u.url, headers=headers)
    soup = BeautifulSoup(page.text, "lxml")
    links = soup.find('div', class_="mw-content-ltr mw-parser-output")
    
    for l in links.find_all('a'):
        url = str(l.get("href"))

        #   Tratando os dados:     
        if not valid_url(url): continue 

        u.neighbours.append(f"https://en.wikipedia.org{url}")
        u.num_neighbours += 1
        if u.num_neighbours >= num_max: break 


def bfs(start_url : str, n : int) -> dict:
    start_node = Node(1, url=start_url)
    T = deque([start_node])
    visited = set()
    while T:
        u = T.popleft()
        fill_neighbours(u)
        visited.add(u.url)
        print(f"{u.url} {u.index}:")
        for url in u.neighbours:
            if url in visited: continue
            T.append(Node(index=u.index + 1, url=url))
            print(f"    {url}")