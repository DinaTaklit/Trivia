# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```
>Ps: In case the previous command does not work just process like this:
- First create the database "trivia": 
    ```
    CREATE DATABASE trivia OWNER name_of_owner
    ```
- Populate the trivia database using `trivia.psql` script 
    ```  
    psql -d trivia -U db_onwner -a -f trivia.psql
    ```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
>PS: if the command avbove does not work just process like this:

- First create the database of the test: 
    ```
    CREATE DATABASE trivia_test OWNER name_of_owner
    ```
- Populate the trivia_test database using `trivia.psql` script 
    ```  
    psql -d trivia_test -U db_onwner -a -f trivia.psql
    ```
- To run the test type: 
    ```
    python test_flaskr.py
    ``` 

# API Reference 

## Getting Started 

- **Base URL**: Base URL: Actually, this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default,`http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- **Authentication**: This version of the application does not require authentication or API keys.

## Error Handling 

Errors are returned as JSON object in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return four(04) error types when requests fail:
- 400: Bad Request 
- 404: Resource Not Found
- 405: Method Not allowed
- 422: Not Processable 
  
## Endpoints 

GET '/categories'
GET '/questions'
GET '/categories/{category_id}/questions' 
DELETE '/questions/{question_id}' 
POST '/questions'
POST /quizzes

### GET /categories

- General:
  - Returns a list of categories objects, success value and total number of categories
- Sample: `curl http://127.0.0.1:5000/categories` or `curl.exe http://127.0.0.1:5000/categories`  if the curl itself does not work
    ```
    {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true,
    "total_categories": 6
    }
    ```

### GET /questions

- General:
  - Returns a list of question objects, success value, questions, total number of question and lsit of all the categoris
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1
- Sample: `curl http://127.0.0.1:5000/questions` or `curl.exe http://127.0.0.1:5000/questions`  if the curl itself does not work

    ```
    "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ],
  "success": true,
  "total_questions": 26
  }
  ```

### GET /categories/{category_id}/questions 
- General:
  - Get questions based on category: returns a list of question objects, success value, questions, total number of question, current category and lsit of all the categoris
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1
- Sample: `curl http://127.0.0.1:5000/categories/1/questions` or `curl.exe http://127.0.0.1:5000/categories/1/questions`  if the curl itself does not work
    ```
    {
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": 1,
    "questions": [
        {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
        },
        {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 2
    }
    ```

### DELETE /questions/{question_id} 
- General: 
  - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value.

- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/5?page=2` 
    ```
    {
    "deleted": 5,
    "success": true,
    }
    ```

### POST /questions
- General: 
  -  Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value.
  -  If the POST methond include search term it will get the questions based on a search term
  
- Sample1: Create new question: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", "answer":"Maya Angelou"", "category":4, "difficulty": 2}'` or `curl.exe http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{\"question\":\"Whose autobiography is entitled I Know Why the Caged Bird Sings?\", \"answer\":\"Maya Angelou\", \"category\":4, \"difficulty\": 2}'`  if you are using ananconda PowerShell within windows: 
    
    ```
    {
    "created": 33,
    "success": true,
    }
    ```
- Sample2: Get question based on search item: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Whose"}'` or `curl.exe http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{\"searchTerm\":\"Whose\"}'`
  ```
  {
    "questions": [
      {
        "answer": "Whose autobiography is entitled I Know Why the Caged Bird Sings?",
        "category": 4,
        "difficulty": 2,
        "id": 33,
        "question": "Whose autobiography is entitled I Know Why the Caged Bird Sings?"
      }
    ],
    "success": true,
    "total_questions": 1
  }
  ```

### POST /quizzes
- General: 
  - Give a category and previous question parameters and return a random question within the given category, if provided, and that is not not one of the previous question. If none question found it returns none else it return success value with the randome question

- Sample: Create new question: 
    ```
    curl http://127.0.0.1:5000/quizzes -XPOST -H "Content-Type: application/json" -d 
    '{
        "quiz_category": {"type": "click","id": 0},
        "previous_questions":
        [22,16,18,17]
    }'
    ```
    or if you are using ananconda PowerShell within windows
    ```
    curl.exe http://127.0.0.1:5000/quizzes -XPOST -H "Content-Type: application/json" -d '{
        \"quiz_category\": {\"type\": \"click\",\"id\": 0},
        \"previous_questions\": [22,16,18,17]
        }'

    ```
    The result:  
   ``` 
    {
    "question": {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
    },
    "success": true
    }
    ```