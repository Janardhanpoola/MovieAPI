# MovieAPI

## REST API for a Movie Model

Docker image is movieapi_web

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

GET /movieapi/<id>/
-->id is the particlar movie id

### Response


HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Get a non-existent movie

GET /movieapi/<id>/

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
PUT /movieapi/<id>/


### Response
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Change a movie's state (atleast one field to be specified)

### Request
PATCH /movieapi/<id>/

### Response

HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

# Delete a movie

### Request
DELETE /movieapi/<id>/

### Response
HTTP 204 No Content
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept














