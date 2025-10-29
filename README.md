#CS50 Web Programming with Python and Javascript
## Capstone Project Chat App (Real-Time Messaging App)

### Overview
**Chat** is a real-time web-based chat application that can create user then allows to create group chats, send messages and exchange messages instantly using Django Channels and Websockets.

## Distinctiveness and Complexity

###Distinctiveness
This project is distinct from prior CS50 projects because :
- It implements real-time asynchronous communication using Django Channels and Websockets.
- it allows users to chat live without refreshing the page.
- It utilizes javascript to handle dynamic DOM updates based on incoming data  from the server.
-This app does rely on solely on page reloads or form submission.
- Unlike earlier projects, this app uses asynchronous event-driven architecture instead of synchronous views.

### Complexity 
 This project demonstrates siginificant technical and architectural complexity, including:
- Asynchronous Django Consumer classes (AsyncwebsocketConsumer) to handle messages and events.
- A routing system for Websockets distinct from standard django HTTP routing.
- Database models for persisting user accounts, chat rooms, and message history.
- Frontend rendering logic that updates the chat UI in real-time without a page reload.


## File Contents

/Capstone/
- init.py
- asgi.py ASGI entry point (required for WebSockets)
- settings.py Project settings
- urls.py Root URL configuration
- wsgi.py
- chat/ Main Django app
- static/chat/
- style.css Custom styling
- chat.js JavaScript for WebSocket message handling
- templates/chat/
- layout.html Base layout for all pages
- index.html Homepage (list of rooms, private chats)
- room.html Individual chat room interface
- private.html Private messaging UI

- init.py
- admin.py Registers chat models in Django admin
- apps.py
- consumers.py WebSocket Consumers (handles real-time messages)
- forms.py Django forms 
- models.py Chat models (User, Room, Message)
- routing.py WebSocket URL routing configuration
- urls.py Standard Django URLs
- views.py Renders templates and handles HTTP requests
- chatconnect/ Django project configuration folder

- db.sqlite3 SQLite database for local development
- manage.py Django management utility
- requirements.txt Dependencies list
- README.md Project documentation (this file)


## How to Run this Application
- Clone the repository to your local machine and navigate into the project directory
- Create a virtual environment using python -m venv venv and activate it (source venv/bin/activate on macOS/Linux or             
venv\Scripts\activate on Windows).
- Install dependencies listed in the requirements.txt file by running pip install -r requirements.txt.
- Apply database migrations using python manage.py makemigrations followed by python manage.py migrate.
- Start the development server by running python manage.py runserver.
- Open your browser and go to http://127.0.0.1:8000/ to access the app.
- Register or log in, join or create chat rooms, and start chatting in real time.
