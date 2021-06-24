# pizza
This is a project made with django framework.
Has 2 api endpoints one for admin one for user.
Only superusers can use admin endpoint while users can be created from register page.
Once logged in user as well as admin can create pizza,edit existing pizza or can delete the existing pizza.
All the information about created pizzas will be stored in the database.
The database manager which is used in this project is mongodb.
User can see all the stored pizza once logged in.
User can filter pizzas according to the requirements.
If user enters any wrong input the he will get warning messages.
Unless user is logged in user cannot see,edit or delete existing pizzas.

steps to pull from github
1. download zip file from url.
2. extract to specific location.

steps to run :
install all the packages mentioned in requiredments.txt file using cmd command pip install (followed by package name).
1. install python in your pc.
2. install mongodb compass.
3. open mongodb compass.
4. click connect.
5. create database named pzdata (if you create database with other name then make respective change in settings.py file database section)
6. create collection named pzcollection.
7. open cmd navigate to project directory.
8. run command "python manage.py check" (check if there are any issues)
9. then run command "python manage.py makemigrations"
10. run command "python manage.py migrate"
11. then run the server by running command "python manage.py runserver".
12. open the provided url
13. u will reach required webpage.
14. u can create user by clicking register.
15. then u can login using user login if you are user or a superuser.
16. Only superusers can login using admin login.
17. once logged in you can create/edit/delete pizzas.
18. to see existing pizza u have to login using user login.
19. admin can create edit and delete pizzas from admin prompt.
20. The list of already existing pizza can be filtered by type and size of pizza.
21. one can add multiple toppings on a pizza.


steps to create superuser

1.in cmd run command "python manage.py createsuperuser"

2.enter username

3.enter email(optional)

4.Enter password

You can log into admin panel once server is up and running by the url   http://localhost/8000/admin
