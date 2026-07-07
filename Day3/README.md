Project Overview
My project upgrades the system with real file storage, so data now survives between runs.

What's New in this
- every Add, Update, and Delete operation immediately calls `save_students()`, which writes the full in-memory list to `students.json` using `json.dump()`.
- `load_students()` runs at the very beginning of `main()` and reads `students.json` with `json.load()`, so previously
  saved records appear automatically — no manual "load" step needed.
- file operations and user input are wrapped in `try/except` blocks instead of relying only on manual string checks, so the program never crashes on bad input or file problems.

What I Learned Today
- How to make a program's data persistent by writing it to disk instead of only keeping it in a Python variable that disappears when the script ends.
- The difference between the `json` module's two key functions: json.dump() and json.load()
- How to structure a program so that every state-changing action immediately syncs to disk, instead of only saving once when the program exits even if the program crashes or is closed unexpectedly, no changes are lost.
- How to use try/except to handle multiple realistic failure points: a missing file (`FileNotFoundError`), a corrupted/empty file (`json.JSONDecodeError`), a bad numeric input (`ValueError`), and general I/O problems (`IOError`/`OSError`).
- Why it's good practice to check `os.path.exists()` before attempting to open a file for reading, to give a clean first-run experience.

How File Handling and JSON Work Together
A Python list of dictionaries lives only in memory — it's fast to work with, but temporary. JSON is a lightweight, human-readable text format that maps almost directly onto Python's own
data structures: a JSON array looks and behaves like a Python `list`, and a JSON object looks and behaves like a Python `dict`.

Because `save_students()` is called after every add/update/delete, the JSON file on disk is always an permanent snapshot of the current data

Challenges Faced & Solutions Implemented
First run of the program has no `students.json` yet, and trying to open a non-existent file crashes with `FileNotFoundError`. added an `os.path.exists()` check plus a `try/except FileNotFoundError` fallback in `load_students()` so the program simply starts with an empty list on first run. 
A manually edited or corrupted JSON file could crash `json.load()`. wrapped the load logic in `try/except json.JSONDecodeError` so the program warns the user and safely falls back to an empty list instead of crashing.
Saving after every single operation felt repetitive. wrote one reusable `save_students()` function and called it at the end of `add_student()`, `update_student()`, and `delete_student()` 
Needed to handle bad input without the old `isdigit()`-only approach feeling fragile. switched to `try/except ValueError` around `int()` conversions, which is the standard way to validate numeric input and catches negative/zero values too. 
Wanted to make sure an unexpected error inside any menu option wouldn't crash the whole program and lose unsaved progress. wrapped the main menu dispatch in `main()` with a broad `try/except Exception`, so the program reports the error and safely returns to the menu instead of terminating.

