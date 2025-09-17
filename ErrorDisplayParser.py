from __future__ import annotations

import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import List

from Lib import resolve_path


@dataclass(frozen=True)
class ErrorDisplayEntry:
    mapping_order: int
    message: str
    regex: str
    is_default: bool


class ErrorDisplayParser:
    def get_error_display_messages(self) -> List[ErrorDisplayEntry]:
        """
        Parse ErrorDisplayMessages XML into a list of ErrorDisplayEntry.
        xml_source can be:
          - a file path (str or Path) to the XML file
          - a string containing XML content
          - bytes containing XML content
        """
        current_dir = resolve_path()
        xml_source = os.path.join(current_dir, "ErrorDisplayMessages.xml")
        root = None
        p = Path(xml_source)
        if p.exists():
            root = ET.parse(p).getroot()
        else:
            root = ET.fromstring(str(xml_source))

        entries: List[ErrorDisplayEntry] = []
        for node in root.findall("./ErrorMessage"):
            order_raw = node.get("mappingOrder", "0")
            try:
                mapping_order = int(order_raw)
            except ValueError:
                mapping_order = 0

            message = (node.findtext("ErrorDisplayMessage") or "").strip()
            regex = (node.findtext("ErrorDisplayRegexPattern") or "").strip()
            is_default_raw = (node.findtext("IsDefault") or "0").strip()

            # Accept common truthy values
            is_default = is_default_raw in {"1", "true", "True", "YES", "yes"}

            entries.append(
                ErrorDisplayEntry(
                    mapping_order=mapping_order,
                    message=message,
                    regex=regex,
                    is_default=is_default,
                )
            )

        # Sort by mapping_order while preserving document order for ties (stable sort)
        entries.sort(key=lambda e: e.mapping_order)
        return entries
