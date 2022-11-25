from flask_login import UserMixin
from dataclasses import dataclass

@dataclass
class comments:
    idc: int
    date: str
    contents :str
    reaction: str