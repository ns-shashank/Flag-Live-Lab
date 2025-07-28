from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import feature_flags, audit_logs, websocket
from app.middleware import FeatureFlagMiddleware

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Feature Flag Live Lab")

# Add CORS middleware so frontend can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins in production like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom middleware
app.add_middleware(FeatureFlagMiddleware)

# Include routers
app.include_router(feature_flags.router)
app.include_router(audit_logs.router)
app.include_router(websocket.router)
