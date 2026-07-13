from bs4 import BeautifulSoup


class HtmlParser:
    def parse(self, html: str):
        return BeautifulSoup(html, "html.parser")