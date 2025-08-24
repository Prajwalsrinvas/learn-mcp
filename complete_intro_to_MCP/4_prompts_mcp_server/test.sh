#!/bin/bash

# Test MCP prompts server with JSON-RPC commands step by step
# This demonstrates the complete MCP protocol flow for prompts

echo "--- 1. Sending initialize request ---"
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | python server.py 2>/dev/null | jq -c
echo ""

echo "--- 2. Sending initialized notification + listing prompts ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 2, "method": "prompts/list"}'
} | python server.py 2>/dev/null | jq -c
echo ""

echo "--- 3. Getting prompt with sample code (text only) ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 3, "method": "prompts/get", "params": {"name": "review_code", "arguments": {"code": "def test():\n    x=1\n    return x"}}}'
} | python server.py 2>/dev/null | jq -r '.result.messages[0].content.text'