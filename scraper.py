from piazza_api import Piazza
import login_info
import pandas
from datetime import datetime

p = Piazza()

p.user_login(login_info.email, login_info.password)
user_profile = p.get_user_profile()

course = p.network(login_info.piazza_course)
posts = course.iter_all_posts(limit=None, sleep = 1)

data = {}

for post in posts:
    post_history = post["history"][0]

    content = post_history["content"] # content of post
    title = post_history["subject"] # title of post
    number = post['nr'] # post number
    date = post["created"]
    views = post["unique_views"]
    folders = post["folders"]

    # store the data into a dictionary
    data[number] = [title, content, date, views, folders]

df = pandas.DataFrame.from_dict(data)
df = df.transpose()

time = datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = "piazzaData_" + time + '.csv'

df.to_csv(filename, encoding = 'utf-8', index = False)