import datetime
import random
import typing
from datetime import datetime as dt

from stests.core.domain import *
from stests.core.utils import crypto
from stests.core.utils import factory



def create_account(typeof: AccountType=None) -> Account:
    return factory.create_account(
        status=random.choice(list(AccountStatus)),
        typeof=typeof or random.choice(list(AccountType))
    )


def create_block() -> Block:
    return Block(
        block_hash="9dbc064574aafcba8cadbd20aa6ef5b396e64ba970d829c188734ac09ae34f64",
        deploy_cost_total=int(1e7),
        deploy_count=1,
        deploy_gas_price_avg=1,
        network="lrt1",
        rank=1,
        size_bytes=int(1e8),
        timestamp=dt.now().timestamp(),
        validator_id="dca0025bfb03f7be74c47371ca74883b47587f3630becb0e7b46b7c9ae6e8500",
        status=random.choice(list(BlockStatus))
    )


def create_deploy() -> Deploy:
    return Deploy(
        block_hash="9dbc064574aafcba8cadbd20aa6ef5b396e64ba970d829c188734ac09ae34f64",
        deploy_hash="02c74421666866809a2343f95229af960077a9bfed56b31bc9f231d108958eeb",
        network="lrt1",
        node=1,
        run=1,
        run_type="WG-XXX",
        status=random.choice(list(DeployStatus)),
        ts_dispatched=None,
        ts_finalized=None    
    )


def create_network() -> Network:
    index=1
    typeof=NetworkType.LOC

    return Network(
        faucet=create_account(AccountType.FAUCET),
        index=index,
        name=f"{typeof.name}-{str(index).zfill(2)}",
        name_raw=f"{typeof.name.lower()}{index}",
        status=random.choice(list(NetworkStatus)),
        typeof=random.choice(list(NetworkType)),
    )


def create_network_id() -> NetworkIdentifier:
    return factory.create_network_id("lrt1")


def create_node() -> Node:
    return Node(
        account=create_account(AccountType.BOND),
        host="localhost",
        index=1,
        network="LOC-01",
        port=40400,
        status=random.choice(list(NodeStatus)),
        typeof=random.choice(list(NodeType)),
    )


def create_run_context() -> RunContext:
    return RunContext(
        args=None,
        network="LOC-01",
        node=1,
        run=1,
        run_type="WG-XXX"
        )


def create_run_event() -> RunEvent:
    return RunEvent(
        event="on_wg_event",
        network="LOC-01",
        run=1,
        run_type="WG-XXX",
        timestamp=dt.now().timestamp()
        )


def create_transfer() -> Transfer:
    return Transfer(
        amount=int(1e7),
        asset="CLX",
        cp1_index=1,
        cp2_index=2,
        deploy_hash="02c74421666866809a2343f95229af960077a9bfed56b31bc9f231d108958eeb",
        deploy_hash_refund=None,
        is_refundable=False,
        network="lrt1",
        node=1,
        run=1,
        run_type="WG-XXX",
        status=TransferStatus.PENDING
        )


# Map: domain type to factory function.
FACTORIES: typing.Dict[typing.Type, typing.Callable] = {
    Account: create_account,
    Block: create_block,
    Deploy: create_deploy,
    Network: create_network,
    Node: create_node,
    RunContext: create_run_context,
    RunEvent: create_run_event,
    Transfer: create_transfer
}


def get_instance(dcls: typing.Type) -> typing.Any:
    try:
        factory = FACTORIES[dcls]
    except KeyError:
        raise ValueError("Unsupported domain type: {}".format(dcls))
    else:
        return factory()
