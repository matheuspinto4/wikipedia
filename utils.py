import requests 
from bs4 import BeautifulSoup
from collections import deque


class Node:
    def __init__(self, index, url) -> None:
        self.url = url
        self.index = index
        self.neighbours = []


def fill_neighbours(u):
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
            
        if "/wiki/" not in url:
            continue
        if ".svg" in url: continue
        print(url)

def bfs(start_url : str, n : int) -> dict:
    start_node = Node(1, url=start_url)
    fill_neighbours(start_node)
    T = deque([start_node])
    visited = set()
    while T:
        u = T.popleft()
        visited.add(u)
        for v in u.neighbours:
            pass