from dataclasses import dataclass
from dataclasses_json import dataclass_json

from stests.core.domain.enums import AccountType
from stests.core.domain.enums import NetworkType
from stests.core.utils.domain import get_enum_field




@dataclass_json
@dataclass
class NetworkIdentifier:
    """Information required to disambiguate between networks.
    
    """ 
    # Internal name of network, e.g. LRT-01
    name: str   

    @property
    def index(self) -> int:
        return int(self.name.split("-")[1])

    @property
    def type(self) -> NetworkType:
        return NetworkType[self.name.split("-")[0]]

    @property
    def key(self) -> str:
        return f"global.network:{self.name}"


@dataclass_json
@dataclass
class NodeIdentifier:
    """Information required to disambiguate between nodes.
    
    """ 
    # Associated network identifer.
    network: NetworkIdentifier

    # Node index.
    index: int
 

@dataclass_json
@dataclass
class RunIdentifier:
    """Information required to disambiguate between generator runs.
    
    """
    # Associated network identifer.
    network: NetworkIdentifier
    
    # Numerical index to distinguish between multiple runs of the same generator.
    index: int

    # Type of generator, e.g. WG-100 ...etc.
    type: str


@dataclass_json
@dataclass
class AccountIdentifier:
    """Information required to disambiguate between accounts.
    
    """ 
    # Numerical index to distinguish between accounts within same context.
    index: int

    # Associated run identifier.
    run: RunIdentifier

    @property
    def network_id(self) -> NetworkIdentifier:
        return this.run.network
