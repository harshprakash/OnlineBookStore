# OnlineBookStore
This is the fullstack devlopment  of BookStore web-app using django.

To run this web-app, execute the following steps :
1. clone the repo or run  ``https://github.com/harshprakash/OnlineBookStore.git``
3. install mySqlConnector  '' pip install mysqlclient ''
2. install mysql (or click the [link](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) for installation help).
3. ## create a database and run the following:
~~~~sql
CREATE USER 'sql_username'@'localhost' IDENTIFIED BY 'password';.
GRANT ALL PRIVILEGES ON *test* TO 'sql_username'@'localhost' WITH GRANT OPTION;.
FLUSH PRIVILEGES;
~~~~
4. ## now go to my.cnf file and add following.
```
# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

 ## for run.
```
5. run cd BookStore.
6  run  python manage.py migrate
7. run python manage.py runserver.
```

## Contribution
Both have equal contribution to the project.

Dhiraj Kumar Sah: Sytem Design, SRS Prepration,Data Flow Diagram,  Database Design and Creation, E-R diagram,  Backend Admin Login Creation, Product Listing implementation, Search Funtionality,  Bootstrap, Black Box testing and report, readme.

Harsh Prakash:  Usecase, Tech Stack Selection, User Registration, User Login, Home page with Product,  Cart Funtionality, Add to cart, Remove from cart, Payment Integration, Order tracking and Cancelation, Unit testing, readme.