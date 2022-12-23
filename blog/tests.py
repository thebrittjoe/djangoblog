from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

# Create your tests here.
class post_testcase(TestCase):
    def setUp(self):
        User.objects.create(username='test', password='Test123!', is_active=True, 
                            email='test@testcase.com')
        user = User.objects.get(username='test')
        Post.objects.create(title='Test Case Post', author=user, body='The test should run', 
                            status='PB', tags='test, post')
    def test_published_post(self):
        post = Post.objects.get(title='Test Case Post')
        # check the data saved correctly
        self.assertEqual(post.body, 'The test should run')