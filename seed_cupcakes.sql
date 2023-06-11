-- psql -U <username> -f cupcakes.sql

CREATE DATABASE cupcakes;

\c cupcakes

CREATE TABLE cupcakes (
    id SERIAL PRIMARY KEY,
    flavor TEXT NOT NULL,
    size TEXT NOT NULL,
    rating FLOAT NOT NULL,
    image TEXT NOT NULL DEFAULT 'https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg'
);
