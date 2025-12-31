from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="Production-ready FastAPI microservice template",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_allowed_origins(),  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
    }


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "FastAPI Microservice Template",
        "version": "1.0.0",
        "docs": "/docs",
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Actions to perform on application startup"""
    print(f"Starting {settings.APP_NAME}...")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Actions to perform on application shutdown"""
    print(f"Shutting down {settings.APP_NAME}...")