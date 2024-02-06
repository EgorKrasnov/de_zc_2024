docker rm -f mysql_dbt
docker run -it \
--name mysql_dbt \
-e MYSQL_USER=test \
-e MYSQL_ROOT_PASSWORD=123 \
-e MYSQL_PASSWORD=123 \
-e MYSQL_DATABASE=dbt_test \
-p 9000:3306 \
--rm -d \
-v $(pwd)/mysql_data:/var/lib/mysql \
mysql
