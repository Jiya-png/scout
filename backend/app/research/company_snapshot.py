from dataclasses import dataclass, field


@dataclass
class CompanySnapshot:
    website: str

    title: str | None = None
    description: str | None = None

    h1: str | None = None
    h2: list[str] = field(default_factory=list)
    h3: list[str] = field(default_factory=list)

    paragraphs: list[str] = field(default_factory=list)

    links: list[str] = field(default_factory=list)

    social_links: list[str] = field(default_factory=list)

    emails: list[str] = field(default_factory=list)

    phone_numbers: list[str] = field(default_factory=list)
    
    pages: dict = field(default_factory=dict)