import requests
import json
from house_tools import PAINTER_TOOLS, CARPENTER_TOOLS, MASON_TOOLS

def select_tool_with_llm(user_query):
    """
    Use Ollama LLM to select the best tool and agent for a user query.
    Returns: (agent_name, tool_name, tool_args_dict)
    """
    tools = {
        "Painter Agent": PAINTER_TOOLS,
        "Carpenter Agent": CARPENTER_TOOLS,
        "Mason Agent": MASON_TOOLS
    }
    tool_list = []
    for agent, agent_tools in tools.items():
        for tool in agent_tools:
            tool_list.append({"agent": agent, **tool})
    
    prompt = f"""
You are a smart router for a house-building multi-agent system. Given a user request, select the best tool and agent to handle it. 

Available tools:
{json.dumps(tool_list, indent=2)}

User request: {user_query}

Respond in JSON with keys: agent, tool, and arguments (a dict of parameter values).
Example:
{{"agent": "Painter Agent", "tool": "apply_paint", "arguments": {{"surface": "wall"}}}}
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "gemma3", "prompt": prompt, "stream": False}
    )
    if response.ok:
        data = response.json()
        # Try to extract JSON from response
        import re
        import ast
        match = re.search(r'\{.*\}', data.get("response", ""), re.DOTALL)
        if match:
            try:
                return ast.literal_eval(match.group(0))
            except Exception:
                pass
        # fallback: return raw
        return data.get("response")
    return f"Ollama error: {response.text}"
