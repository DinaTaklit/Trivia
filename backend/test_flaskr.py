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
        self.new_question = {
            'question': 'Who discovered penicillin?',
            'answer': 'Alexander Fleming', 
            'category': 1, 
            'difficulty': 3, 
        }
        # User it to get a question to play the quiz 
        self.quiz = {
            'previous_questions': [16,18],
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
        
    """
    TODO
    Test Create question success and fail case 
    """
    def test_create_new_question(self):
        res =  self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    def test_405_if_question_creation_not_allowed(self):
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')
        

    """
    TODO
    Test search questions with searchTerm success and fail case 
    """

    def test_get_questions_search_with_results(self):
        res = self.client().post('/questions', json={'searchTerm':'the'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
    
    def test_get_questions_search_without_results(self):
        res = self.client().post('/questions', json={'searchTerm':'dina'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')      

    """
    TODO
    Test get questions based on catagory success and fail case 
    """
    def test_get_questions_by_category(self):    
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'],1)
        
    def test_404_not_found_questions_by_category(self):    
        res = self.client().get('/categories/30/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')  
    
    """
    TODO
    Test get question for quiz success and fail case 
    """
    def test_get_question_for_quiz(self):
        res =  self.client().post('/quizzes', json=self.quiz)
        data = json.loads(res.data)
         
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
    
    def test_422_get_question_for_quiz_for_none_category_given(self):
        res =  self.client().post('/quizzes', json=self.quiz_2)
        data = json.loads(res.data)
                
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'unprocessable')
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()