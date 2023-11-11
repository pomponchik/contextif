from contextvars import ContextVar


flag: ContextVar[bool] = ContextVar('flag', default=False)
