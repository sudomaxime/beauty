# What does this shell script do ?

This solutions allows you to grab env variables from your docker-compose.yml to create your base users to administrate other users or to create new databases and use Mongo in a secure way.

This shell script will create on the fly all the users you need to safely administrate your database.

## ROOT admin variables 
These are your regular docker mongo variables used to set the auth mode, you can (read more here)[https://hub.docker.com/_/mongo].
```
MONGO_INITDB_ROOT_USERNAME=<your_ROOT_database_admin_name>
MONGO_INITDB_ROOT_PASSWORD=<your_ROOT_database_password>
```

## Superadmin variables
This admin level is used to create more users and assign them to databases. You should never use your ROOT admin to create your users.
```
* MONGO_DATABASE_ADMIN_NAME=<your_db_SUPERADMIN_user>
* MONGO_DATABASE_ADMIN_PASSWORD=<your_db_SUPERADMIN_password>
```

## Application specific variables
This admin level is intended to manage only the database that deals with your application logic. This user will have access to do any write/read operations on your  `MONGO_INITDB_DATABASE`
```
* MONGO_INITDB_DATABASE=<your_app_database_name>
* MONGO_INITDB_DATABASE_ADMIN=<your_app_database_admin_name>
* MONGO_INITDB_DATABASE_PASSWORD=<your_app_database_admin_password>
```
