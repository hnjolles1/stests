from stests.core.cache.stores import get_store
from stests.core.cache.utils import flush_namespace
from stests.core.utils import encoder


def _do_flush(instance):
    """Sink function to flush instances of domain types.
    
    """
    if type(instance) not in encoder.TYPESET:
        raise TypeError("Instance to be cached is not encodeable.")

    with get_store() as store:
        flush_namespace(store, instance.cache_key)


# Flush run information.
flush_run = _do_flush