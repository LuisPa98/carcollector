CREATE DATABASE shoecollector;

CREATE USER shoe_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE shoecollector TO shoe_admin;