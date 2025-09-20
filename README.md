# Learn MCP 🔧⚡

Learning Model Context Protocol (MCP) through comprehensive courses and hands-on implementations.

## What is MCP? 🧩

The Model Context Protocol (MCP) transforms how we build AI applications by providing a standardized way to connect AI systems to external data sources, tools, and services:

- **Standardized Integration** - Replace fragmented custom integrations with a single, open protocol
- **Client-Server Architecture** - Clean separation between AI applications (clients) and data/tool providers (servers)
- **Rich Context Access** - Give AI models access to real-time data, tools, and resources through standardized interfaces
- **Ecosystem Compatibility** - Leverage growing ecosystem of MCP servers and integrate with tools like Claude Desktop, VS Code, and more
- **Secure by Design** - Built-in security with explicit user approval for tool and resource access

## Core MCP Concepts 🛠️

### MCP Server - Expose Functionality
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def my_tool(param: str) -> str:
    """A tool that LLMs can call."""
    return f"Result: {param}"

@mcp.resource("data://resource")
def my_resource() -> str:
    """Static content for LLM context."""
    return "Resource content"

@mcp.prompt()
def my_prompt(topic: str) -> str:
    """Template for LLM instructions."""
    return f"Please analyze {topic}..."
```

### MCP Client - Connect AI to Servers
```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Connect to MCP server
server_params = StdioServerParameters(command="python", args=["server.py"])
async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await session.list_tools()
```

## Courses 📚

### [Complete Intro to MCP](complete_intro_to_MCP/) 
Holt course content with Python FastMCP implementations
- 5 working MCP servers showcasing core concepts
- Tools, Resources, Prompts, and Design Patterns
- Job-based vs API-based tool design comparison
- Real working examples with screenshots

### [DeepLearning.AI MCP Course](deeplearning_ai_short_course/)
Advanced MCP concepts and production patterns
- Progressive learning: Chatbot → Server → Client → Multi-Server → Production
- Building complete MCP ecosystems
- Remote deployment and Docker containerization
- Integration with multiple reference servers

### [Build AI Apps with MCP Servers: Working with Box Files](build_ai_apps_with_mcp_servers_working_with_box_files/)
Practical MCP integration with cloud storage and multi-agent systems
- Document processing with Box cloud storage integration
- Google ADK agent framework and A2A protocol
- Multi-agent orchestration patterns
- Enterprise-ready document workflow automation

## Quick Start 🚀

1. **Install dependencies**:
   ```bash
   uv venv && source .venv/bin/activate
   uv pip install fastmcp httpx
   ```

2. **Test any server**:
   ```bash
   # Test with MCP Inspector
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Add to Claude Desktop**: Follow [FastMCP integration guide](https://gofastmcp.com/integrations/claude-desktop)

## Resources 📖

### Official MCP Resources
- 🌐 **[Model Context Protocol](https://modelcontextprotocol.io)** - Official specification
- 📦 **[MCP GitHub Repository](https://github.com/modelcontextprotocol)** - Official implementations
- 🐍 **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** - Python development kit
- 🗂️ **[MCP Server Collection](https://github.com/modelcontextprotocol/servers)** - Reference server implementations

### Development Tools
- ⚡ **[FastMCP Framework](https://github.com/jlowin/fastmcp)** - High-level Python MCP framework  
- 📝 **[FastMCP Documentation](https://gofastmcp.com)** - Complete FastMCP guide
- 🔍 **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)** - Interactive testing tool
- 📦 **[UV Package Manager](https://docs.astral.sh/uv/)** - Python environment management

### Learning Resources
- 🎓 **[Complete Intro to MCP](https://mcp.holt.courses)** - Comprehensive MCP course by Holt
- 🎓 **[DeepLearning.AI MCP Course](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/)** - Advanced MCP with Anthropic

### Integration Examples  
- 🖥️ **[Claude Desktop MCP](https://docs.anthropic.com/en/docs/mcp)** - Official Anthropic integration
- 💻 **[VS Code MCP Support](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)** - IDE integration