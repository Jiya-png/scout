from urllib.parse import urljoin, urlparse

IMPORTANT_KEYWORDS = {
    "about",
    "company",
    "careers",
    "jobs",
    "pricing",
    "products",
    "solutions",
    "platform",
    "customers",
    "blog",
    "contact",
    "security",
    "research",
    "team",
}


class LinkDiscovery:

    def discover(self, soup, base_url):

        links = []

        for a in soup.find_all("a", href=True):

            href = a["href"]

            absolute = urljoin(base_url, href)

            parsed = urlparse(absolute)

            if parsed.netloc != urlparse(base_url).netloc:
                continue

            score = 0

            for keyword in IMPORTANT_KEYWORDS:
                if keyword in absolute.lower():
                    score += 10

            if score > 0:
                links.append((score, absolute))

        links = sorted(
            list(set(links)),
            reverse=True
        )

        return [url for _, url in links[:10]]