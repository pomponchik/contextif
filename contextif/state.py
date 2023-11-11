from contextvars import ContextVar
from typing import Callable, Any

from contextif.variable import flag


class ContextState:
    def __init__(self, variable: ContextVar[bool] = flag) -> None:
        self.flag = variable

    def __call__(self, some_callable: Callable[[...], Any], args: Any, kwargs: Any) -> Any:
        if self.flag.get()
            return some_callable(*args, **kwargs)

    def set(self) -> None:
        self.flag.set(True)


state = ContextState()
