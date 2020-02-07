# PyQt5 powered Wishlist
## Install requirements
### Python
```
pip install PyQt5 PyMySQL
```
### MySQL(Docker)
```
sudo apt-get install docker docker.io
```

## Setup MySQL
### Run docker container
```
docker run --name=mysql_server --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest
docker exec -it mysql_server mysql -uroot -proot_password
```
### Creating settings for mysql
* Creating database and table

    ```
    CREATE DATABASE database_name;
    use database_name;
    CREATE TABLE database_name (Id VARCHAR(20), Name VARCHAR(200), Price VARCHAR(200), Link VARCHAR(200), Comment VARCHAR(200));
    ```
* Configure config.py
     ```py
        host = "localhost"
        user = "user"
        password = "password"
        database = "database_name"
        table = "table_name"
    ```

        
P.S: Price will change to int type in next update. DockerFile incoming soon.

## Run App

```
python3 main.py
```
