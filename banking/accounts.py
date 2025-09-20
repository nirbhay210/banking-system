from dataclasses import dataclass

@dataclass
class Account:
    id: int
    owner: str
    balance: float = 0.0