from contextvars import ContextVar
from typing import List


flags: ContextVar[List[bool]] = ContextVar('flags', default=None)
