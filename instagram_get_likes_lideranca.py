import instaloader
import json
from datetime import datetime

L = instaloader.Instaloader()

USER = "lidod10344"
PROFILE = "juniororosco.sp"

# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

likes = set()
print("Fetching likes of all posts of profile {}.".format(profile.username))

i=0
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")
file_name = "post-info-" + dt_string + ".csv"

with open(file_name, 'w') as f:
    for post in profile.get_posts():
        likes = likes | set(post.get_likes())
        for like_each in post.get_likes():
            print(dt_string,post.likes, post.owner_username, post.shortcode, post.date, like_each.username, like_each.full_name, sep=';')
            print(dt_string,post.likes, post.owner_username, post.shortcode, post.date, like_each.username, file=f, sep=';')

print("end")

"""
with open("post-info.txt", 'w') as f:
    for post in profile.get_posts():
        i=i+1
        if i==3:
            break
        else:
            likes = likes | set(post.get_likes())
            for like_each in post.get_likes():
                #print(post.likes, post.owner_username, post.shortcode, post.date, like_each.username, like_each.full_name, sep=';')
                print(post.likes, post.owner_username, post.shortcode, post.date, like_each.username, file=f, sep=';')

print("end")

print("Fetching followers of profile {}.".format(profile.username))
followers = set(profile.get_followers())

ghosts = followers - likes

print("Storing ghosts into file.")
with open("inactive-users.txt", 'w') as f:
    for ghost in ghosts:
        print(ghost.username, file=f)
"""


"""

CODE STREAMLIT to SELENIUM

requirements.txt

selenium==4.4.3
webdriver-manager==3.8.3


"""

"""
INSTALOADER to STREAMLIT

instaloader==4.9.3

"""