# Claude Context for MCP Learning Project

## User Profile
- **Background**: Python developer learning MCP through hands-on workshop approach
- **Learning Style**: Step-by-step progression, experience over explanation
- **Git Workflow**: Logical commits with crisp messages, no pushing

## Tech Stack
- **Python 3.13** + **uv** package manager + **FastMCP** library
- **Course**: https://mcp.holt.courses (JS → Python conversion)
- **Docs**: https://gofastmcp.com

## Progress Completed ✅
1. **Tools**: Addition server (`@mcp.tool`)
2. **APIs**: Weather server with Open-Meteo
3. **Resources**: Database schema (`@mcp.resource`) 
4. **Prompts**: Code review templates (`@mcp.prompt`)
5. **Design Patterns**: Job-based vs API-based comparison
   - `job_based_server.py` (6 focused tools, recommended)
   - `api_based_server.py` (15+ generic tools, comparison)

**Key Learning**: Job-based tools > API-based tools for LLM success

🔄 **Ready for**: Advanced MCP topics (Streamable HTTP, SSE, Vibe Coding)

## FastMCP Patterns
- **Decorators**: `@mcp.tool`, `@mcp.resource`, `@mcp.prompt`
- **Server**: `FastMCP(name="server-name")` + `mcp.run()`
- **Resources**: Read-only SQLite `"schema://database"` URI format
- **Testing**: `npx @modelcontextprotocol/inspector /path/to/python server.py`
- **Design**: Job-focused (opinionated) > API-focused (generic) tools

## Important Paths & Commands
- **Claude Desktop logs**: `~/.config/Claude/logs/`
- **Claude Desktop config**: `/home/prajwal/.config/Claude/claude_desktop_config.json`
- **Project venv**: `/home/prajwal/Downloads/learn-mcp/.venv/bin/python`
- **JSON-RPC flow**: initialize → initialized notification → methods/list → methods/call
- **Read-only SQLite**: `sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)`

## Project Structure
```
5_issues_mcp_server/
├── job_based_server.py  # 6 focused tools (RECOMMENDED)
├── api_based_server.py  # 15+ generic tools (comparison)
└── test.sh             # ./test.sh [job|api]
```

**All 5 servers configured**: addition-server, weather-server, database-schema-server, code-review-server, issues-tracker-server

## MCP Concepts
1. **Tools**: LLM-callable functions (LLM decides when to call)
2. **Resources**: User-provided static content (user attaches via ➕ button)
3. **Prompts**: User-provided templates (user attaches via ➕ button)  
4. **Design**: Job-based > API-based for LLM success

## Next Steps Context
- **Course Position**: Completed "Jobs Based Tools", ready for advanced topics
- **Next Sections**: Streamable HTTP, Server-side Events, Vibe Coding
- **Pattern**: Follow same structure, convert JS examples to Python using FastMCP

## Advanced Topics Completed ✅

### SSEs & Streaming HTTP
**Server-Side Events (SSEs)** were an initial approach for remote MCP servers, allowing clients to connect to HTTP endpoints for real-time communication. However, SSEs were quickly deprecated in favor of **Streamable HTTP**, which provides superior capabilities: resumable sessions with UUIDs, single endpoint management, and stateless server architecture for better scalability. Streamable HTTP enables production-ready remote MCP deployments while maintaining the real-time communication benefits.

### Vibe Coding  
**"Vibe Coding"** represents supervised agent development where you direct AI coding assistants enhanced by MCP servers. Key integrations include: **GitHub MCP** (workflow management, issue creation, PR generation), **Neon MCP** (database operations, schema management), **Playwright MCP** (UI testing, browser automation), and **Context7** (up-to-date documentation). This approach combines human oversight with AI capability, enabling full development workflows from requirements to deployment using tools like Claude Code, Cursor, and Windsurf.