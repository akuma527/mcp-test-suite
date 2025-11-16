# agent.py
from python_a2a import A2AServer, agent, run_server, TaskStatus, TaskState
import asyncio
from fastmcp import Client
from gemma3_client import query_gemma3
from llm_router import select_tool_with_llm

@agent(
    name="Builder Agent",
    description="Coordinates Painter, Carpenter, and Mason agents to build a house.",
    version="1.0.0"
)
class BuilderAgent(A2AServer):
    def handle_task(self, task):
        message_data = task.message or {}
        content = message_data.get("content", {})
        text = content.get("text", "") if isinstance(content, dict) else ""
        response_text = ""
        
        llm_result = select_tool_with_llm(text)
        
        if isinstance(llm_result, dict) and "agent" in llm_result and "tool" in llm_result:
            async def call_mcp():
                client = Client("http://localhost:8000/mcp")
                async with client:
                    try:
                        tool_name = llm_result["tool"]
                        # Get arguments, default to empty dict
                        arguments = llm_result.get("arguments", {})
                        
                        # Special handling for query_knowledge_base
                        if tool_name == "query_knowledge_base":
                            # If no arguments provided, use the original text as query
                            if not arguments or "query" not in arguments:
                                arguments = {"query": text}
                        
                        print(f"Calling tool: {tool_name} with args: {arguments}")
                        result = await client.call_tool(tool_name, arguments)
                        return result.data
                    except Exception as e:
                        return f"MCP error: {e}"
            
            response_text = asyncio.run(call_mcp())
        else:
            # Fallback to direct LLM query
            response_text = query_gemma3(text)
        
        task.artifacts = [{"parts": [{"type": "text", "text": response_text}]}]
        task.status = TaskStatus(state=TaskState.COMPLETED)
        return task

if __name__ == "__main__":
    agent = BuilderAgent(url="http://localhost:5400")
    run_server(agent, port=5400)