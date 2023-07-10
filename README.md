<div align="center">
<h1>Django todo app</h1>
<em>a small django prject</em>
</div>


## Functionality
+ user signin, signup, signout
+ create / update / delete tasks
+ search task
+ info / warn / error messages


## Requirements
+ python (used 3.11.0)
+ django (used 4.2.2)
+ git (optional)


## How to Run
Must have above requirements satisfied.
1. Download the zip and extract it OR clone (requires git) this repository.
2. In terminal, go to the directory where manage.py file is located.
3. Run following command (create database and tables)
```
python manage.py migrate
```
4. Run the project using the command
```
python manage.py runserver
```
5. Open browser and type `localhost:8000/todo/` in url.
6. Use `ctrl+c` in terminal to stop the project.


## Quick View of project

<div align="center">
    <p>Index page</p>
    <img src="./demo/index.png" alt="index page">
</div>
<br>
<div align="center">
    <p>Signup page</p>
    <img src="./demo/signup.png" alt="signup page">
</div>
<br>
<div align="center">
    <p>Signin page</p>
    <img src="./demo/signin.png" alt="signin page">
</div>
<br>
<div align="center">
    <p>Tasks page</p>
    <img src="./demo/tasks.png" alt="tasks page">
</div>
<br>
<div align="center">
    <p>Task create page</p>
    <img src="./demo/create.png" alt="task create page">
</div>
<br>
<div align="center">
    <p>Task update page</p>
    <img src="./demo/update.png" alt="task update page">
</div>
<br>
<div align="center">
    <p>Task delete page</p>
    <img src="./demo/delete.png" alt="task delete page">
</div>
<br>
<div align="center">
    <p>Task search</p>
    <img src="./demo/search.png" alt="task search page">
</div>
<br>
<div align="center">
    <p>Message popup</p>
    <img src="./demo/message.png" alt="message popup">
</div>

