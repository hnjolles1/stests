from dataclasses import dataclass
from enum import Flag

from dataclasses_json import dataclass_json

from stests.core.types.utils import get_enum_field



# Enum: Set of node states.
NodeStatus = Flag("NodeStatus", [
    "NULL",
    "GENESIS",
    "INITIALIZING",
    "HEALTHY",
    "DISTRESSED",
    "DOWN",
    "DEINITIALIZING"    
    ])


@dataclass_json
@dataclass
class Node():
    """Represents a node within a target network.
    
    """
    host: str
    port: int
    status: NodeStatus = \
        get_enum_field(NodeStatus, NodeStatus.NULL)


# Set: supported domain types.
TYPESET = {
    Node,
}