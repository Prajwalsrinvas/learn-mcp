#!/usr/bin/env python3

from pathlib import Path
from fastmcp import FastMCP

# Create FastMCP server
mcp = FastMCP("code-review-server", version="1.0.0")

# Read the Python style guide at startup
style_guide_path = Path(__file__).parent / "python_style_guide.md"
try:
    with open(style_guide_path, 'r', encoding='utf-8') as f:
        python_style_guide = f.read()
except FileNotFoundError:
    python_style_guide = "Python style guide not found."

@mcp.prompt
def review_code(code: str) -> str:
    """Review Python code for best practices and potential issues"""
    
    return f"""Please review this Python code to see if it follows our best practices. Use this Python style guide as a reference:

=============

{python_style_guide}

=============

Code to review:

{code}

Please provide specific feedback on:
1. Code style and PEP 8 compliance
2. Naming conventions
3. Code organization and structure
4. Best practices and potential improvements
5. Any potential bugs or issues

Format your response with clear sections and actionable recommendations."""

if __name__ == "__main__":
    mcp.run()