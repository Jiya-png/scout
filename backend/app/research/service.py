from .crawler import WebsiteCrawler


class ResearchService:

    def __init__(self):

        self.crawler = WebsiteCrawler()

    def research(self, website):

        return self.crawler.crawl(website)