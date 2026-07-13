from .company_snapshot import CompanySnapshot

class ContentExtractor:

    def extract(self, soup):

        title = soup.title.string.strip() if soup.title else None

        description = None

        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            description = meta.get("content")

        h1 = soup.find("h1")
        h1 = h1.get_text(strip=True) if h1 else None

        h2 = [
        tag.get_text(strip=True)
        for tag in soup.find_all("h2")
        ]

        h3 = [
        tag.get_text(strip=True)
        for tag in soup.find_all("h3")
        ]

        paragraphs = [
        p.get_text(strip=True)
        for p in soup.find_all("p")
        ]   

        paragraphs = paragraphs[:10]

        snapshot = CompanySnapshot(
        website="",
        title=title,
        description=description,
        h1=h1,
        h2=h2,
        h3=h3,
        paragraphs=paragraphs
        )

        return snapshot