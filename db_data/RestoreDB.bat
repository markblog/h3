"C:\Program Files\PostgreSQL\9.5\bin\dropdb.exe" -i -Upostgres auto_plan
"C:\Program Files\PostgreSQL\9.5\bin\pg_restore.exe" -Upostgres -C -d postgres  db.dump
