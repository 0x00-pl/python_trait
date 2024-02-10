import typing

trait_impl_pool = {}

T = typing.TypeVar('T')


class Trait(typing.Generic[T]):
    def trait_for(self, obj) -> T:
        return self.cls_trait_for(obj)

    @classmethod
    def cls_trait_for(cls, obj) -> T:
        impl = cls.get_impl(obj)
        return impl(obj)

    def __call__(self, obj) -> T:
        return self.trait_for(obj)

    @classmethod
    def get_impl(cls, obj):
        if cls not in trait_impl_pool:
            return None
        impl_pool = trait_impl_pool[cls]
        for ty, impl in reversed(impl_pool.items()):
            if isinstance(obj, ty):
                return impl
        return None


    @classmethod
    def has_trait(cls, obj) -> bool:
        return cls.get_impl(obj) is not None


def register_trait(origin_cls, trait_cls):
    def impl(trait_impl):
        impl_pool = trait_impl_pool.get(trait_cls, {})
        impl_pool[origin_cls] = trait_impl
        return trait_impl

    return impl


def trait_to(origin_cls):
    def impl(trait_impl):
        trait_cls = [t for t in trait_impl.__bases__ if issubclass(t, Trait)][0]
        impl_pool = trait_impl_pool.get(trait_cls, {})
        impl_pool[origin_cls] = trait_impl
        trait_impl_pool[trait_cls] = impl_pool
        return trait_impl

    return impl
