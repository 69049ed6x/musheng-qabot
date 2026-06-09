from __future__ import annotations

import json

from .config import PROJECT_ROOT, SOURCE_DIR
from .documents import load_source_chunks


def main() -> None:
    chunks = load_source_chunks(SOURCE_DIR)
    payload = {
        "version": 1,
        "chunks": [
            {
                "id": index,
                "source": chunk.source,
                "title": chunk.title,
                "content": chunk.content,
                "kind": chunk.kind,
            }
            for index, chunk in enumerate(chunks, start=1)
        ],
    }
    target = PROJECT_ROOT / "static" / "kb.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(chunks)} chunks to {target}")


if __name__ == "__main__":
    main()
