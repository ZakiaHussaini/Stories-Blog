import os
os.environ['DATABASE_URL'] = 'postgres://ljjlxzwg:WJmzHLUsTNxF_ZZ4gCZ9AXJUene7jBNW@trumpet.db.elephantsql.com/ljjlxzwg'
os.environ['DEBUG'] = '1'
os.environ['CLOUDINARY_URL'] = 'cloudinary://619146312833525:w8-CWIKW3AunltlqYqybGIcuBow@dd5s8l3yh'
os.environ['DEV'] = '1'
os.environ['ALLOWED_HOST'] = 'story-blog-24bc3af065de.herokuapp.com'
os.environ['CLIENT_ORIGIN'] = 'https://story-blog-24bc3af065de.herokuapp.com'
os.environ.setdefault("SECRET_KEY", "StoryBlogAdmin")