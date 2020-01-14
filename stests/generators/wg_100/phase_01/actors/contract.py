import dramatiq

from stests.core.cache import accessor as cache
from stests.core.types.factory import create_contract_account
from stests.generators.wg_100 import metadata
from stests.core.types.account import AccountType
from stests.core.types.account import AccountType


# Queue to which message will be dispatched.
_QUEUE = f"{metadata.ID}.phase_01.contract"


@dramatiq.actor(queue_name=_QUEUE, actor_name="deploy_contract")
def deploy(ctx, account):
    """Deploys smart contract to target network.
    
    """
    print(222, account)
    print(cache.retrieve_account(ctx, AccountType.CONTRACT, account.index))
