from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text 
from .database import database

app = FastAPI(title="FastAPI Scrapper", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to FastAPI Scrapper"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
    
@app.get("/health/db")
async def health_db_check(db: Session = Depends(database.get_db)):
  try: 
    db.execute(text("SELECT 1"))
    
    return {"status": "ok", "message": "Database connection is active."}
  except Exception as e:
    raise HTTPException(
        status_code=500,
        detail=f"Database connection fail: {str(e)}"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
