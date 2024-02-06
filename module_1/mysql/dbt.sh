docker rm -f dbt
docker run -it \
--name dbt \
--network=host \
--rm \
-v $(pwd)/dbt/project:/root/.dbt/ \
-w /root/.dbt/mysql \
--entrypoint dbt \
dbt_mysql:test \
debug
