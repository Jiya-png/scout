import requests


class HttpClient:
    def download(self, url: str) -> str:
        response = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/137.0.0.0 Safari/537.36"
                )
            },
            timeout=15,
        )

        response.raise_for_status()
        return response.text