#!/bin/bash

# Test MCP server with JSON-RPC commands step by step
# This demonstrates the complete MCP protocol flow with immediate responses

echo "--- 1. Sending initialize request ---"
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | uv run python server.py 2>/dev/null | jq -c
echo ""

echo "--- 2. Sending initialized notification + requesting tools ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
} | uv run python server.py 2>/dev/null | jq -c
echo ""

echo "--- 3. Calling add tool with arguments (5 + 3) ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "add", "arguments": {"a": 5, "b": 3}}}'
} | uv run python server.py 2>/dev/null | jq -c