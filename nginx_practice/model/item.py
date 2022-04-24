from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    description: str | None = None
    tax: float | None = None
    tags: list = field(default_factory=list)
