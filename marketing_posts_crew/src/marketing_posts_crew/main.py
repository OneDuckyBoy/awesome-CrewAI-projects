from marketing_posts_crew.crew import MarketingPostsCrew
from datetime import datetime
import requests # type: ignore


def run():
    current_datetime = datetime.now()
    print("## Welcome to the Marketing posts Crew")
    print('-------------------------------')

    # you need to replace 'marketing_information.md' with one for your company/profile
    inputs = { }
    posts= MarketingPostsCrew(current_datetime).crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The posts are the done : D")
    print("########################\n")
    with open(f"results/posts.md", "w", encoding="utf-8") as file:
        file.write(posts.raw)
    

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")

    with open("posts/Instagram/Instagram post picture "+formatted_datetime+".txt", 'r') as file:
        image_url = file.read().strip()
    response = requests.get(image_url)
    if response.status_code == 200:
        # Open a file in write-binary mode to save the image
        with open("posts/Instagram/Instagram post picture "+formatted_datetime+".png", 'wb') as image_file:
            image_file.write(response.content)
        print("Image downloaded and saved as "+"posts/Instagram/Instagram post picture "+formatted_datetime+".png"+".")
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")
    



    with open("posts/Facebook/Facebook post picture "+formatted_datetime+".txt", 'r') as file:
        image_url = file.read().strip()
    response = requests.get(image_url)
    if response.status_code == 200:
        # Open a file in write-binary mode to save the image
        with open("posts/Facebook/Facebook post picture "+formatted_datetime+".png", 'wb') as image_file:
            image_file.write(response.content)
        print("Image downloaded and saved as "+"posts/Facebook/Facebook post picture "+formatted_datetime+".png"+".")
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")
    



    with open("posts/Threads/Threads post picture "+formatted_datetime+".txt", 'r') as file:
        image_url = file.read().strip()
    response = requests.get(image_url)
    if response.status_code == 200:
        # Open a file in write-binary mode to save the image
        with open("posts/Threads/Threads post picture "+formatted_datetime+".png", 'wb') as image_file:
            image_file.write(response.content)
        print("Image downloaded and saved as "+"posts/Threads/Threads post picture "+formatted_datetime+".png"+".")
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")
    



    with open("posts/X.com/X.com post picture "+formatted_datetime+".txt", 'r') as file:
        image_url = file.read().strip()
    response = requests.get(image_url)
    if response.status_code == 200:
        # Open a file in write-binary mode to save the image
        with open("posts/X.com/X.com post picture "+formatted_datetime+".png", 'wb') as image_file:
            image_file.write(response.content)
        print("Image downloaded and saved as "+"posts/X.com/X.com post picture "+formatted_datetime+".png"+".")
    else:
        print(f"Failed to retrieve the image. HTTP Status code: {response.status_code}")
   



