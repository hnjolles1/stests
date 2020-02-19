import dramatiq
from stests.core.actors.misc import on_run_event
from stests.core.domain import NetworkIdentifier
from stests.core.domain import RunContext



class GeneratorEventMiddleware(dramatiq.Middleware):
    """Middleware to automatically persist generator events.
    
    """
    def before_process_message(self, broker, message):
        """Called before a message is processed.

        :param broker: Message broker to which message was dispatched.
        :param message: A message being processed.

        """
        actor_name = str(message).split('(')[0]
        if isinstance(message.args, tuple) and len(message.args) > 0 and \
           actor_name.startswith("on_") and \
           actor_name != "on_run_event":
            args = message.args if isinstance(message.args[0], (RunContext, NetworkIdentifier)) else message.args[0]['args']
            if isinstance(args[0], RunContext):
                on_run_event.send_with_options(
                    args=(args[0], actor_name)
                    )        

