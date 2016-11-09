import os
from traveler import web_app
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, web_app.application.config['DATABASE'] = tempfile.mkstemp()
        self.app = web_app.application.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(web_app.application.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        self.assertIn('Hello Traveler!', str(rv.data))

if __name__ == '__main__':
    unittest.main()
