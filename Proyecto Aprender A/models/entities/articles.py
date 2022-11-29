from flask_login import UserMixin
from dataclasses import dataclass

@dataclass
class articles:
    ida: int
    id: int
    idc: int
    title : str
    content: str
    pdate: str
    learningchannel: str