import typing

from stests.core.cache.utils import flushcache
from stests.core.domain import RunContext



@flushcache
def flush_run(ctx: RunContext) -> typing.Generator:
    """Flushes previous run information.

    :param ctx: Generator run contextual information.

    :returns: A generator of keypaths to be flushed.
    
    """
    for collection in [
        "account",
        "context",
        "deploy",
        "event",
        "step",
        "transfer",
    ]:
        yield [
            f"run-{collection}",
            ctx.network,
            ctx.run_type,
            f"R-{str(ctx.run).zfill(3)}"            
        ]
