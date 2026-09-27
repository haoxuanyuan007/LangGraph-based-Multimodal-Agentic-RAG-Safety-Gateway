# Data boundary

Git stores only manifests, license records, deterministic generators, and small safe fixtures. Raw documents, page images, indexes, model caches, vulnerability snapshots, and sensitive runtime material must remain in ignored local storage or configured external storage.

Runtime storage must keep these logical collections separate:

- `source_registry`
- `knowledge_corpus`
- `case_memory`
- `vulnerability_intel`
- `evaluation_set`

The evaluation set must be physically or access-control isolated from ingestion jobs. Index writes must also reject records with `split=eval`.
