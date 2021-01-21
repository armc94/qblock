## Task management tool 

### Startig up
To start the app:
1. enter the project folder 
2. `sudo docker-compose build`
3. `sudo docker-compose up`

This will start the django app, the proxy and and the neo4j database.

Or in the development mode:
1. Go to qblock/docker/neo4j
2. sudo docker build -t neo4j . -> to create an image for the container. It has
       to be done just once.
3. 'sudo docker run -p 7474:7474 -p 7473:7473 -p 7687:7687 -v neodb:/data neo4j'
       -> create docker container
4. go to -> qblock/qblock manage.py runserver


Before the app connects to the neo4j the db it has to be initialized and a user
needs to be created

### Folder structure

In qblock folder:
- api -> rest interfaces
- dbabs -> abstractization for neo4j db
- qapp -> main app, handlers
- qblock -> configuration folder 
- users -> user autentification/registration app
