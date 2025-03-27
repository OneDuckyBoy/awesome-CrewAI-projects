import sys
from movie_recommendation_crew.crew import MovieRecommendationCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Movie Recommendation Crew")
    print('-------------------------------')

    preference = "My favourite movies are in the sci fi genre, and or other genres. I like the Show Lucifer - i watched it on Netflix 2 times the whole show! " \
    "What I liked about the show is that it used she supernatural ascpect of the show as a plot device to explore the human psyche and emotions and the whole " \
    "premise of the show was amazing in my opinion. I also like House M.D. and like it for the characters - I like that they grow and become more fleshed out " \
    "with time. I think that House is a little on the nose(a little too much in some specific scenes), but overall he is good character - I am currently on the second " \
    "season, but I think that I will finish it. Other show is Suits. The character development and the premise of the law as a driving instrument was super. I didn't like " \
    "Dexter : ( it was too much violence and it wasn't a show that i liked"
    inputs = {
        "preference":preference,
        
    }
    results= MovieRecommendationCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The recommendations are in the result folder")
    print("########################\n")
 


