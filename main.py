from fastapi import FastAPI
from uuid import uuid4


from routes import user, event, speaker, registration
from database import db



#App Instance
app = FastAPI(
    title="Event Management API",
    description="Manage events, users, registrations, and speakers",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"Welcome to my Event Management"}


app.include_router(event.router, prefix="/events", tags=["Events"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(registration.router, prefix="/registrations", tags=["Registration"])
app.include_router(speaker.router, prefix="/speakers", tags=["Speakers"])


#Initialize_speakers():


