import typing

from stests.core.cache.utils import encache
from stests.core.domain import Block
from stests.core.domain import Deploy
from stests.core.domain import Network
from stests.core.domain import NetworkIdentifier
from stests.core.domain import Node



@encache
def set_network(network: Network) -> typing.Tuple[typing.List[str], Network]:
    """Encaches domain object: Network.

    :param network: Network domain object instance to be cached.
    
    :returns: Keypath + domain object instance.

    """
    return [
        "network",
        network.name,
    ], network


@encache
def set_network_block(network_id: NetworkIdentifier, block: Block) -> typing.Tuple[typing.List[str], Block]:
    """Encaches domain object: Block.
    
    :param network_id: A network identifier.
    :param block: Block domain object instance to be cached.

    :returns: Keypath + domain object instance.

    """
    return [
        "network-block",
        network_id.name,
        f"{str(block.rank).zfill(7)}.{block.block_hash}"
    ], block
    

@encache
def set_network_node(node: Node) -> typing.Tuple[typing.List[str], Node]:
    """Encaches domain object: Node.
    
    :param node: Node domain object instance to be cached.

    :returns: Keypath + domain object instance.

    """
    return [
        "network-node",
        node.network,
        f"N-{str(node.index).zfill(4)}"
    ], node


@encache
def set_network_deploy(network_id: NetworkIdentifier, deploy: Deploy) -> typing.Tuple[typing.List[str], Deploy]:
    """Encaches domain object: Deploy.
    
    :param network_id: A network identifier.
    :param block: Deploy domain object instance to be cached.

    :returns: Keypath + domain object instance.

    """
    return [
        "network-deploy",
        network_id.name,
        f"{deploy.block_hash}.{deploy.deploy_hash}"
    ], deploy
