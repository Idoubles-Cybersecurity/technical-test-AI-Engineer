from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class TTPEntry:
    id: str
    text: str


def builtin_ttps() -> Dict[str, TTPEntry]:
    return {
        "T1566": TTPEntry(
            id="T1566",
            text=("Adversaries send deceptive messages (often via email) to trick users "
                  "into revealing information or executing malicious content. May include "
                  "spearphishing attachments, links, or service messages to gain initial access.")
        ),
        "T1134": TTPEntry(
            id="T1134",
            text=("Adversaries manipulate access tokens to operate under another user’s context. "
                  "Techniques include creating, stealing, or impersonating tokens to escalate "
                  "privileges or bypass access controls on Windows and other platforms.")
        ),
    }
