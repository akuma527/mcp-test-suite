# mcp_server.py
from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP(name="HouseBuilderMCP")

# ---- TOOLS ---- #

@mcp.tool
def paint_wall(color: str, surface: str) -> str:
    """Paints a wall with the specified color and surface."""
    return f"Painted {surface} with {color} paint."

@mcp.tool
def cut_wood(length: int, width: int) -> str:
    """Cuts wood to the specified length and width."""
    return f"Cut wood to {length}x{width} units."

@mcp.tool
def lay_bricks(area: float) -> str:
    """Lays bricks to cover the specified area in square meters."""
    return f"Laid bricks to cover {area} square meters."

@mcp.tool
def install_door(door_type: str) -> str:
    """Installs a door of the specified type."""
    return f"Installed a {door_type} door."

@mcp.tool
def mix_cement(ratio: str) -> str:
    """Mixes cement with the given ratio."""
    return f"Mixed cement with ratio {ratio}."

# --- Additional tools for full coverage ---

@mcp.tool
def join_wood(pieces: str) -> str:
    """Joins pieces of wood together."""
    return f"Joined wood pieces: {pieces}."

@mcp.tool
def apply_cement(surface: str) -> str:
    """Applies cement to a surface."""
    return f"Cement applied to {surface}."

@mcp.tool
def apply_brick(surface: str) -> str:
    """Applies brick to a surface."""
    return f"Brick applied to {surface}."

import requests
@mcp.tool
def query_knowledge_base(query: str) -> str:
    """Queries the knowledge base (Ollama LLM) for an answer."""
    try:
        resp = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma3", "prompt": query, "stream": False}
        )
        if resp.ok:
            data = resp.json()
            return data.get("response", "No response from LLM.")
        return f"Ollama error: {resp.status_code} {resp.text}"
    except Exception as e:
        return f"Ollama call failed: {e}"

# ---- START SERVER ---- #

if __name__ == "__main__":
    # Run with default settings (stdio) or specify sse
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
    