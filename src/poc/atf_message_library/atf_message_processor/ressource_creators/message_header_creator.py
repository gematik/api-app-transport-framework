from fhir.resources.meta import Meta
from fhir.resources.messageheader import MessageHeader, MessageHeaderDestination, MessageHeaderSource
from fhir.resources.fhirtypes import ReferenceType
from fhir.resources.coding import Coding
from typing import List


class MessageHeaderCreator:
    @staticmethod
    def create_message_header(
        id: str,
        message_sender: ReferenceType,
        source: MessageHeaderSource,
        destinations: List[MessageHeaderDestination],
        code_system: str,
        use_case: str,
        use_case_display: str,
        focus_reference: str,
    ) -> MessageHeader:
        message_header = MessageHeader(
            id=id,
            meta=Meta.construct(profile=[
                "https://gematik.de/fhir/atf/StructureDefinition/message-header-app-transport"
            ]),
            eventCoding=Coding(
                system=code_system,
                code=use_case,
                display=use_case_display
            ),
            source=source,
            destination=destinations,
            sender=message_sender,
            focus=[ReferenceType(reference=f"urn:uuid:{focus_reference}")]
        )
        return message_header
