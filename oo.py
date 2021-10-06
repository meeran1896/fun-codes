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