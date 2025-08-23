# Claude Context for MCP Learning Project

## User Profile & Learning Style
- **Background**: Python developer learning MCP
- **Learning approach**: Workshop-style, hands-on coding alongside video course
- **Preference**: Step-by-step progression, wants to experience concepts rather than just explanations
- **Git workflow**: Commits at logical points with crisp 1-2 line messages, no pushing
- **File naming**: Folders with step numbers containing `server.py`, `test.sh`, `demo.png`

## Project Setup
- **Language**: Python 3.13
- **Package manager**: uv
- **MCP Library**: fastmcp
- **Repository**: Local git repo at `/home/prajwal/Downloads/learn-mcp`
- **Structure**: Folders per major concept with organized files, progressive numbering

## Course Context
- **Source**: https://mcp.holt.courses (JavaScript-based course)
- **Goal**: Convert JS examples to Python using fastmcp
- **Documentation**: https://gofastmcp.com/llms.txt and https://github.com/jlowin/fastmcp

## Current Progress
- ✅ Project setup with uv and Python 3.13
- ✅ fastmcp installed
- ✅ Created `1_addition_mcp_server/` with basic addition tool
- ✅ MCP server tested and working
- ✅ Created `test.sh` with step-by-step JSON-RPC testing
- ✅ Configured Claude Desktop with MCP server using .venv/bin/python
- ✅ Tested MCP server in Claude Desktop successfully
- ✅ Created `2_weather_mcp_server/` with Open-Meteo API integration
- ✅ Weather MCP server tested with Seattle coordinates
- ✅ Added weather server to Claude Desktop config
- ✅ Reorganized project into folder structure with organized files
- ✅ Updated all paths and configurations for new structure
- ✅ Created `3_resources_mcp_server/` with database schema resource
- ✅ Implemented resources using FastMCP with read-only SQLite access
- ✅ Resources tested and working in Claude Desktop
- ✅ Created `4_prompts_mcp_server/` with code review prompt template
- ✅ Implemented prompts using FastMCP @mcp.prompt decorator
- ✅ Created Python style guide and sample code for review
- ✅ Prompts tested and working in Claude Desktop
- 🔄 Ready for next lesson: Advanced MCP topics or Issues Tracker project

## Key Technical Notes
- FastMCP uses `@mcp.tool`, `@mcp.resource`, `@mcp.prompt` decorator patterns
- Server creation: `FastMCP(name="server-name")`
- Type hints required for tool functions
- Main execution: `mcp.run()` for stdio transport
- JSON-RPC testing: initialize → initialized notification → methods/list → methods/call
- Test script shows step-by-step i1→o1, i2→o2, i3→o3 interaction flow
- Resources use read-only SQLite connections: `sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)`
- Prompts read external files at startup and create templated instructions

## Current Status
- **Last completed**: Prompts section - code review prompt template implementation
- **Ready for**: Next MCP course section (Advanced topics or Issues Tracker project)
- **Course position**: Completed "Let's Build an MCP Server" - Tools, Resources, and Prompts sections

## File Structure
```
/learn-mcp/
├── 1_addition_mcp_server/
│   ├── server.py       # Basic addition tool
│   ├── test.sh         # JSON-RPC testing
│   └── demo.png        # Screenshot
├── 2_weather_mcp_server/
│   ├── server.py       # Weather API integration
│   ├── test.sh         # JSON-RPC testing  
│   └── demo.png        # Screenshot
├── 3_resources_mcp_server/
│   ├── server.py       # Database schema resource
│   ├── test.sh         # JSON-RPC testing
│   ├── demo.png        # Screenshot
│   └── database.sqlite # SQLite database file
├── 4_prompts_mcp_server/
│   ├── server.py       # Code review prompt template
│   ├── test.sh         # JSON-RPC testing
│   ├── demo.png        # Screenshot
│   ├── python_style_guide.md    # PEP 8 style guide
│   └── script_to_be_reviewed.py # Sample code with style issues
├── README.md           # Project overview with images
├── CLAUDE.md          # This context file
├── course_content.txt  # Full course content (no need to refetch)
└── fastmcp_docs.txt    # FastMCP documentation
```

## Claude Desktop Configuration
Path: `/home/prajwal/.config/Claude/claude_desktop_config.json`
- All four servers configured with folder structure paths
- Uses `.venv/bin/python` from project root
- Server names: addition-server, weather-server, database-schema-server, code-review-server

## MCP Concepts Learned
1. **Tools** (`@mcp.tool`): LLM-callable functions (addition, weather API)
2. **Resources** (`@mcp.resource`): Static content user provides (database schema)  
3. **Prompts** (`@mcp.prompt`): Templated instructions user provides (code review)

## Next Steps Context
When resuming:
1. Continue with next course section from `course_content.txt` 
2. Next likely sections: MCP Server Design, API Based Tools, Jobs Based Tools, or Issues Tracker project
3. Follow same pattern: create `5_[concept]_mcp_server/` folder structure
4. Convert JavaScript examples to Python using fastmcp
5. Test and commit at logical points

## Interaction Guidelines
- User prefers minimal explanations unless asked
- Focus on hands-on implementation
- Use TodoWrite for task tracking
- Learning output style active (insights and collaborative coding)
- Git commits at logical progression points