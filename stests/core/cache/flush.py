import typing

from stests.core.cache.utils import flushcache
from stests.core.domain import RunContext



@flushcache
def flush_run(ctx: RunContext) -> typing.Generator:
    """Flushes previous run information.

    :param ctx: Generator run contextual information.

    :returns: A generator of keypaths to be flushed.
    
    """
    yield ["run-account"] + ctx.keypath
    yield ["run-context"] + ctx.keypath
    yield ["run-deploy"] + ctx.keypath
    yield ["run-event"] + ctx.keypath
    yield ["run-transfer"] + ctx.keypath
