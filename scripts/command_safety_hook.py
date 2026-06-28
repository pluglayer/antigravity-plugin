#!/usr/bin/env python3
"""Optional Antigravity hook that asks before broad cleanup commands."""

from __future__ import annotations

import json
import re
import sys


def main() -> int:
    payload = json.load(sys.stdin)
    command = str(payload.get("toolCall", {}).get("args", {}).get("CommandLine", ""))
    broad_cleanup = (
        r"\bdocker\s+system\s+prune\b",
        r"\bdocker\s+(image|container|volume)\s+prune\b",
        r"\brm\s+-rf\s+(~|/|\$HOME)\b",
    )
    if any(re.search(pattern, command) for pattern in broad_cleanup):
        result = {
            "decision": "force_ask",
            "reason": (
                "This command can remove resources outside PlugLayer's task-owned "
                "artifacts. Confirm the exact cleanup scope first."
            ),
        }
    else:
        result = {
            "decision": "ask",
            "reason": "Review the proposed command before execution.",
        }
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
