# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

[View the README.md within ./backend for more details.](./frontend/README.md)
### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

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
  - Returns a list of question objects, success value, questions, total number of question, current category and lsit of all the categoris
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
  "current_category": [],
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
  - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total question, question list, current category and catoegory list based on current page number to update the frontend.

- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/5?page=2` 
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
    "current_category": [],
    "deleted": 5,
    "questions": [
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
        "answer": "Scarab",
        "category": 4,
        "difficulty": 4,
        "id": 23,
        "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
        "answer": null,
        "category": null,
        "difficulty": null,
        "id": 25,
        "question": null
        },
        {
        "answer": null,
        "category": null,
        "difficulty": null,
        "id": 26,
        "question": null
        },
        {
        "answer": null,
        "category": null,
        "difficulty": null,
        "id": 27,
        "question": null
        }
    ],
    "success": true,
    "total_questions": 25
    }
    ```

### POST /questions
- General: 
  -  Creates a new question using the submitted question, answer, category and difficulty. Returns the id of the created question, success value, total questions, question list, current category and list of actegories based on current page number to update the frontend.
  -  If the POST methond include search term it will get the questions based on a search term
  
- Sample1: Create new question: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", "answer":"Maya Angelou"", "category":4, "difficulty": 2}'` or `curl.exe http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{\"question\":\"Whose autobiography is entitled I Know Why the Caged Bird Sings?\", \"answer\":\"Maya Angelou\", \"category\":4, \"difficulty\": 2}'`  if you are using ananconda PowerShell within windows: 
    
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
    "created": 33,
    "current_category": [],
    "questions": [
        {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
        "answer": "Edward Scissorhands",
        "category": 5,
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
        "answer": "Muhammad Ali",
        "category": 4,
        "difficulty": 1,
        "id": 9,
        "question": "What boxer's original name is Cassius Clay?"
        },
        {
        "answer": "Brazil",
        "category": 6,
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
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
        }
    ],
    "success": true,
    "total_questions": 26
    }
    ```
- Sample2: Get question based on search item: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Whose"}'` or `curl.exe http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{\"searchTerm\":\"Whose\"}'`
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
  "current_category": [],
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