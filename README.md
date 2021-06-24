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


steps to run :

1.pull the projest to local machine.
2.open cmd
3.Navigate to the project directory.
4.run command python manage.py runserver
5.open url provided by the cmd.

steps to create superuser

1.in cmd run command "python manage.py createsuperuser"
2.enter username
3.enter email(optional)
4.Enter password

You can log into admin panel once server is up and running by the url   http://localhost/8000/admin
