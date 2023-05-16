from fhir.resources.meta import Meta
from fhir.resources.bundle import Bundle, BundleEntry
from fhir.resources.messageheader import MessageHeader
from fhir.resources.fhirtypes import IdentifierType
from uuid import uuid4


class MessageBundleCreator:
    @staticmethod
    def create_message_bundle(message_header: MessageHeader, resources: list[BundleEntry]) -> Bundle:
        bundle_id = str(uuid4())

        entries = [
            BundleEntry(
                fullUrl=f"urn:uuid:{message_header.id}", resource=message_header)
        ]

        entries.extend(resources)

        message_bundle = Bundle(
            id=bundle_id,
            meta=Meta.construct(profile=[
                "https://gematik.de/fhir/atf/StructureDefinition/bundle-app-transport-framework"
            ]),
            type="message",
            identifier=IdentifierType(
                system="urn:ietf:rfc:3986", value=f"urn:uuid:{bundle_id}"),
            entry=entries
        )

        return message_bundle
