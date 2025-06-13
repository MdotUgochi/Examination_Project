This is an Event Management API system built with FastAPI that allows users register for events, track attendance, and manage both event information and speaker details.



Features
* Create and Manage events with endpoints to create, read, update, delete, and close registration.

* Create and Manage users with endpoints that enables users to create, read, update, delete, and deactivate registration.

* Interactive and easy to use API documentation via Swagger UI

* In-memory data storage (no external database required)




RUNNING THE APPLICATION
* To run the application:
* clone the repository,
* create and activate a virtual enviroment
* install the dependencies contained in the requirements.txt file,
* start the fastAPI server by running "uvicorn main:app --reload" (without the quotes),
* visit and try out the API documentation at:
  Swagger UI: http://127.0.0.1:8000/docs

NOTE: Because this app uses an in-memory database, data is lost once the server restarts.

