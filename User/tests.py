from django.test import TestCase 
from django.contrib.auth.models import User
from django.urls import reverse

# testing for login funnctionality and admin pannel
class CustomUserTests(TestCase):

    def test_create_user(self):
        #User = get_user_model()
        user = User.objects.create_user(
            username="dhiraj",
            email="dhiraj123@gmail.com",
            password="dhiraj123"
        )
        self.assertEqual(user.username, "dhiraj")
        self.assertEqual(user.email, "dhiraj123@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
       # User = get_user_model()
        user = User.objects.create_superuser(
            username="harsh",
            email="harsh123@gmail.com",
            password="harsh123"
        )
        self.assertEqual(user.username, "harsh")
        self.assertEqual(user.email, "harsh123@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupTests(TestCase):
    
    
    username = 'newuser'
    email = 'newuser@email.com'
    
    
    def setUp(self):
        url = reverse('Login')
        self.response = self.client.get(url)
        
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'User/login.html')
        self.assertContains(self.response, 'login')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
        
    def test_signup_form(self): 
        new_user = User.objects.create_user(self.username, self.email)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.email)
