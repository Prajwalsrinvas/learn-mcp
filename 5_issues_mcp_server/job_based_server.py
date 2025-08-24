#!/usr/bin/env python3

"""
Issues Tracker MCP Server - Job-Based Tools (Recommended Approach)

This is the main server file that uses the job-based approach as recommended
by the MCP course. For the API-based approach comparison, see api_based_server.py

The job-based approach provides:
- Opinionated workflows that are easier for LLMs to use correctly
- Focused, single-purpose tools
- Hardcoded sensible defaults
- Better success rate with smaller models

Compare this with api_based_server.py to see the difference in approaches.
"""

import json
import os
import sqlite3
from pathlib import Path

import httpx
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("issues-tracker-server")

# Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3000/api")

# Hardcoded tag IDs from database (matching course approach)
BUG_TAG_ID = 3
FEATURE_TAG_ID = 4


async def make_request(
    method: str, url: str, data: dict = None, headers: dict = None
) -> dict:
    """Helper function to make HTTP requests"""
    default_headers = {"Content-Type": "application/json"}
    if headers:
        default_headers.update(headers)

    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=default_headers)
            elif method.upper() == "POST":
                response = await client.post(url, json=data, headers=default_headers)
            elif method.upper() == "PUT":
                response = await client.put(url, json=data, headers=default_headers)
            elif method.upper() == "DELETE":
                response = await client.delete(url, headers=default_headers)

            try:
                json_result = response.json()
            except:
                json_result = response.text

            return {
                "status": response.status_code,
                "data": json_result,
                "headers": dict(response.headers),
            }
        except Exception as error:
            return {"status": 0, "error": str(error)}


# Job-Based Tools - Opinionated Workflows


@mcp.tool()
async def create_bug(api_key: str, title: str, description: str) -> str:
    """Create a new bug issue with high priority and bug tag

    This is an opinionated tool that automatically:
    - Sets priority to "high"
    - Sets status to "not_started"
    - Applies the "bug" tag

    Args:
        api_key: API key for authentication
        title: Bug title
        description: Bug description
    """
    # Create bug with opinionated defaults
    issue_data = {
        "title": title,
        "description": description,
        "priority": "high",
        "status": "not_started",
        "tag_ids": [BUG_TAG_ID],  # Hardcoded bug tag ID
    }

    result = await make_request(
        "POST",
        f"{API_BASE_URL}/issues",
        data=issue_data,
        headers={"x-api-key": api_key},
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def create_feature_request(api_key: str, title: str, description: str) -> str:
    """Create a new feature request issue with low priority and feature tag

    This is an opinionated tool that automatically:
    - Sets priority to "low"
    - Sets status to "not_started"
    - Applies the "feature" tag

    Args:
        api_key: API key for authentication
        title: Feature request title
        description: Feature request description
    """
    # Create feature request with opinionated defaults
    issue_data = {
        "title": title,
        "description": description,
        "priority": "low",
        "status": "not_started",
        "tag_ids": [FEATURE_TAG_ID],  # Hardcoded feature tag ID
    }

    result = await make_request(
        "POST",
        f"{API_BASE_URL}/issues",
        data=issue_data,
        headers={"x-api-key": api_key},
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def update_ticket_status(api_key: str, id: int, status: str) -> str:
    """Update the status of an existing ticket/issue

    Simple, focused tool for status updates only.

    Args:
        api_key: API key for authentication
        id: Issue ID to update
        status: New status for the ticket (not_started, in_progress, done)
    """
    if status not in ["not_started", "in_progress", "done"]:
        return json.dumps(
            {"error": "Invalid status. Must be one of: not_started, in_progress, done"},
            indent=2,
        )

    result = await make_request(
        "PUT",
        f"{API_BASE_URL}/issues/{id}",
        data={"status": status},
        headers={"x-api-key": api_key},
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def create_urgent_issue(api_key: str, title: str, description: str) -> str:
    """Create a new urgent issue that needs immediate attention

    This is an opinionated tool that automatically:
    - Sets priority to "urgent"
    - Sets status to "not_started"
    - Does not assign any specific tag (could be bug or feature)

    Args:
        api_key: API key for authentication
        title: Urgent issue title
        description: Urgent issue description
    """
    issue_data = {
        "title": title,
        "description": description,
        "priority": "urgent",
        "status": "not_started",
    }

    result = await make_request(
        "POST",
        f"{API_BASE_URL}/issues",
        data=issue_data,
        headers={"x-api-key": api_key},
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def list_my_issues(api_key: str) -> str:
    """List all issues in the system

    Simplified listing tool - gets all issues without complex filtering.
    For job-based approach, we keep tools simple and focused.

    Args:
        api_key: API key for authentication
    """
    result = await make_request(
        "GET", f"{API_BASE_URL}/issues", headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def get_issue_details(api_key: str, id: int) -> str:
    """Get detailed information about a specific issue

    Args:
        api_key: API key for authentication
        id: Issue ID
    """
    result = await make_request(
        "GET", f"{API_BASE_URL}/issues/{id}", headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


# Database Schema Resource


@mcp.resource("schema://database")
async def get_database_schema() -> str:
    """SQLite schema for the issues database"""
    # Get the database path relative to the mcp-issue-tracker folder
    current_dir = Path(__file__).parent
    project_root = current_dir.parent
    db_path = project_root / "mcp-issue-tracker" / "backend" / "database.sqlite"

    if not db_path.exists():
        return "Database file not found. Make sure the issue tracker backend is set up."

    try:
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND sql IS NOT NULL ORDER BY name"
        )

        schemas = []
        for row in cursor.fetchall():
            schemas.append(row[0] + ";")

        conn.close()
        return "\n".join(schemas)

    except Exception as e:
        return f"Error reading database schema: {str(e)}"


if __name__ == "__main__":
    mcp.run()
