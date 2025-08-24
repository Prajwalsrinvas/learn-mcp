#!/bin/bash

echo "Issues Tracker MCP Server Testing"
echo "=================================="
echo ""
echo "This folder contains both API-based and Job-based versions to demonstrate"
echo "the difference in approaches as taught in the MCP course."
echo ""
echo "Available servers:"
echo "1. job_based_server.py - Job-based approach (RECOMMENDED)"
echo "2. api_based_server.py - API-based approach (for comparison)"
echo ""

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_PYTHON="/home/prajwal/Downloads/learn-mcp/.venv/bin/python"

case "${1:-job}" in
    "api"|"api-based")
        echo "Starting MCP Inspector for API-Based Server..."
        echo "This version has 15+ tools that map 1:1 to REST API endpoints."
        echo "More flexible but harder for LLMs to use correctly."
        echo ""
        npx @modelcontextprotocol/inspector "$VENV_PYTHON" "$SCRIPT_DIR/api_based_server.py"
        ;;
    "job"|"job-based"|"")
        echo "Starting MCP Inspector for Job-Based Server (RECOMMENDED)..."
        echo "This version has 6 focused tools with opinionated workflows."
        echo "Less flexible but much easier for LLMs to use correctly."
        echo ""
        npx @modelcontextprotocol/inspector "$VENV_PYTHON" "$SCRIPT_DIR/job_based_server.py"
        ;;
    "help"|"-h"|"--help")
        echo "Usage: $0 [api|job]"
        echo ""
        echo "  api, api-based    - Test the API-based tools version"
        echo "  job, job-based    - Test the job-based tools version (default)"
        echo "  help              - Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0                # Test job-based version (default)"
        echo "  $0 job            # Test job-based version"  
        echo "  $0 api            # Test API-based version"
        echo ""
        echo "The job-based approach is recommended as it:"
        echo "- Is easier for LLMs to use correctly"
        echo "- Has better success rates with smaller models"
        echo "- Provides opinionated workflows"
        echo "- Reduces decision fatigue for the LLM"
        ;;
    *)
        echo "Unknown option: $1"
        echo "Use '$0 help' for usage information."
        exit 1
        ;;
esac