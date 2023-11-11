from contextvars import ContextVar


flags: ContextVar[list[bool]] = ContextVar('flags', default=None)
