users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY, 
    username VARCHAR(200) NOT NULL,
    email VARCHAR(250) NOT NULL,
    password VARCHAR(200) NOT NULL,
    type VARCHAR(200) NOT NULL
)
"""

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
    ordered_date VARCHAR(250) NOT NULL,
    price INT NOT NULL,
    status VARCHAR (25) NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
"""

queries = [users_table, meals_table, orders_table]