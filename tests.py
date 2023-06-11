import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db
from models import Cupcake

class CupcakeViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.create_all()
            cupcake = Cupcake(
                flavor='chocolate',
                size='medium',
                rating=4.5,
                image='chocolate_cupcake.jpg'
            )
            db.session.add(cupcake)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_list_cupcakes(self):
        with app.app_context():
            response = self.client.get('/api/cupcakes')
            data = response.json

            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(data, list)
            self.assertEqual(len(data), 1)

    def test_get_cupcake(self):
        with app.app_context():
            cupcake = Cupcake.query.first()
            response = self.client.get(f'/api/cupcakes/{cupcake.id}')
            data = response.json

            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(data, dict)
            self.assertEqual(data['flavor'], 'chocolate')
            self.assertEqual(data['size'], 'medium')
            self.assertEqual(data['rating'], 4.5)
            self.assertEqual(data['image'], 'chocolate_cupcake.jpg')

    def test_create_cupcake(self):
        with app.app_context():
            cupcake_data = {
                'flavor': 'vanilla',
                'size': 'small',
                'rating': 4.0,
                'image': 'vanilla_cupcake.jpg'
            }
            response = self.client.post('/api/cupcakes', json=cupcake_data)
            data = response.json

            self.assertEqual(response.status_code, 201)
            self.assertIsInstance(data, dict)
            self.assertEqual(data['flavor'], 'vanilla')
            self.assertEqual(data['size'], 'small')
            self.assertEqual(data['rating'], 4.0)
            self.assertEqual(data['image'], 'vanilla_cupcake.jpg')
            self.assertEqual(Cupcake.query.count(), 2)


if __name__ == '__main__':
    unittest.main()
