from django.test import TestCase

from .models import Profile, Projects, Rates


class ProfileTestClass(TestCase):
    def setUp(self):
        self.george = Profile(profile_photo='default.jpg', bio='A fullstack web developer.',
                                website='http://www.george.com', contact='g@mail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.george,Profile))
    
    def test_save_method(self):
        self.george.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        
    def test_get_profile_projects(self):
        projects = Projects.get_profile_projects()
        self.assertTrue(len(projects)>0)    



class RatesTestClass(TestCase):
    def setUp(self):
        self.user = User(username='Kilewa',email='museegeorge@yahoo.com',password='kayolee1')
        
        self.rate = Rates(design=10,usability=10,content=10,user=self.user,project=10)
        self.rate.save()
        
        self.assertTrue(isinstance(self.rate,Rate))        
