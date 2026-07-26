"""Output formatting for different display formats."""

import csv
import io
import json
from typing import List, Optional, cast

from tabulate import tabulate  # type: ignore[import-untyped]


class OutputFormatter:
    """Handles formatting output in table, JSON, CSV, or tree formats."""

    @staticmethod
    def table(headers: List[str], rows: List[List[str]]) -> str:
        """Format as ASCII table."""
        if not rows:
            return "(no data)"
        return str(tabulate(rows, headers=headers, tablefmt="grid"))

    @staticmethod
    def json_format(data: object) -> str:
        """Format as JSON."""
        return json.dumps(data, indent=2, default=str)

    @staticmethod
    def csv_format(headers: List[str], rows: List[List[str]]) -> str:
        """Format as CSV."""
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(headers)
        writer.writerows(rows)
        return output.getvalue()

    @staticmethod
    def format(data: object, format_type: str, headers: Optional[List[str]] = None) -> str:
        """Route data to appropriate formatter."""
        if format_type == "json":
            return OutputFormatter.json_format(data)
        elif format_type == "csv":
            headers = headers or []
            rows = data if isinstance(data, list) else [[data]]
            return OutputFormatter.csv_format(headers, cast(List[List[str]], rows))
        else:  # table (default)
            headers = headers or []
            rows = data if isinstance(data, list) else [[data]]
            return OutputFormatter.table(headers, cast(List[List[str]], rows))
