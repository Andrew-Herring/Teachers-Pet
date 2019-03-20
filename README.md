# Welcome to Teachers' Pet by Andrew Herring
----
## What is Teachers Pet?

> Teachers' Pet is built in Python and Django and is used to organize and manage EFL and ESL teachers' students and courses. A user will log in and create an account as a Teacher then begin to add their courses.  After entering all of their courses a teacher can then add students to that course.  Students will have CEFR values assigned to them as well as three specific skills, readong, speaking and vocabulary.  A teacher can adjust these values as they see fit based on a students preformance in class.  This allows a teacher to have a better idea of what students need help in more specific areas, making lesson planning much easier and more focused around a students needs. Teachers' Pet can store history for multiple users and is fully CRUD capable. Data stored in SQLite 3 database.

----

<!-- ![PonyUpScreenshot1](/src/images/2.png)

![PonyUpScreenshot2](/src/images/1.png) -->

## What technologies went into the application?

>  Python | Django | SQLite 3 | Bootstrap

## Entity Relationship Diagram
![Teachers Pet ERD](/website/static/website/images/teachersPetERD.png "Teachers' Pet ERD")

# Installing Core Technologies

## 1. SQLite

### For OSX Users

```
brew install sqlite
```

### For Windows Users

Visit the [SQLite downloads](https://www.sqlite.org/download.html) and download the 64-bit DLL (x64) for SQLite version, unzip and install it.

## 2. SQL Browser

The [DB browser for SQLite](http://sqlitebrowser.org/) will let you view, query and manage your databases for this project.

## 3. Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/download) is Microsoft's cross-platform editor that you can use to view Python and Django code.

# Setting up environment and installing dependencies

## 1. Set up your virtual environment

Within the terminal, navigate to the location where you'd like to create the new environment and Teachers' Pet project. Create a folder called TeachersPet and navigate within the new folder. Then, enter this text to create the new environment:
```
virtualenv ENV
```
Then activate your environment:
```
source ENV/bin/activate
```
Note that you can type "deactivate" to end the new environment at any time.

## 2. Install Django

Within your new TeachersPet folder, download the Django code by typing:
```
pip install django
```

## 3. Download the Teachers' Pet project

Within your new TeachersPet project folder, download the source code by typing:
```
git clone git@github.com:Andrew-Herring/Teachers-Pet.git
```

## 4. Starting the project server

After downloading the Teachers' Pet project, you should have a new folder within the Teachers' Pet Project folder that you created. The new folder will also be called TeachersPet.  Navigate within this folder.  Start the server by typing:
```
python manage.py runserver
```

## 5. Navigate to the Teachers' Pet webpage

Within your web browser, navigate to http://localhost:8000/

From here, you should see the main links for the Teachers' Pet application.


# Creating the Teachers' Pet DB

While inside the TeachersPet/TeachersPet folder, enter this command:
```
python manage.py makemigrations website
```
Then enter
```
python manage.py migrate
```
You now have a database named sqlite3.sql within your existing folder.  Use the DB Browser for SQLite to open the new database if desired.

