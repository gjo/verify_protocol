from typing import Optional, Protocol

class FooProto(Protocol):
    foo: str

class BarProto(Protocol):
    def bar(self) -> str:
        ...

class BazProto(Protocol):
    baz_: Optional[int]

    def baz(self) -> Optional[str]:
        ...

class Foo:
    def __init__(self, foo: str) -> None:
        self.foo = foo

class Bar:
    def bar(self) -> str:
        return "bar"

class Baz:
    def __init__(self, baz: Optional[int]) -> None:
        self.baz_ = baz

    def baz(self) -> Optional[str]:
        return None if self.baz is None else str(self.baz)

# mypyでこれ書いておけばいいのでは。。。
foo: FooProto = Foo("foo")
bar: BarProto = Bar()
baz: BazProto = Baz(None)


