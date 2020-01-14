from stests.core.mq.brokers import BrokerType
from stests.core.mq.brokers import rabbitmq
from stests.core.mq.brokers import redis
from stests.core.mq.brokers import stub
from stests.core.mq.middleware import get_middleware
from stests.core.utils.execution import ExecutionContext



# Map: Broker type -> factory.
FACTORIES = {
    BrokerType.RABBIT: rabbitmq,
    BrokerType.REDIS: redis,
    BrokerType.STUB: stub
}


def get_broker(ctx: ExecutionContext, broker_type: BrokerType = BrokerType.RABBIT):
    """Returns an MQ broker instance for integration with dramatiq framework.

    :param ctx: Contextual information passed along the flow of execution.
    :param broker_type: Type of broker to be instantiated.

    """
    # Set factory.
    try:
        factory = FACTORIES[broker_type]
    except KeyError:
        raise NotImplementedError(f"{broker_type} MQ broker is unsupported")

    # Set broker.
    broker = factory.get_broker(ctx)

    # Set middleware.
    for mware in get_middleware():
        broker.add_middleware(mware)

    return broker