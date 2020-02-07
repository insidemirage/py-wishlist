import pymysql
import config
pymysql.connect(config.host, config.user, config.password, config.database)
# docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=mySchema mysql