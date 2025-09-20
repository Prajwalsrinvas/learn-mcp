# Build AI Apps with MCP Servers: Working with Box Files

- Code files from the DeepLearning.AI [short course on Build AI Apps with MCP Servers: Working with Box Files](https://www.deeplearning.ai/short-courses/build-ai-apps-with-mcp-server-working-with-box-files/)
- Instructor: Ben Kus, Chief Technology Officer at Box
- [Certificate](https://learn.deeplearning.ai/accomplishments/62773b0e-5598-4b8d-aaad-cc81cdb6c288)

## Course Progression

This course teaches practical MCP integration with cloud storage and multi-agent systems, progressing from local file processing to distributed agent architectures:

**Local Processing** → **MCP Integration** → **Multi-Agent Systems**

## What You'll Build

### Invoice Processing Application
- PDF invoice processing with field extraction (client name, amount, product)
- Cloud storage integration via Box MCP server
- Multi-agent system with A2A protocol communication

### Production MCP Ecosystem
- Google ADK agent framework implementation
- Agent-to-Agent (A2A) protocol communication
- Specialized agent coordination (Files Agent, Extraction Agent, Orchestrator)

| No. | Concepts | NBSanity | GitHub |
|-----|----------|----------|--------|
| 1 | • Local PDF invoice processing<br>• Google Gemini LLM integration<br>• SQLite database storage<br>• Field extraction (client name, amount, product)<br>• Manual file download and processing | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L1/L1.ipynb) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L1/L1.ipynb) |
| 2 | • Box MCP server integration<br>• MCP client session management<br>• Remote file access via Box API<br>• Tool discovery and invocation<br>• Cloud-based invoice processing without downloads | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L2/L2.ipynb) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L2/L2.ipynb) |
| 3 | • Multi-agent system architecture<br>• Google ADK (Agent Development Kit)<br>• A2A (Agent-to-Agent) protocol<br>• Agent cards and capabilities definition<br>• Orchestrator pattern with specialized sub-agents | [![Open In NBSanity](https://nbsanity.com/assets/icon.png)](https://nbsanity.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L3/L3.ipynb) | [![GitHub](https://cdn-icons-png.flaticon.com/32/270/270798.png)](https://github.com/Prajwalsrinvas/learn-mcp/blob/main/build_ai_apps_with_mcp_servers_working_with_box_files/L3/L3.ipynb) |

## Key Learning Outcomes

- **MCP Integration Mastery**: Transform local applications into MCP-compliant cloud-connected systems
- **Box Cloud Storage**: Leverage Box MCP server for secure file access and processing
- **Multi-Agent Architecture**: Build coordinated agent systems using Google ADK and A2A protocol
- **Production Patterns**: Learn enterprise-ready patterns for document processing workflows

## Technical Stack

- **LLM**: Google Gemini 2.5 Flash/Pro
- **Cloud Storage**: Box with MCP server integration
- **Agent Framework**: Google ADK (Agent Development Kit)
- **Communication**: A2A (Agent-to-Agent) protocol
- **Database**: SQLite for invoice data storage
- **File Processing**: PyPDF2 for local processing, Box AI for cloud extraction

## Architecture Evolution

### Lesson 1: Local Processing
```
User Request → Local PDF Files → Gemini API → SQLite Database → Report
```

### Lesson 2: MCP Integration
```
User Request → MCP Client → Box MCP Server → Box Cloud → Gemini API → Database → Report
```

### Lesson 3: Multi-Agent System
```
User Request → A2A Client → Orchestrator Agent
                              ↓
                         Files Agent ←→ Box MCP Server
                              ↓
                       Extraction Agent ←→ Box MCP Server
                              ↓
                           Report Generation
```

## Getting Started

1. **Prerequisites**:
   ```bash
   pip install google-genai box-sdk-gen mcp python-dotenv PyPDF2
   pip install google-adk a2a-sdk nest-asyncio uvicorn
   ```

2. **Environment Setup**:
   - Copy `env.example` to `.env` in each lesson folder
   - Configure Box API credentials and Gemini API key
   - Set up Box folder with sample invoices

3. **Run Lessons**:
   - L1: Local processing with manual file downloads
   - L2: MCP integration with Box cloud storage
   - L3: Multi-agent system with A2A protocol

## Box MCP Server Features

- **File Operations**: List folder contents, access file metadata
- **AI Extraction**: Leverage Box AI for intelligent text extraction
- **Secure Access**: OAuth-based authentication with Box API
- **Scalability**: Handle large document repositories efficiently

## Multi-Agent Components

### Files Agent
- **Purpose**: List and discover files in Box folders
- **Tools**: `box_list_folder_content_by_folder_id`
- **Output**: File IDs and metadata

### Extraction Agent
- **Purpose**: Extract structured data from specific documents
- **Tools**: `box_ai_extract_freeform_tool`
- **Output**: JSON-formatted invoice fields

### Orchestrator Agent
- **Purpose**: Coordinate workflow between specialized agents
- **Communication**: A2A protocol with sub-agents
- **Intelligence**: Task planning and result aggregation