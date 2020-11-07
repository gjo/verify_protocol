from typing import EXCLUDED_ATTRIBUTES, get_type_hints


class Invalid(Exception):
    pass


class BrokenImplementation(Invalid):
    pass


class MultipleInvalid(Invalid):
    pass


def _get_specs(cls):
    specs = get_type_hints(cls)
    for base in cls.__mro__[:-1]:  # without `object`
        if base.__name__ in ("Protocol", "Generic"):
            continue
        for k, v in base.__dict__.items():
            if k.startswith("_abc_") or k in EXCLUDED_ATTRIBUTES:
                continue
            if k not in specs and hasattr(v, "__annotations__"):
                specs[k] = v.__annotations__
    return specs


def _verify_element(proto, name, spec, candidate):
    try:
        attr = getattr(candidate, name)
    except AttributeError:
        raise BrokenImplementation(proto, name, candidate)

    if callable(attr):
        if hasattr(attr, "__annotations__") and attr.__annotations__ != spec:
            raise BrokenImplementation(proto, name, candidate)
    else:
        # FIXME: generics support
        if not isinstance(attr, spec):
            raise BrokenImplementation(proto, name, candidate)


def verify_object(proto, candidate):
    excs = []

    for name, spec in _get_specs(proto).items():
        try:
            _verify_element(proto, name, spec, candidate)
        except Invalid as e:
            excs.append(e)

    if excs:
        if len(excs) == 1:
            raise excs[0]
        raise MultipleInvalid(proto, candidate, excs)
    return True
