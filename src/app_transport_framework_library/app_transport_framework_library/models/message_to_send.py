from fhir.resources.bundle import Bundle


class MessageToSend:
    def __init__(self, atf_bundle: Bundle, receiver: str, message_type: str):
        self.atf_bundle = atf_bundle
        self.receiver = receiver
        self.message_type = message_type
