from fhir.resources.bundle import BundleEntry
from typing import List

class BundleFocusContent:
    def __init__(self, system: str, code: str, bundle_entries: List[BundleEntry]):
        self.system = system
        self.code = code
        self.bundle_entries = bundle_entries
