import requests
from bs4 import BeautifulSoup
TRENDING_PAGE = "https://github.com/trending"


def get_trending_repos():
    repos = []
    resp = requests.get(TRENDING_PAGE)
    data = resp.text
    if resp.status_code != 200:
        return None
    bs = BeautifulSoup(data, "html.parser")
    data_repos = bs.select("h3 > a")
    for repo in data_repos:
        print(repo.get('href')[1:])
    # print(bs.select("h3 > a").get('href'))


if __name__ == '__main__':
    get_trending_repos()
