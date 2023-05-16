from fhir.resources.bundle import BundleEntry


class BundleFocusContent:
    def __init__(self, system: str, code: str, bundle_entries: list[BundleEntry]):
        self.system = system
        self.code = code
        self.bundle_entries = bundle_entries
