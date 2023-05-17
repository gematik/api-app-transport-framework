from fhir.resources.bundle import Bundle
from fhir.resources.operationoutcome import OperationOutcomeIssue


class Empfangsbestaetigung:
    def __init__(self, message_id: str, message_received: bool, sender: str, details: OperationOutcomeIssue):
        self.message_id = message_id
        self.message_received = message_received
        self.sender = sender
        self.details = details
