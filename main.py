from flask import Flask
import random
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    tomorrow_movie = get_random_movie()
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow_movie + "</li>"
    content += "</ul>"
    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ["Best in Show", "Mystic Pizza", "Truman Show", "The Natural", "Hello, Dolly"]
    
    # TODO: randomly choose one of the movies, and return it
    x=0
    for title in movie_list:
        x += 1
    
    dice=random.randrange(0,x)
    return(movie_list[dice])

app.run()
