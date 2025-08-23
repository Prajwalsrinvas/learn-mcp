# Learn MCP

Learning Model Context Protocol (MCP) using FastMCP in Python.

## MCP Servers

Each server is organized in its own folder containing:
- `server.py` - MCP server implementation
- `test.sh` - JSON-RPC testing script  
- `demo.png` - Screenshot demonstration

### 1. Addition Server (`1_addition_mcp_server/`)
Basic number addition tool demonstrating MCP tools functionality.

![Addition Server Demo](1_addition_mcp_server/demo.png)

### 2. Weather Server (`2_weather_mcp_server/`)
Weather data retrieval using Open-Meteo API with latitude/longitude coordinates.

![Weather Server Demo](2_weather_mcp_server/demo.png)

### 3. Resources Server (`3_resources_mcp_server/`)
Database schema resource demonstrating MCP resources functionality.

![Resources Server Demo](3_resources_mcp_server/demo.png)

## Key Concepts

- **Tools**: LLM decides when to call tools autonomously
- **Resources**: User provides resources to LLM manually (via ➕ button)
- **Resources are static** - no input parameters (unlike tools)
- **Resource templates** - support input parameters for dynamic resources
- **Read-only database connections** - safer for resources to prevent accidental modifications

## Technical Notes

- **Claude Desktop logs**: `~/.config/Claude/logs/`
- **Tool Design**: Avoid unnecessary tools - they confuse LLMs and increase context usage

## References

- [MCP Course](https://mcp.holt.courses)
- [FastMCP Documentation](https://gofastmcp.com)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)