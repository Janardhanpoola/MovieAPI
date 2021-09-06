from django.test import TestCase

from rest_framework.test import APITestCase

from django.urls import reverse

from .models import Movie
# Create your tests here.

class MovieAPITestCase(APITestCase):

    url="/movieapi/"
    #url=reverse('movieapi')
      


    def setUp(self):
        Movie.objects.create(

                            name="Parasite",
                            genre="Drama",
                            release_year=2012,
                            language="English")
       
        Movie.objects.create(        
                                                
                            name="Troy Brown",
                            genre="Drama",
                            release_year=1991,
                            language="English")
       
        Movie.objects.create(
                            
                            name="Allison Carney",
                            genre="Sci-fi",
                            release_year=1978,
                            language="Spanish")



    def test_get_method_success(self): #checks if the it is able to get the data from the server which returns 200 status
        
        response=self.client.get(self.url)
        #print(response.data)
        self.assertEqual(response.status_code,200)

        
    

    def test_get_method_success_for_a_particular_movie(self): #checks if the it is able to get the data from the server which returns 200 status
        #url=reverse('movieidapi',args=[1])  
        response=self.client.get(self.url+"2/") #checking for 15th record which actually exists in db
        #print(response.data)
        self.assertEqual(response.status_code,200)
            

    def test_get_method_fail(self):#if we try to get a movie which doesnt exists it returns status 404
        
        response=self.client.get(self.url+"15/") #url for a movie which doesnt exists in the db.
        
        #print(response.data)

        self.assertEqual(response.status_code,404)


    def test_post_method_success(self): #if data is posted it returns 201 status code
        new_movie={
                    "name": "Shawshank Redemption",
                    "genre": "Drama",
                    "release_year": 1974,
                    "language": "English"
                }
        
        response=self.client.post(self.url,new_movie,format='json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['genre'],'Drama')


    def test_post_method_fail(self): #if data is posted it returns 400 status code since we are only posting the data of few attributes
        new_movie={
                    "name": "Shawshank Redemption",
                    "genre": "Drama",
                    "release_year": 1974,
                }
        
        response=self.client.post(self.url,new_movie,format='json')
        self.assertEqual(response.status_code,400)
        


    def test_delete_method_success(self): #returns status code 204
        #url="/movieapi/255/"
        response=self.client.delete(self.url+"1/")
        self.assertEqual(response.status_code,204)

    


    
    def test_wrong_movie_genre(self):
        
        response=self.client.get(self.url+"2/") #Testing the movie genre if submitted wrongly
        #print(response.data)
        self.assertNotEqual(response.data['genre'],'Comedy') 

    
    def test_total_records(self):
        movies=Movie.objects.all() #testing the total records in db
        self.assertEqual(movies.count(),3)






