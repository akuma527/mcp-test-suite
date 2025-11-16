# test_mcp_client.py
import asyncio
from fastmcp import Client

# Connect to the MCP server
client = Client("http://localhost:8000/mcp")

async def test_all_tools():
    print("=== Testing HouseBuilder MCP Server ===\n")
    
    async with client:
        # List available tools
        print("=== Available Tools ===")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  • {tool.name}: {tool.description}")
        print()
        
        # Test each tool
        print("=== Testing Tools ===\n")
        
        # Test 1: paint_wall
        print("1. Testing paint_wall...")
        result = await client.call_tool("paint_wall", {
            "color": "green",
            "surface": "garage"
        })
        print(f"   Result: {result.data}")
        print()
        
        # Test 2: cut_wood
        print("2. Testing cut_wood...")
        result = await client.call_tool("cut_wood", {
            "length": 150,
            "width": 75
        })
        print(f"   Result: {result.data}")
        print()
        
        # Test 3: lay_bricks
        print("3. Testing lay_bricks...")
        result = await client.call_tool("lay_bricks", {
            "area": 20.5
        })
        print(f"   Result: {result.data}")
        print()
        
        # Test 4: install_door
        print("4. Testing install_door...")
        result = await client.call_tool("install_door", {
            "door_type": "sliding glass"
        })
        print(f"   Result: {result.data}")
        print()
        
        # Test 5: mix_cement
        print("5. Testing mix_cement...")
        result = await client.call_tool("mix_cement", {
            "ratio": "1:2:3"
        })
        print(f"   Result: {result.data}")
        print()
        
        print("=== All tests completed! ===")

if __name__ == "__main__":
    asyncio.run(test_all_tools())