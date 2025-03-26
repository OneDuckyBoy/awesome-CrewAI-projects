from marketing_posts_crew.crew import MarketingPostsCrew


def run():
   
    print("## Welcome to the Marketing posts Crew")
    print('-------------------------------')

    # you need to replace 'marketing_information.md' with one for your company/profile
    inputs = { }
    posts= MarketingPostsCrew().crew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## The posts are the done : D")
    print("########################\n")
    with open(f"results/posts.md", "w") as file:
        file.write(posts.raw)
   



