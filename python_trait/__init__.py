import typing

T = typing.TypeVar('T')


class Trait(typing.Generic[T]):
    def get_trait(self, obj) -> T:
        impl = trait_impl_pool[type(obj), type(self)]
        return impl(obj)

    def __call__(self, obj) -> T:
        return self.get_trait(obj)


trait_impl_pool = {}


def register_trait(origin_cls, trait_cls):
    def impl(trait_impl):
        trait_impl_pool[origin_cls, trait_cls] = trait_impl
        return trait_impl

    return impl
