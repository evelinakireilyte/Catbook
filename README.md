# Catbook

## Installation

Enter the src directory

### Backend

#### Docker

In the root directory type

```
docker-compose up -d
```

To view the container logs use:

```
docker-compose logs -f
```

Shut the containers down with:

```
docker-compose down
```

#### Local

Install a virtual environment using:

```
python -m venv venv
```

activate by:

```
source venv/bin/activate
```

install the requirements with:

```
pip install -r requirements.txt
```

Apply database migrations:

```
docker-compose run web alembic upgrade head
```

### Frontend

To redeploy the frontend to the server: cd to the /frontend directory and run

```
npm install
npm run build
```

This will serve the latest frontend over localhost:8000

## Usage

Access the application at localhost:8000

## Development

To develop the frontend cd into the /frontend directory and run:

```
npm start
```

Then see the development app on localhost:3000. To upstate the served FastAPI app run:

```
npm build
```

## Catbook App Development process

I have created the app using Docker containers, FastAPI, PostgreSQL and React. I have put the app in containers to be simple to get working. I have served the static files through the main url by copying them into the /static directory using a post-build command in the package.json. I added middleware to disable the CORS protection and allow easy development of the react app using the backend apis. I added a .env file to keep variables in, only 1 currently.

### Backend

I have kicked things off by:

- Creating requirements.txt file, Dockerfile, docker-compose.yml containing configs for building and running 3 docker containers (web, db and pgadmin).

- Set up a PostgreSQL database along with SQLAlchemy and Alembic to handle migrations.

- Defined Models in models.py and made migrations to PostgreSQL. I decided to store information on two tables (documents and types, see image below) to minimise data storage as part of a future maintenance plan and link them through a foreign key. Data was initially added directly to the db trough localhost:5050 (Servers > pgadmin >Databases > postgres >Schemas >public>Tables) using credentials: user=pgadmin4@pgadmin.org and password=admin. Later I decided to use alembic to populate the db with the data directly so that the app can be viewed immediately on running the containers. The data can be viewed in pgadmin.

![DB tables/relations](https://res.cloudinary.com/eevelynaa1/image/upload/v1641396720/SEI_Project3/Blank_diagram_5_y3nvrs.png)

- Next up defined pydantic models in schema.py to allow SQLAlchemy models to be serialized to JSON.

- Set up main.py to include configs and get request to allow display data in the frontend. I have first checked it works by going to http://localhost:8000/docs and invoking 'get documents' endpoint.

### Frontend

- I followed the instructions provided and implemented features as listed in the document.

- Created React app and installed required dependencies.

- Created DocumentCard.js component to display content as cards using React-Bootsrap, each displaying document title and thumbnail.

- Created DocumentList.js page to display cards as a list by mapping through each one and used Flexbox to display 3 cards on the top row and 2 on the bottom row. Data was fetched making axios get request (see helpers/api.js)

- Implemented placeholder spinner using React useState hook and React-Bootstrap spinner.

- Implemented drag and drop using React-Beautiful DND hooks by defining draggable components and including a placeholder to minimise component shifting while performing the action.

- Implemented image overlay allowing to enlarge image when clicked on (and exit by pressing esc button on the keyboard) through the use of React-Bootstrap Modal and React useState and setShow hooks (see DocumentCard.js).

- Countdown timer displaying time remaining until the page content is re-fetched (every 5 minutes) was implemented using React Countdown.

### PART 5 - Maintenance

Future improvements would involve:

- Implementation of CRUD functionality by adding post, put and delete requests to the main.py. Post request would take in document type, title, image and position. Same would apply to put requests allowing user to edit documents if necessary. Old documents could be deleted through delete requests. Actions for posting, editing and deleting would require authorisation, meaning user registration and login had to be implemented as part of the process.

- Presuming user authorisation has been implemented, one to many relationship between users and documents table would allow to display documents the user has saved as 'work in progress', allowing for better visibility and planning.

- Additional features would include document filtering according to type and searching to allow users to quickly locate a document of interest. An option to zoom into picture overlays to be able to read fine text.
