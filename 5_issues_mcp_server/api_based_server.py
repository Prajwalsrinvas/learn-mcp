#!/usr/bin/env python3

import sqlite3
import json
import os
from pathlib import Path
from typing import Optional, List
import httpx
from pydantic import BaseModel, Field

from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("issues-tracker-api-server")

# Configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:3000/api")

# Pydantic Models
class IssueCreateData(BaseModel):
    api_key: str = Field(description="API key for authentication")
    title: str = Field(description="Issue title")
    description: Optional[str] = Field(None, description="Issue description")
    status: Optional[str] = Field(None, description="Issue status (not_started, in_progress, done)")
    priority: Optional[str] = Field(None, description="Issue priority (low, medium, high, urgent)")
    assigned_user_id: Optional[str] = Field(None, description="Assigned user ID")
    tag_ids: Optional[List[int]] = Field(None, description="Array of integer tag IDs")

class IssueUpdateData(BaseModel):
    api_key: str = Field(description="API key for authentication")
    id: int = Field(description="Issue ID")
    title: Optional[str] = Field(None, description="Issue title")
    description: Optional[str] = Field(None, description="Issue description")
    status: Optional[str] = Field(None, description="Issue status (not_started, in_progress, done)")
    priority: Optional[str] = Field(None, description="Issue priority (low, medium, high, urgent)")
    assigned_user_id: Optional[str] = Field(None, description="Assigned user ID")
    tag_ids: Optional[List[int]] = Field(None, description="Array of integer tag IDs")


async def make_request(
    method: str, 
    url: str, 
    data: dict = None, 
    headers: dict = None
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
                "headers": dict(response.headers)
            }
        except Exception as error:
            return {
                "status": 0,
                "error": str(error)
            }


# Issues Tools

@mcp.tool()
async def issues_list(
    api_key: str,
    status: Optional[str] = None,
    assigned_user_id: Optional[str] = None, 
    tag_ids: Optional[str] = None,
    search: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    priority: Optional[str] = None,
    created_by_user_id: Optional[str] = None
) -> str:
    """Get a list of issues with optional filtering
    
    Args:
        api_key: API key for authentication
        status: Filter by status (not_started, in_progress, done)
        assigned_user_id: Filter by assigned user ID
        tag_ids: Comma-separated tag IDs
        search: Search in title and description
        page: Page number (default: 1)
        limit: Items per page (default: 10, max: 100)
        priority: Filter by priority (low, medium, high)
        created_by_user_id: Filter by creator user ID
    """
    params = {}
    
    for key, value in {
        "status": status,
        "assigned_user_id": assigned_user_id,
        "tag_ids": tag_ids,
        "search": search,
        "page": page,
        "limit": limit,
        "priority": priority,
        "created_by_user_id": created_by_user_id
    }.items():
        if value is not None:
            params[key] = value
    
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    url = f"{API_BASE_URL}/issues"
    if query_string:
        url += f"?{query_string}"
    
    result = await make_request("GET", url, headers={"x-api-key": api_key})
    return json.dumps(result, indent=2)


@mcp.tool()
async def issues_create(data: IssueCreateData) -> str:
    """Create a new issue
    
    Args:
        data: Issue creation data with all required and optional fields
    """
    # Extract API key for headers
    api_key = data.api_key
    
    # Prepare issue data (exclude api_key from the payload)
    issue_data = data.model_dump(exclude={"api_key"}, exclude_none=True)
    
    result = await make_request(
        "POST", f"{API_BASE_URL}/issues", 
        data=issue_data,
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def issues_get(api_key: str, id: int) -> str:
    """Get a specific issue by its ID
    
    Args:
        api_key: API key for authentication
        id: Issue ID
    """
    result = await make_request(
        "GET", f"{API_BASE_URL}/issues/{id}",
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def issues_update(data: IssueUpdateData) -> str:
    """Update an existing issue
    
    Args:
        data: Issue update data with all required and optional fields
    """
    # Extract API key and ID
    api_key = data.api_key
    issue_id = data.id
    
    # Prepare update data (exclude api_key and id from the payload)
    update_data = data.model_dump(exclude={"api_key", "id"}, exclude_none=True)
    
    result = await make_request(
        "PUT", f"{API_BASE_URL}/issues/{issue_id}",
        data=update_data,
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def issues_delete(api_key: str, id: int) -> str:
    """Delete an issue by ID
    
    Args:
        api_key: API key for authentication
        id: Issue ID
    """
    result = await make_request(
        "DELETE", f"{API_BASE_URL}/issues/{id}",
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


# Tags Tools

@mcp.tool()
async def tags_list(api_key: str) -> str:
    """Get all available tags
    
    Args:
        api_key: API key for authentication
    """
    result = await make_request(
        "GET", f"{API_BASE_URL}/tags",
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def tags_create(api_key: str, name: str, color: str) -> str:
    """Create a new tag
    
    Args:
        api_key: API key for authentication
        name: Tag name
        color: Tag color (hex format)
    """
    tag_data = {"name": name, "color": color}
    
    result = await make_request(
        "POST", f"{API_BASE_URL}/tags",
        data=tag_data,
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


@mcp.tool()
async def tags_delete(api_key: str, id: int) -> str:
    """Delete a tag by ID
    
    Args:
        api_key: API key for authentication
        id: Tag ID
    """
    result = await make_request(
        "DELETE", f"{API_BASE_URL}/tags/{id}",
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


# Users Tools

@mcp.tool()
async def users_list(api_key: str) -> str:
    """Get all users
    
    Args:
        api_key: API key for authentication
    """
    result = await make_request(
        "GET", f"{API_BASE_URL}/users",
        headers={"x-api-key": api_key}
    )
    return json.dumps(result, indent=2)


# API Key Tools

@mcp.tool()
async def api_key_verify(api_key: str) -> str:
    """Verify if an API key is valid
    
    Args:
        api_key: API key to verify
    """
    result = await make_request(
        "POST", f"{API_BASE_URL}/auth/api-key/verify",
        data={"key": api_key}
    )
    return json.dumps(result, indent=2)


# Health Check Tools

@mcp.tool()
async def health_status() -> str:
    """Get the health status of the API"""
    health_url = API_BASE_URL.replace("/api", "") + "/health"
    result = await make_request("GET", health_url)
    return json.dumps(result, indent=2)


@mcp.tool()
async def health_ready() -> str:
    """Check if the API is ready to serve requests"""
    ready_url = API_BASE_URL.replace("/api", "") + "/health/ready"
    result = await make_request("GET", ready_url)
    return json.dumps(result, indent=2)


@mcp.tool()
async def health_live() -> str:
    """Check if the API is alive"""
    live_url = API_BASE_URL.replace("/api", "") + "/health/live"
    result = await make_request("GET", live_url)
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