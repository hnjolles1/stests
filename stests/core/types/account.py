import random
import typing
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from enum import Enum
from enum import Flag

from stests.core.types.crypto import KeyPair
from stests.core.types.utils import get_enum_field
from stests.core.utils import defaults



# Flag: Set of account states.
AccountStatus = Flag("AccountStatus", [
    "NEW",
    "FUNDING",
    "FUNDED",
    "ACTIVE"
    ])


# Enum: Set of account types.
AccountType = Enum("AccountType", [
    "CONTRACT",
    "FAUCET",
    "USER",
    "VALIDATOR"
    ])


@dataclass_json
@dataclass
class Account:
    """An account that maps to an address upon target chain.
    
    """
    index: int
    key_pair: KeyPair
    network_id: str = defaults.NETWORK_ID
    status: AccountStatus = get_enum_field(AccountStatus, AccountStatus.NEW)
    typeof: AccountType = get_enum_field(AccountType)


    @property
    def short_type(self) -> str:
        """Returns short type name.
        
        """
        return str(self.typeof).split('.')[-1]


    @staticmethod
    def create(typeof=None):
        """Factory: returns an instance for testing purposes.
        
        """
        return Account(
            index=0,
            key_pair=KeyPair.create(),
            typeof=typeof or random.choice(list(AccountType))
            )
