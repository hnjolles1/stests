import typing

from stests.core.clx.utils import get_client
from stests.core.domain import Account
from stests.core.domain import Block
from stests.core.domain import BlockStatus
from stests.core.domain import NetworkIdentifier
from stests.core.domain import RunContext
from stests.core.utils import factory



def get_balance(ctx: RunContext, account: Account) -> int:
    """Returns a chain account balance.

    :param ctx: Generator run contextual information.
    :param account: Account whose balance will be queried.

    :returns: Account balance.

    """
    client = get_client(ctx)
    try:
        balance = client.balance(
            address=account.public_key,
            block_hash=_get_last_block_hash(client)
            )
    except Exception as err:
        if "Failed to find base key at path" in err.details:
            return 0
        raise err
    else:
        return balance


def get_block(network_id: NetworkIdentifier, block_hash: str) -> Block:
    """Queries network for information pertaining to a specific block.

    :param network_id: A network identifier.
    :param block_hash: Hash of a block.

    :returns: Block information.

    """
    client = get_client(network_id)
    info = client.showBlock(block_hash_base16=block_hash, full_view=False)

    return factory.create_block(
        network_id=network_id,
        block_hash=block_hash,
        deploy_cost_total=info.status.stats.deploy_cost_total,
        deploy_count=info.summary.header.deploy_count, 
        deploy_gas_price_avg=info.status.stats.deploy_gas_price_avg,
        rank=info.summary.header.rank,
        size_bytes=info.status.stats.block_size_bytes,
        timestamp=info.summary.header.timestamp,
        validator_id=info.summary.header.validator_public_key.hex()
        )


def get_block_deploys(network_id: NetworkIdentifier, block_hash: str) -> typing.List[str]:
    """Queries network for set of deploys associated with a specific block.

    :param network_id: A network identifier.
    :param block_hash: Hash of a block.

    :returns: Block information.

    """
    client = get_client(network_id)

    return (i.deploy.deploy_hash.hex() for i in client.showDeploys(block_hash_base16=block_hash, full_view=False))


def _get_last_block_hash(client) -> str:
    """Returns a chain's last block hash.
    
    """
    last_block_info = next(client.showBlocks(1))

    return last_block_info.summary.block_hash.hex()
