from .http_client import HttpClient
from .parser import HtmlParser
from .extractor import ContentExtractor
from .link_discovery import LinkDiscovery


class WebsiteCrawler:

    def __init__(self):

        self.client = HttpClient()

        self.parser = HtmlParser()

        self.extractor = ContentExtractor()

        self.discovery = LinkDiscovery()

    def crawl(self, website):

        homepage = self.client.download(website)

        soup = self.parser.parse(homepage)

        snapshot = self.extractor.extract(soup)

        snapshot.website = website

        snapshot.pages["homepage"] = {
            "title": snapshot.title,
            "description": snapshot.description,
            "h1": snapshot.h1,
            "h2": snapshot.h2,
            "h3": snapshot.h3,
            "paragraphs": snapshot.paragraphs,
        }

        important_links = self.discovery.discover(
            soup,
            website
        )

        for link in important_links:

            try:

                html = self.client.download(link)

                page = self.extractor.extract(
                    self.parser.parse(html)
                )

                page.website = link

                snapshot.pages[link] = {
                    "title": page.title,
                    "description": page.description,
                    "h1": page.h1,
                    "h2": page.h2,
                    "h3": page.h3,
                    "paragraphs": page.paragraphs,
                }

            except Exception:
                continue

        return snapshot