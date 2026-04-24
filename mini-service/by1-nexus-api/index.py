#!/usr/bin/env python3
"""
BY1-Nexus API Server Entry Point

Start the FastAPI server on port 3031.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=3031,
        reload=True,
        log_level="info"
    )
