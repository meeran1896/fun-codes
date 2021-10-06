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
