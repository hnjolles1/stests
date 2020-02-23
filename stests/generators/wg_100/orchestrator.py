import dramatiq

from stests.core import cache
from stests.core.domain import AccountType
from stests.core.domain import RunContext

from stests.core.actors.account import do_create_account
from stests.core.actors.account import do_fund_account
from stests.core.actors.misc import do_reset_cache
from stests.generators.wg_100 import constants
from stests.generators.wg_100.phase_1 import do_start_auction
from stests.generators.wg_100.phase_1 import do_deploy_contract
from stests.generators.wg_100.phase_1 import do_fund_faucet


# Queue to which message will be dispatched.
_QUEUE = f"generators.{constants.TYPE.lower()}"

# Account index: faucet.
ACC_INDEX_FAUCET = 1

# Account index: contract.
ACC_INDEX_CONTRACT = 2

# Account index: users.
ACC_INDEX_USERS = 3



def execute(ctx: RunContext):
    """Orchestrates execution of WG-100 workflow.

    :param ctx: Generator run contextual information.

    """ 
    ctx.run_step == "reset_cache"
    cache.set_run_context(ctx)

    do_reset_cache.send_with_options(
        args=(ctx, ),
        on_success=on_cache_reset
        )


@dramatiq.actor(queue_name=_QUEUE, actor_name="on_wg100_deploy_finalized")
def on_deploy_finalized(deploy_hash):
    """Callback: on_start_auction.
    
    :param ctx: Generator run contextual information.

    """    
    print(f"TIME TO GO HOME :: {deploy_hash}")


@dramatiq.actor(queue_name=_QUEUE)
def on_cache_reset(_, ctx: RunContext):
    """Callback: on_cache_reset.
    
    :param ctx: Generator run contextual information.

    """
    ctx.run_step == "create_accounts"
    cache.set_run_context(ctx)

    def get_messages():
        yield do_create_account.message(ctx, ACC_INDEX_FAUCET, AccountType.FAUCET)
        yield do_create_account.message(ctx, ACC_INDEX_CONTRACT, AccountType.CONTRACT)
        for index in range(ACC_INDEX_USERS, ctx.args.user_accounts + ACC_INDEX_USERS):
            yield do_create_account.message(ctx, index, AccountType.USER)

    g = dramatiq.group(get_messages())
    g.add_completion_callback(on_create_accounts.message(ctx))
    g.run()


@dramatiq.actor(queue_name=_QUEUE)
def on_create_accounts(ctx: RunContext):
    """Callback: on_create_accounts.
    
    :param ctx: Generator run contextual information.

    """
    ctx.run_step == "fund_faucet"
    cache.set_run_context(ctx)

    do_fund_faucet.send(ctx, ACC_INDEX_FAUCET, ctx.args.faucet_initial_clx_balance)


@dramatiq.actor(queue_name=_QUEUE)
def on_fund_faucet(_, ctx: RunContext):
    """Callback: on_fund_faucet.
    
    :param ctx: Generator run contextual information.

    """
    ctx.run_step == "fund_contract"
    cache.set_run_context(ctx)

    print(777)
    # do_fund_account.send_with_options(
    #     args=(ctx, ACC_INDEX_FAUCET, ACC_INDEX_CONTRACT, ctx.args.contract_initial_clx_balance),
    #     on_success=on_fund_contract
    # )


@dramatiq.actor(queue_name=_QUEUE)
def on_fund_contract(_, ctx: RunContext):
    """Callback: on_fund_contract.
    
    :param ctx: Generator run contextual information.

    """
    def get_messages():
        for index in range(ACC_INDEX_USERS, ctx.args.user_accounts + ACC_INDEX_USERS):
            yield do_fund_account.message(
                ctx, ACC_INDEX_FAUCET, index, ctx.args.user_initial_clx_balance
            )

    g = dramatiq.group(get_messages())
    g.add_completion_callback(on_fund_users.message(ctx))
    g.run()


@dramatiq.actor(queue_name=_QUEUE)
def on_fund_users(ctx: RunContext):
    """Callback: on_fund_users.
    
    :param ctx: Generator run contextual information.

    """
    do_deploy_contract.send_with_options(
        args=(ctx, ),
        on_success=on_deploy_contract
        )


@dramatiq.actor(queue_name=_QUEUE)
def on_deploy_contract(_, ctx: RunContext):
    """Callback: on_deploy_contract.
    
    :param ctx: Generator run contextual information.

    """
    do_start_auction.send_with_options(
        args=(ctx, ),
        on_success=on_start_auction
        )


@dramatiq.actor(queue_name=_QUEUE)
def on_start_auction(_, ctx: RunContext):
    """Callback: on_start_auction.
    
    :param ctx: Generator run contextual information.

    """
    print("TIME TO GO HOME")

