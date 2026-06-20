# Notes on Files

- **Memory Limits**: `f.read()` loads the entire file into memory as a giant string. This is fine for small files, but fatal for gigabyte-sized server logs. Iterating via `for line in f:` only loads one line into memory at a time.
- **The `os` module**: Interacting with the file system requires asking the Operating System for help. The `os` module provides these hooks (checking if files exist, listing directories).
- **Graceful Degradation**: `try`/`except` isn't for suppressing bugs; it's for handling predictable failures (like a missing file) and providing the user with a helpful path forward, rather than a scary traceback.
