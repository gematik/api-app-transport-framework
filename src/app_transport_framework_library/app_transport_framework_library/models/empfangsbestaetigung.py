from fhir.resources.R4B.bundle import Bundle
from fhir.resources.R4B.operationoutcome import OperationOutcomeIssue


class Empfangsbestaetigung:
    def __init__(self, message_id: str, message_received: bool, sender: str, receiver: str, details: OperationOutcomeIssue):
        self.message_id = message_id
        self.message_received = message_received
        self.receiver = receiver
        self.sender = sender
        self.details = details
