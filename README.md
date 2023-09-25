# Navigation
* ***[Project description](#project-description)***
* ***[Software versions](#software-versions)***
* ***[Getting started](#getting-started)***
   * ***[Run via Docker Compose](#run-via-docker-compose)***
   * ***[Run locally](#run-locally)***
* ***[Creating superuser](#creating-superuser)***
* ***[Usage](#usage)***
* ***[Database](#database)***

## Project description
The project is a test task for the company [1ak.by/](https://1ak.by/) and is a compact web-service "Library" for automating the accounting of issuing books to readers.
The service provides simple web-interface for keeping track of readers and accounting for the issuance and storage of books.

## Software versions
- python:3.11.5
- PIP_VERSION:23.2.1
- POETRY_VERSION:1.6.1

## Getting started
You have got two ways of running the project

### Run via Docker Compose
To run this project, follow the steps below:
1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) on your computer if they are not already installed.
2. Clone the repository to your local machine.
3. Navigate to the root directory of the project.
4. configure `.env` file by assigning values to the variables defined in `.env.sample`
 - ***NOTE: The variable values specified in `.env.sample` are just for example. You must configure `.env` file with your own settings***
5. In the project directory, run `docker-compose up --build` to start the services.

### Run locally
To run this project locally, first of all make sure that you have `python 3.11.5` or above installed on your maschine. Then follow next steps:
1. Install `poetry 1.6.1` by running `pip install poetry==1.6.1`.
2. Make sure that you've got database available.
3. Make steps 2 - 4 of the instruction above.
4. Create and activate virtual environment by running `poetry shell`.
5. Install dependencies by running `poetry install`.
6. Apply migrations by running `python project/manage.py migrate`.
7. [Optional] you can run `python project/create_default_db_data.py`to fill you database with default superuser, books and authors.
8. Start development server by running `python project/manage.py runserver`.

After completing these steps, the project will be running and available at [http://localhost:8000/](http://localhost:8000/).


## Creating superuser

If you already followed the **[Run via Docker Compose](#run-via-docker-compose)** section steps or completed the step **7** of **[Run locally](#run-locally)** instruction, superuser will be automatically created with the credentials provided in `.env` variables `SUPERUSER_USERNAME` and `SUPERUSER_PASSWORD`.
This superuser can be used to get access to the django admin panel which is available at [http://localhost:8000/admin](http://localhost:8000/admin).
If you want to create another superuser you can also run command `python project/manage.py createsuperuser` and followed the instructions in console.

## Usage
Here are the small description of project functionality.

The main page of the project displays a list of library readers in the format "last name, first name, patronymic". 
If the reader is not in the list, he can click the "Add Reader" button and will be taken to an input form page where he can enter his details. 
Upon successful submission of the form, the reader is returned to the main page, where he already appears in the list. 
By clicking on his name in the list, the reader is taken to his individual page, which displays information about all the books that this reader has taken, including the author, title, code and date the book was issued to the reader. 
The page also contains a “Get a book” button, by clicking on which the reader is taken to the book list page, where a list of all available and issued books is displayed. Books issued are displayed with information about the reader to whom they were issued and the date the book was issued to the reader. Reader can choose one
or more books that he wants to take in special form provided at the end of the page.

***NOTE: The right to add, update or remove books and authors belongs only to superuser via the admin-panel***

Available pages:
  - Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)
  - Main page (list of readers): [http://localhost:8000/](http://localhost:8000/)
  - Reader's page: [http://localhost:8000/readers/<reader_id>](http://localhost:8000/readers/<reader_id>)
  - Create reader page: [http://localhost:8000/readers/create](http://localhost:8000/readers/create)
  - Books page (list of books): [http://localhost:8000/books](http://localhost:8000/books)

***NOTE: The address 'localhost:8000' shown here just for example. In reality, the actual address depends on host on which the application is deployed***

## Database
The project was written to use the MySQL database, the service of which is used in docker-compose. 
However, you can use any other database that Django supports, but unfortunately, you have to deploy it yourself. 
To do this, you can follow next steps:
1. Deploy your database
2. Install appropriate drivers that allows python to work with database (for example `psycopg2` for PostgreSQL by running `poetry add psycopg2`)
3. Specify the data for connecting to the database in the `.env` file
