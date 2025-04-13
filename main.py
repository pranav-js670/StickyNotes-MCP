from mcp.server.fastmcp import FastMCP
import os

# create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.
    Args:
        message (str): The message to add to the sticky note file.
    Returns:
        str: Confirmation message indicating that the note was added.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note added!"


@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.
    Returns:
        str: A string containing all notes from the sticky note file, separated by newlines.
        If no notes are found, returns "No notes found."
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes or "No notes yet"


@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Retrieve the latest note from the sticky note file.
    Returns:
        str: The latest note from the sticky note file, or "No notes yet" if no notes are found.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet"


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarizing the current notes.
    Returns:
        str: A string containing the prompt asking the AI to summarize the current notes.
        If no notes are found, returns "No notes yet."
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet"
    return f"Summarize the current notes: {content}"
