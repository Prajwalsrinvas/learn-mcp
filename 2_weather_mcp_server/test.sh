#!/bin/bash

echo "--- 1. Sending initialize request ---"
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}}' | uv run python server.py 2>/dev/null | jq -c

echo ""
echo "--- 2. Sending initialized notification + requesting tools ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list"}'
} | uv run python server.py 2>/dev/null | jq -c

echo ""
echo "--- 3. Calling get_weather tool for Seattle (47.6062, -122.3321) ---"
{
    echo '{"jsonrpc": "2.0", "method": "notifications/initialized"}'
    echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_weather", "arguments": {"latitude": 47.6062, "longitude": -122.3321}}}'
} | uv run python server.py 2>/dev/null | jq -c