import requests
import sys
class Test:
    api_data = 'b1c41fdf'
    link = 'http://www.omdbapi.com'
    def __init__(self, movie):
       # self.link = 'http://www.omdbapi.com'
        self.title = movie
       #self.api_data = 'b1c41fdf'
        self.data = {}

    def validation(self):
        self.payload = {'t': self.title, 'r': 'json', 'apikey': Test.api_data}
        try:
            self.data = requests.get(Test.link, params=self.payload).json()
            print (self.data['Error'])
        except ValueError:
            print (
                'Exception caught, check your URL')
        except KeyError:
            pass
        return self.data
    def type(self):
        self.movie_data = self.validation()
        try:
            list_of_movies = self.movie_data["Ratings"]
            print ('Movie Name is ==>'+str(sys.argv[1:]))
            test = list(filter(lambda movie: movie['Source'] == 'Rotten Tomatoes', list_of_movies))
            if test:
                print ("Rotten Tomatoes Ratings -->" + [value['Value'] for value in test][0])
            else:
                print ("Rotten Tomatoes Ratings not present, Displaying others rating \n")
                print ([value['Source'] for value in list_of_movies][0], [value['Value'] for value in list_of_movies][0])
        except KeyError:
            pass
        except IndexError:
            print ("Ratings not avialable")
if len(sys.argv) == 1:
    raise Exception('Please provide movie name as an argument')
else:
    define = Test(sys.argv[1:])
    define.type()
