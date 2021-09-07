# MovieAPI

# REST API for a Movie Model

Steps to reproduce the application locally:

git clone https://github.com/Janardhanpoola/MovieAPI.git

pull the docker image using the command 
   - docker pull 1421333/movieapi_web:latest

to spin the container use:
   - docker-compose up

use port 8000 to access the api-endpoints:

   - http://localhost:8000/movieapi/

docker start <container_id> to start the container
docker stop <container_id> to stop the container

 - docker ps  -> list the containers.
 - docker images -> list the images

To check the application files use:
   - docker exec -it movieapi_web_1 /bin/sh
      - This opens interactive terminal. For instance, ls will list all the application files.

unit tests for this api are in the app's tests.py file

# Get list of all movies

Populated the movies list using faker module with the file name fakedata.py

### Request
GET /movieapi/

### Response

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Get a particluar movie

### Request

GET /movieapi/id/
-->id is the particlar movie id

### Response


HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Get a non-existent movie

GET /movieapi/id/

-->id is non existent movie id

HTTP 404 Not Found
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Create a movie

### Request

POST /movieapi/

### Response

HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept


# Change a movie's state (all fields are to be specified)

### Request
PUT /movieapi/id/


### Response
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Change a movie's state (atleast one field to be specified)

### Request
PATCH /movieapi/id/

### Response

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Delete a movie

### Request
DELETE /movieapi/id/

### Response
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept


















