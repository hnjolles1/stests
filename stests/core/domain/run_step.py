from dataclasses import dataclass

from stests.core.domain.enums import RunStepStatus
from stests.core.utils.domain import *



@dataclass
class RunStep(Entity):
    """Step information associated with a generator run.
    
    """
    # Step name.
    step: str

    # Step parameter.
    step_param: str

    # Associated network.
    network: str

    # Numerical index to distinguish between multiple runs of the same generator.
    run: int

    # Type of generator, e.g. WG-100 ...etc.
    run_type: str

    # Current status.
    status: RunStepStatus = get_enum_field(RunStepStatus)

    # Moment in time when step occurred.
    timestamp: int

    # Moment in time when step completed.
    timestamp_end: int

    # Type key of associated object used in serialisation scenarios.
    _type_key: str = None

    # Timestamp: create.
    _ts_created: datetime = get_isodatetime_field(True)

    # Timestamp: update.
    _ts_updated: datetime = get_isodatetime_field(True)

    # Universally unique identifier.
    _uid: str = get_uuid_field(True) 

    @property
    def name(self):
        return self.step

    @property
    def phase(self):
        return self.step.split(".")[0]

    @property
    def action(self):
        return self.step.split(".")[-1]
