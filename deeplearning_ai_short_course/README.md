# MCP: Build Rich-Context AI Apps with Anthropic 🔧⚡

- Code files from the DeepLearning.AI [short course on MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/)
- Instructor: Elie Schoppik, Head of Technical Education at Anthropic
- [Certificate](https://learn.deeplearning.ai/accomplishments/0d2a9ff9-262c-4fd4-bf9e-9cf36bebb4c5)

## Course Progression 📈

This course teaches MCP through hands-on implementation, progressing from basic chatbots to production-ready MCP ecosystems:

**Chatbot** → **MCP Server** → **MCP Client** → **Multi-Server** → **Full Features** → **Remote Deployment**

## What You'll Build 🛠️

### Research Paper MCP Server
- arXiv paper search with metadata storage  
- Tools, Resources, and Prompts for academic research
- Multi-transport support (stdio, SSE)

### Production MCP Ecosystem  
- Multi-server architecture with session management
- Integration with reference servers (filesystem, fetch)
- Remote deployment with Docker containerization

| No. | Concepts | NBSanity | GitHub |
|-----|----------|----------|--------|
| 1 | • Anthropic Claude integration for chatbots<br>• Direct tool integration with arXiv search<br>• Tool schema definition and execution<br>• Interactive chat loops and conversation flow<br>• Paper metadata storage and retrieval | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L3/L3.ipynb) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L3/L3.ipynb) |
| 2 | • FastMCP server framework introduction<br>• Tool extraction using @mcp.tool() decorators<br>• STDIO transport protocol setup<br>• MCP Inspector testing and debugging<br>• Server environment with UV package management | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L4/mcp_project/) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L4/mcp_project/) |
| 3 | • MCP client creation and integration<br>• ClientSession async management patterns<br>• STDIO client-server communication<br>• Tool discovery and dynamic invocation<br>• Session lifecycle and connection handling | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L5/mcp_project/) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L5/mcp_project/) |
| 4 | • Multi-server architecture design<br>• Server configuration file management<br>• Session mapping and tool routing<br>• AsyncExitStack for resource cleanup<br>• Reference server integration (filesystem, fetch) | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L6/mcp_project/) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L6/mcp_project/) |
| 5 | • Resource implementation with URI patterns<br>• Prompt template systems and parameterization<br>• Command-line interface with slash commands<br>• Dynamic resource access with @ syntax<br>• Complete MCP feature set utilization | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L7/mcp_project/) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L7/mcp_project/) |
| 6 | • SSE transport for remote server deployment<br>• Docker containerization and orchestration<br>• Cloud deployment strategies (Render.com)<br>• Production environment configuration<br>• Remote server testing and monitoring | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L9/mcp_project/) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/deeplearning_ai_short_course/L9/mcp_project/) |

## Key Learning Outcomes 📈

- **Progressive MCP Mastery**: Master the full MCP ecosystem from basic concepts to production deployment
- **Hands-on Implementation**: Build real working MCP servers and clients with practical applications  
- **Production Patterns**: Learn best practices for multi-server architectures and remote deployment
- **Integration Skills**: Connect MCP systems with existing tools and services