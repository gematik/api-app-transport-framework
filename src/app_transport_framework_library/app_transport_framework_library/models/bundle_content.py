from fhir.resources.R4B.bundle import BundleEntry
from typing import List
from .service_identifier import ServiceIdentifier


class BundleContent:
    def __init__(self, service_identifier: ServiceIdentifier, focus_ressource_id: str, sender: str,  bundle_entries: List[BundleEntry]):
        self.service_identifier = service_identifier
        self.focus_ressource_id = focus_ressource_id
        self.sender = sender
        self.bundle_entries = bundle_entries
