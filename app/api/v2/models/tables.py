users = """CREATE TABLE if not exists users (
    id bigserial UNIQUE PRIMARY KEY,
    email varchar(50) NOT NULL UNIQUE,
    username varchar(12) NOT NULL UNIQUE,
    type varchar(250) NOT NULL DEFAULT 'user',
    password varchar(250) NOT NULL
    );"""

meals_table = """
CREATE TABLE IF NOT EXISTS meals (
    meal_id serial PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    price INT NOT NULL,
    description VARCHAR(25) NOT NULL
)
"""


orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id serial PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(200),
    createddate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price INT NOT NULL,
    status VARCHAR (100) NOT NULL DEFAULT 'Pending',
    address VARCHAR (100) NOT NULL
    )
"""


queries = [users, meals_table, orders_table]