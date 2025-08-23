#!/bin/bash

# Test MCP resources server with JSON-RPC commands step by step
# This demonstrates the complete MCP protocol flow for resources

echo "--- 1. Sending initialize request ---"
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | python server.py 2>/dev/null | jq -c
echo ""

echo "--- 2. Sending initialized notification + requesting resources ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 2, "method": "resources/list"}'
} | python server.py 2>/dev/null | jq -c
echo ""

echo "--- 3. Reading database-schema resource (text only) ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 3, "method": "resources/read", "params": {"uri": "schema://database"}}'
} | python server.py 2>/dev/null | jq -r '.result.contents[0].text'