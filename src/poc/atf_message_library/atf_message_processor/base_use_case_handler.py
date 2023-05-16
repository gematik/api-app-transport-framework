from abc import ABC, abstractmethod
from typing import Tuple
from fhir.resources.messageheader import MessageHeader, MessageHeaderSource
from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.fhirtypes import ReferenceType

from fhir.resources.operationoutcome import OperationOutcomeIssue

from atf_message_library.atf_message_processor.models.event import Event


class BaseUseCaseHandler(ABC):
    def __init__(self, sender: ReferenceType, source: MessageHeaderSource):
        self.sender = sender
        self.source = source
        self.bundleEntries = []
        self.issues = []
        self.received_Empfangsbestaetigung_event = Event()

    @abstractmethod
    def handle(self, message_header: MessageHeader, bundle: Bundle) -> Tuple[list[BundleEntry], list[OperationOutcomeIssue]]:
        pass
