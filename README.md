# Introducting 

![Frame 4949 (3)](https://user-images.githubusercontent.com/81405395/232273519-8e067f93-769d-4905-a9aa-0a296c9a5d6d.png)

# Current Prototype 

https://user-images.githubusercontent.com/81405395/232275130-83047466-5c77-4f4e-a38a-bd9c56c7c29a.mp4

# Hustle - A To-Do List Web Application

Hustle is a web application designed to help you manage your to-do list and get things done efficiently. With an intuitive and user-friendly interface, Hustle allows you to easily add, update, and delete tasks, as well as track their due dates, priorities, and completion status. Built with Python and Flask, and utilizing a SQL database, Hustle is a reliable and versatile tool to keep you on top of your tasks and goals.


## Technologies Used
Hustle is built with the following technologies:

* Python 3.9.7
* Flask 2.0.2
* SQLite 3.36.0
* HTML 5
* CSS 3
* JavaScript
* jQuery 3.6.0
* Bootstrap 5.1.0
* Font Awesome 5.15.4

## Features
Hustle includes the following features:

* Add new tasks with a title, description, due date, priority, and completion status.
* Update existing tasks to mark them as complete or change their details.
* Delete tasks that are no longer needed.
* Sort tasks by title, due date, priority, or completion status.
* Filter tasks by due date, priority, or completion status.

Upcoming features 
* Use a status slider to indicate the progress of each task.
* Synchronize your tasks with your calendar and never miss an important event again.
* Receive notifications and reminders for upcoming tasks and events.
* Customize multiple To do groups
* Mobile app


## Installation
To install and run Hustle on your local machine, follow these steps:

1. Clone the Hustle repository from GitHub:
```git clone https://github.com/your-username/hustle.git```

2. Change into the Hustle directory:
```cd hustle```

3. Create a virtual environment for Hustle:
```python3 -m venv venv```

4. Activate the virtual environment:
```source venv/bin/activate```

5. Install the required Python packages:
```pip install -r requirements.txt```

6. Initialize the database:
```python3
from app import db
db.create_all()
quit()```

7. Start the Flask server:
```flask run```

8. Open Hustle in your web browser by navigating to http://localhost:5000/

## License
Hustle is licensed under the MIT License. See LICENSE for more information.

