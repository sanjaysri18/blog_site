# from fastapi import FastAPI, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# import mysql.connector



# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # Database connection configuration
# db_config = {
#     "host": "localhost",
#     "user": "ss",
#     "password": "Sanjay@123",
#     "database": "blog",
# }

# @app.get("/")
# def home():
#     return {"message": "Welcome to the signup page!"}

# @app.get("/signup", response_class=HTMLResponse)
# def signup(request: Request):
#     return templates.TemplateResponse("signup.html", {"request": request})

# @app.post("/signup", response_class=HTMLResponse)
# def signup_post(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
#     connection = mysql.connector.connect(**db_config)

#     try:
#         cursor = connection.cursor()
#         insert_query = "INSERT INTO iam_user (name, password, email) VALUES (%s, %s, %s)"
#         cursor.execute(insert_query, (username,password, email))
#         connection.commit()

#         message = "Signup successful"
#     except mysql.connector.Error as error:
#         message = f"Error occurred: {error}"
#     finally:
#         cursor.close()
#         connection.close()

#     return templates.TemplateResponse("login.html", {"request": request, "message": message})

# @app.get("/login", response_class=HTMLResponse)
# def login(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request, "message": ""})

# @app.post("/login", response_class=HTMLResponse)
# def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
#     connection = mysql.connector.connect(**db_config)

#     try:
#         cursor = connection.cursor()
#         select_query = "SELECT * FROM iam_user WHERE name = %s"
#         cursor.execute(select_query, (username,))
#         user = cursor.fetchone()

#         if user and user[2] == password:
#             message = "Login successful"
#             return templates.TemplateResponse("create_blog.html", {"request": request, "message": message})
#         else:
#             message = "Invalid username or password"
#     except mysql.connector.Error as error:
#         message = f"Error occurred: {error}"
#     finally:
#         cursor.close()
#         connection.close()

#     return templates.TemplateResponse("login.html", {"request": request, "message": message})


# posts = []
 

# @app.get("/create-blog", response_class=HTMLResponse)
# def create_blog(request: Request):
    
#     return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})

# @app.post("/create-post", response_class=HTMLResponse)
# def create_post(request: Request, title: str = Form(...), content: str = Form(...), tags: str = Form(...)):
#     # Create a new post dictionary
        
#     post = {
#         "title": title,
#         "content": content,
#         "tags": tags
#     }

#     # Add the post to the list
#     posts.append(post)
   

#     return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})

# @app.get("/edit-post/{post_index}", response_class=HTMLResponse)
# def edit_post(request: Request, post_index: int):
#     # Check if the post index is valid
#     if post_index >= 0 and post_index < len(posts):
#         return templates.TemplateResponse("create_blog.html", {"request": request, "post_index": post_index, "post": posts[post_index]})
#     else:
#         return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})

# @app.post("/update-post/{post_index}", response_class=HTMLResponse)
# def update_post(request: Request, post_index: int, title: str = Form(...), content: str = Form(...), tags: str = Form(...)):
#     # Check if the post index is valid
#     if post_index >= 0 and post_index < len(posts):
#         # Update the post with the new data
#         posts[post_index]["title"] = title
#         posts[post_index]["content"] = content
#         posts[post_index]["tags"] = tags

#     return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})

# @app.get("/delete-post/{post_index}", response_class=HTMLResponse)
# def delete_post(request: Request, post_index: int):
#     #  Check if the post index is valid
#      if post_index >= 0 and post_index < len(posts):
#         # Delete the post from the list
#          del posts[post_index]

#      return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})



# def logout():
#     # Perform logout logic here
#     # For example, you can clear the session or delete the user's authentication token
#     # You can also redirect the user to a login page or return a success message
    
#     # Example: Clear session
#     return {"message": "Logged out successfully"}


# /



from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
import mysql.connector
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "ss",
    "password": "Sanjay@123",
    "database": "blog",
}
message=""
# Define the Post model
class Post(BaseModel):
    title: str
    content: str
    tags: str

@app.get("/")
def home():
    return {"message": "Welcome to the signup page!"}

@app.get("/signup", response_class=HTMLResponse)
def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup", response_class=HTMLResponse)
def signup_post(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO iam_user (name, password, email) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (username, password, email))
        connection.commit()

        message = "Signup successful"
    except mysql.connector.Error as error:
        message = f"Error occurred: {error}"
    finally:
        cursor.close()
        connection.close()

    return templates.TemplateResponse("login.html", {"request": request, "message": message})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "message": ""})

@app.post("/login", response_class=HTMLResponse)
def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM iam_user WHERE name = %s"
        cursor.execute(select_query, (username,))
        user = cursor.fetchone()

        if user and user[2] == password:
            message = "Login successful"
            return templates.TemplateResponse("create_blog.html", {"request": request, "message": message})
        else:
            message = "Invalid username or password"
    except mysql.connector.Error as error:
        message = f"Error occurred: {error}"
    finally:
        cursor.close()
        connection.close()

    return templates.TemplateResponse("login.html", {"request": request, "message": message})


@app.get("/create-blog", response_class=HTMLResponse)
def create_blog(request: Request):
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM post"
        cursor.execute(select_query)
        posts = cursor.fetchall()
    except mysql.connector.Error as error:
        post = post[1]


        # message = f"Error occurred: {error}"
        
    finally:
        cursor.close()
        connection.close()

    return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})


@app.post("/create-post", response_class=HTMLResponse)
def create_post(request: Request, title: str = Form(...), content: str = Form(...), tags: str = Form(...)):
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM post"
        cursor.execute(select_query)
        posts = cursor.fetchall()
    except mysql.connector.Error as error:
        post = post[1]
        # message = f"Error occurred: {error}"
        
    finally:
        pass


    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO post (title, content, tags) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (title, content, tags))
        connection.commit()

    except mysql.connector.Error as error:
        message = f"Error occurred: {error}"
    finally:
        cursor.close()
        connection.close()

    return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})
   


def logout():
    # Perform logout logic here
    # For example, you can clear the session or delete the user's authentication token
    # You can also redirect the user to a login page or return a success message

    # Example: Clear session
    return {"message": "Logged out successfully"}



@app.get("/delete-post/{post_index}", response_class=HTMLResponse)
def delete_post(request: Request, post_index: int):
    connection = mysql.connector.connect(**db_config)
    try:
        cursor = connection.cursor()
        insert_query = "delete from post where id=%s"
        cursor.execute(insert_query, (post_index,))
        connection.commit()

    except mysql.connector.Error as error:
        message = f"Error occurred: {error}"
    
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM post"
        cursor.execute(select_query)
        posts = cursor.fetchall()
    except mysql.connector.Error as error:
        post = post[1]
        # message = f"Error occurred: {error}"
        
    finally:
        pass

    return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})



@app.get("/edit/{post_index}", response_class=HTMLResponse)
def edit(request: Request,post_index: int):
    return templates.TemplateResponse("update.html", {"request": request, "post_index": post_index,"message": ""})


@app.post("/edit-post/{post_index}")
def edit_post(request: Request,post_index: int,title: str = Form(...), content: str = Form(...), tags: str = Form(...)) :
    connection = mysql.connector.connect(**db_config)

    try:
        cursor = connection.cursor()
        select_query = "UPDATE post set title=%s, content=%s,tags=%s where id=%s"
        cursor.execute(select_query,(title, content, tags,post_index))
        connection.commit()
        cursor.execute("select * from post")
        posts = cursor.fetchall()
        

    except mysql.connector.Error as error:
        post = post[1]
        # message = f"Error occurred: {error}"
        
    finally:
        connection.close()
    return templates.TemplateResponse("create_blog.html", {"request": request, "posts": posts})


def fetch_user_id():
    connection = mysql.connector.connect(**db_config)
    user_id = cursor.fetchone()

    try:
        cursor = connection.cursor()
        query = "SELECT id FROM iam_user"
        cursor.execute(query)
        user_id = cursor.fetchone()

    except mysql.connector.Error as error:
        message = f"Error occurred: {error}"
    finally:
        cursor.close()
        connection.close()
    print(f"this is the user_id----------------__> {user_id}")
    return user_id