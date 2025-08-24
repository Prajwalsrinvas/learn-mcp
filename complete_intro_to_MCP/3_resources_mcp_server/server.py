#!/usr/bin/env python3

import sqlite3
from pathlib import Path

from fastmcp import FastMCP

# Create FastMCP server
mcp = FastMCP("issues-server", version="1.0.0")


@mcp.resource("schema://database")
async def database_schema() -> str:
    """Register the database schema resource"""
    # Use the database from the mcp-issue-tracker backend
    db_path = (
        Path(__file__).parent.parent
        / "mcp-issue-tracker"
        / "backend"
        / "database.sqlite"
    )

    if not db_path.exists():
        raise FileNotFoundError(f"Database file not found at {db_path}")

    # Connect to database and extract schema in read-only mode
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND sql IS NOT NULL ORDER BY name"
        )
        rows = cursor.fetchall()

        # Join all SQL statements with newlines and semicolons
        schema = "\n".join([row[0] + ";" for row in rows])
        return schema

    finally:
        conn.close()


if __name__ == "__main__":
    mcp.run()
