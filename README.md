# Learn MCP

Learning Model Context Protocol (MCP) using FastMCP in Python.

## MCP Servers

Each server demonstrates core MCP concepts:
- **Tools**: LLM-callable functions 
- **Resources**: User-provided static content
- **Prompts**: User-provided templated instructions
- **Design Patterns**: Job-based vs API-based approaches

### 1. Addition Server - Tools (`1_addition_mcp_server/`)
Basic number addition tool demonstrating `@mcp.tool` decorator.

### 2. Weather Server - External APIs (`2_weather_mcp_server/`)
Weather data retrieval using Open-Meteo API with coordinates.

### 3. Resources Server - Static Content (`3_resources_mcp_server/`)
Database schema resource demonstrating `@mcp.resource` decorator.

### 4. Prompts Server - Templates (`4_prompts_mcp_server/`)
Code review prompt template demonstrating `@mcp.prompt` decorator.

### 5. Issues Tracker - Design Patterns (`5_issues_mcp_server/`)
Comparison of **Job-based vs API-based** MCP server design patterns.

**Key Learning**: Job-based tools (6 focused) vs API-based tools (15+ generic)

**Job-Based (`job_based_server.py`)**:
- 6 focused tools with opinionated workflows
- `create_bug`, `create_feature_request`, `create_urgent_issue`
- Better LLM success rates, less decision fatigue

**API-Based (`api_based_server.py`)**:
- 15+ tools mapping 1:1 to REST endpoints
- Generic CRUD operations
- Harder for LLMs, more errors in sequential calls

```bash
./test.sh      # Job-based (recommended)  
./test.sh api  # API-based (comparison)
```

## MCP Architecture

**Server-side (MCP Server provides)**:
- **Tools** (`@mcp.tool`): LLM-callable functions  
- **Resources** (`@mcp.resource`): Static content (user attaches via ➕)
- **Prompts** (`@mcp.prompt`): Templated instructions (user attaches via ➕)

**Client-side (Future features)**:
- **Roots**: File system access
- **Sampling**: Server-initiated LLM prompts  
- **Elicitation**: Server asks follow-up questions

## Design Philosophy

**Job-Based > API-Based**:
- Fewer focused tools > many generic tools
- Opinionated workflows > flexible but complex APIs
- Single-purpose > multi-step sequential calls

**Why LLMs prefer Job-Based**:
- Less decision fatigue with fewer tool choices
- Built-in guardrails and sensible defaults
- Avoid error-prone sequential API calls

## References

- [MCP Course](https://mcp.holt.courses)
- [FastMCP Documentation](https://gofastmcp.com)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp)