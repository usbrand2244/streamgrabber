from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import sys
import os

# Add the 'src' directory to the Python path so we can import streamgrabber
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# TODO: Replace this with the actual import from your streamgrabber code
# Example: from streamgrabber.core import grab_stream

app = FastAPI()

@app.get("/api/grab")
async def grab_stream_endpoint(imdb_id: str):
    if not imdb_id:
        raise HTTPException(status_code=400, detail="Missing 'imdb_id' parameter. Example: /api/grab?imdb_id=tt0137523")
    
    try:
        # TODO: Replace this placeholder with your actual streamgrabber function call
        # Example: result = await grab_stream(imdb_id)
        
        return JSONResponse(content={
            "success": True,
            "imdb_id": imdb_id,
            "message": "Replace this with the actual streamgrabber function call that returns the .m3u8 link."
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to grab stream: {str(e)}")
