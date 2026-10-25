"""
Lab 1.2 — Tool 1: File I/O
===========================

Implement two functions: read_file and write_file.

Both functions must:
  - Match the parameter names in schemas.py EXACTLY. The LLM sends those
    exact names; a mismatch causes a silent failure that is hard to debug.
  - NEVER raise an unhandled exception. Always return a string —
    either a success message or a descriptive error message.
  - Be usable as pure Python functions with no LLM dependency.

Run the tests to verify your implementation before moving to agent.py:
  pytest tests/test_file_io.py -v

Success criterion (from the lab spec):
  The agent writes a Python file, executes it, reads the output, and
  reports the result — all in one agentic loop.
"""

import os


def read_file(path: str) -> str:
    """
    Read the contents of a file at the given path.

    Parameters
    ----------
    path : str
        Relative or absolute path to the file.

    Returns
    -------
    str
        File contents on success.
        A descriptive error string on failure — do NOT raise.

    Hints
    -----
    - Use os.path.abspath(path) to resolve relative paths before opening.
    - Handle at minimum: FileNotFoundError, PermissionError, and a
      generic Exception fallback.
    - Always include the path in the error message so the agent can
      diagnose what went wrong and try an alternative.

    Example return values
    ---------------------
    Success : "def word_count(text):\n    ..."
    Failure : "Error reading file '/src/utils.py': No such file or directory."
    """
    try:
        with open(os.path.abspath(path), encoding="utf-8") as handle:
            return handle.read()
    except Exception as exc:
        return f"Error reading file {path!r}: {exc}"


def write_file(path: str, content: str) -> str:
    """
    Write content to a file at the given path.

    Creates the file (and any missing parent directories) if needed.
    Overwrites any existing file at that path.

    Parameters
    ----------
    path : str
        Relative or absolute path to the target file.
    content : str
        Full text content to write.

    Returns
    -------
    str
        A confirmation message that includes the number of lines written.
        A descriptive error string on failure — do NOT raise.

    Hints
    -----
    - Before opening the file, create parent directories with:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
      The `if parent` guard is needed because os.path.dirname returns ''
      for bare filenames like "script.py".
    - Open in write mode ("w") with encoding="utf-8".
    - Count lines AFTER writing: len(content.splitlines()).

    Example return values
    ---------------------
    Success : "File written successfully. 12 lines."
    Failure : "Error writing file '/read-only/file.py': Permission denied."
    """
    try:
        target = os.path.abspath(path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(content)
        return f"File written successfully. {len(content.splitlines())} lines."
    except Exception as exc:
        return f"Error writing file {path!r}: {exc}"
