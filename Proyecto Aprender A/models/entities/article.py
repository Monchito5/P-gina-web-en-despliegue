from flask_login import UserMixin
from dataclasses import dataclass

@dataclass
class article:
    ida: int
    id: int
    idc: int
    title : str
    content: str
    views: str
    pdate: str
    learningchannel: str