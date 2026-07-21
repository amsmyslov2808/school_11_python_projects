from dataclasses import dataclass


@dataclass(slots=True)
class Post:
    posting_datetime: str
    media_url: str
    description: str
    id: int | None = None
