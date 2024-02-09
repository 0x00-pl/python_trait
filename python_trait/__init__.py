import typing

trait_impl_pool = {}

T = typing.TypeVar('T')


class Trait(typing.Generic[T]):
    def trait_for(self, obj) -> T:
        impl = trait_impl_pool[type(obj), type(self)]
        return impl(obj)

    @classmethod
    def cls_trait_for(cls, obj) -> T:
        impl = trait_impl_pool[type(obj), cls]
        return impl(obj)

    def __call__(self, obj) -> T:
        return self.trait_for(obj)

    @classmethod
    def has_trait(cls, obj) -> bool:
        return (type(obj), cls) in trait_impl_pool


def register_trait(origin_cls, trait_cls):
    def impl(trait_impl):
        trait_impl_pool[origin_cls, trait_cls] = trait_impl
        return trait_impl

    return impl


def trait_to(origin_cls):
    def impl(trait_impl):
        trait_cls = [t for t in trait_impl.__bases__ if issubclass(t, Trait)][0]
        trait_impl_pool[origin_cls, trait_cls] = trait_impl
        return trait_impl

    return impl
