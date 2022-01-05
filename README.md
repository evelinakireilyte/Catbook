# Catbook

## Installation

Enter the src directory

### Backend

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

cd to the /frontend directory and run

```
npm install
npm run build
```

<!-- Do I want to talk about about docker commands?

Create and start containers with:

```
docker-compose build --no-cache
docker-compose up -d
```

List containers and access each by typing specified PORT into the browser:

```
docker compose ps
``` -->

## Usage/Development

To develop the frontend cd into the /frontend directory and run:

```
npm start
```

Then see the development app on localhost:3000. To upstate the served FastAPI app run:

```
npm build
```

## Catbook App Development process

I have created the app using Docker containers, FastAPI, PostgreSQL and React.

### Backend

I have kicked things off by:

- Creating requirements.txt file, Dockerfile, docker-compose.yml containing configs for building and running 3 docker containers (web, db and pgadmin).

- Set up a PostgreSQL database along with SQLAlchemy and Alembic to handle migrations.

- Defined Models in models.py and made migrations to PostgreSQL. I decided to store information on two tables (documents and types) to minimise data storage and link them through a foreign key. Data was added directly to the db trough localhost:5050 (Servers > pgadmin >Databases > postgres >Schemas >public>Tables) login with user=pgadmin4@pgadmin.org and password=admin.

![DB tables/relations](https://res.cloudinary.com/eevelynaa1/image/upload/v1641396720/SEI_Project3/Blank_diagram_5_y3nvrs.png)

- Next up defined pydantic models in schema.py to allow SQLAlchemy models to be serialized to JSON.

- Set up main.py to include configs and get request to allow display data in the front end. I have first checked it works by going to http://localhost:8000/docs and invoking get documents endpoint.

### Frontend

- I followed the instructions provided and implemented features as listed in the document.

- Created React app and installed required dependencies.

- Created DocumentCard.js component to display content as cards using React-Bootsrap, each displaying document title and thumbnail.

- Created DocumentList.js page to display cards as a list by mapping through each one and used Flexbox to display 3 cards on the top row and 2 on the bottom row. Data was fetched making axios get request (see helpers/api.js)

- Implemented placeholder spinner using React useState hook and React-Bootstrap spinner.

- Implemented drag and drop using React-Beautiful DND hooks by defining draggable components and including a placeholder to minimise component shifting while performing the action.

- Implemented image overlay allowing to enlarge image when clicked on (and exit by pressing esc button on the keyboard) through the use of React-Bootstrap Modal and React useState and setShow hooks (see DocumentCard.js).
