from typing import Callable,    TypeAlias

Vendor:TypeAlias =str

def dummy_loader(path: str, **kwargs):
    return path

Loader = Callable[[str], "AClass"]

_REGISTRY: dict[str, Loader] = {
    "dummy": dummy_loader,
}


def _normalize_vendor(vendor: Vendor) -> str:
    # Accept Enum, str, etc.
    if hasattr(vendor, "name"):  # Enum-like
        return vendor.name.lower()
    return str(vendor).lower()


def load(
    path: str, *, vendor: Vendor, **kwargs
):
    """
    Load a thing for a vendor
    """
    key = _normalize_vendor(vendor)
    try:
        fn = _REGISTRY[key]
    except KeyError as e:
        raise ValueError(
            f"Unknown vendor '{vendor}'. Known: {sorted(_REGISTRY)}"
        ) from e

    call_kwargs = dict(kwargs)

    return fn(path=path, **call_kwargs)


__all__ = ["load"]
