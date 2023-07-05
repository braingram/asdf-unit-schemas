import importlib.resources
from pathlib import Path

from asdf_standard import DirectoryResourceMapping

import asdf_unit_schemas


def get_resource_mappings():
    resources_root = importlib.resources.files(asdf_unit_schemas) / "resources"
    if not resources_root.is_dir():
        # In an editable install, the resources directory will exist off the
        # repository root:
        resources_root = Path(__file__).parent.parent.parent / "resources"
        if not resources_root.is_dir():
            raise RuntimeError("Missing resources directory")

    return [
        DirectoryResourceMapping(
            resources_root / "stsci.edu" / "schemas", "http://stsci.edu/schemas/asdf/unit/", recursive=True
        ),
        DirectoryResourceMapping(
            resources_root / "asdf-format.org" / "manifests", "asdf://asdf-format.org/unit/manifests/"
        ),
    ]
