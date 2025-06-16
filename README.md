This is an Event Management API system built with FastAPI and runs with an in-memory data storage.


The API enables to:
* Create and manage users and events  
* Register users for events  
* Mark attendance  
* Filter users who attended at least one event

Framework: FastAPI

RUNNING THE APPLICATION
* To run the application:
* clone the repository,
* create and activate a virtual enviroment
* install the dependencies contained in the requirements.txt file,
* start the fastAPI server by running "uvicorn main:app --reload" (without the quotes) on the terminal,
* The server will run at:
http://127.0.0.1:8000 and try out the Swagger documentation at: http://127.0.0.1:8000/docs

NOTE: Because this app uses an in-memory database, data is lost once the server restarts.

API ENDPOINTs
1. Users
GET/users/:  List all users
GET/users/{user_id}: Get a single user by ID
POST/users/: Create a new user
PUT	/users/{user_id}: Update an existing user
DELETE/users/{user_id}: Delete a user
PATCH	/users/{user_id}/deactivate: Deactivate a user
GET	/users/users/filter_attended: Get all users who have attended at least one event

2. Events
GET	/events/: List all events
GET	/events/{event_id}: Get a single event
POST/events/: Create a new event
PUT	/events/{event_id}: Update event details
DELETE	/events/{event_id}: Delete an event

3. Registration
POST/registrations: Register a user for an event
PATCH/registrations/{registration_id}/attend: Mark a user as attended(attendance).
GET/registrations: List all registrations
GET/registrations/{registration_id}: Get a specific registration

NOTE: Every new registration has attendance set to false until an admin marks the user as attended.