#Get instagram profile pictures and posts
#install instaloader,Pillow
# import required modules
import instaloader
from PIL import Image, ImageTk
import os
# Create instance
loader = instaloader.Instaloader()
# get username 
user = input("Enter Username: ")
# download profie
loader.download_profile(user, profile_pic_only = True)
# get list of image from folder
img = [x for x in os.listdir(f'{os.getcwd()}/{user}') if x.endswith('jpg')]
# read image from list
img = Image.open(f'{os.getcwd()}/{user}/{img[0]}')
# Display image
img.show()

#Get instagram user details
#install instagramy
from instagramy import InstagramUser
# user input
name = input("Enter user name:")
# instance of instagram user
user = InstagramUser(name)
# total followers
followers = user.number_of_followers
print('Total followers:', followers)
# total followings
following = user.number_of_followings
print('Total followings:',following)
# total number of posts
posts = user.number_of_posts
print('Total posts:',posts)
#bio description
bio = user.biography
print('Bio:\n',bio)
#link in bio
link_in_bio = user.website
print("Link in Bio:",link_in_bio)

#Download youtube videos
import webbrowser
url = input("Enter youtube url to download")
download = url[:12] + "ss" + url[12:]
webbrowser.open(download)
