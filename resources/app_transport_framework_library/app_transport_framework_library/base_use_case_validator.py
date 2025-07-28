from abc import ABC, abstractmethod
from typing import List, Tuple
from fhir.resources.R4B.messageheader import MessageHeader, MessageHeaderSource
from fhir.resources.R4B.bundle import Bundle, BundleEntry
from fhir.resources.R4B.fhirtypes import ReferenceType
from fhir.resources.R4B.operationoutcome import OperationOutcomeIssue
from app_transport_framework_library.models.event import Event

class BaseUseCaseValidator(ABC):
    def __init__(self, sender: ReferenceType, source: MessageHeaderSource):
        self.sender = sender
        self.source = source
        self.bundleEntries = []
        self.issues = []
        self.received_Empfangsbestaetigung_event = Event()

    @abstractmethod
    def handle(self, message_header: MessageHeader, bundle: Bundle) -> Tuple[List[BundleEntry], List[OperationOutcomeIssue]]:
        pass
