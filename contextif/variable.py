from contextvars import ContextVar


flags: ContextVar[list] = ContextVar('flags', default=None)
