import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgres://{}:{}@{}/{}".format('dina','dina','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        
        # Use it to test the creation of new question 
        self.question = {
            'question': 'Who discovered penicillin?',
            'answer': 'Alexander Fleming', 
            'category': 1, 
            'difficulty': 3, 
        }
        # User it to get a question to play the quiz 
        self.quiz = {
            'Previous_questions': [16,18],
            'quiz_category':{
                'id': 2
            }
        }
        self.quiz_2 = {
            'previous_questions': []
        }
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    
    """
    TODO
    Test Get categories in both case success and faillure
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_categories'])               
     
    def test_404_no_categories_found(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)   
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')   
    """
    TODO
    Test Get questions success and fail case 
    """
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))

    #test retrive books requesting beyon valid page
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')  

    """
    TODO
    Test DELETE question success and fail case 
    """
    def test_delete_question(self):
        res = self.client().delete('/questions/21')
        data = json.loads(res.data)
        question= Question.query.filter(Question.id == 21).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 21)
        self.assertEqual(question,None)
    
    def test_422_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()