from fhir.resources.bundle import Bundle


class MessageToSend:
    def __init__(self, operation_outcome_bundle: Bundle, receiver: str, message_type: str):
        self.operation_outcome_bundle = operation_outcome_bundle
        self.receiver = receiver
        self.message_type = message_type
