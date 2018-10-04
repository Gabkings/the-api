[![Build Status](https://travis-ci.com/Gabkings/the-api.svg?branch=develop)](https://travis-ci.com/Gabkings/the-api)   [![Maintainability](https://api.codeclimate.com/v1/badges/341c078ef39e63e8af17/maintainability)](https://codeclimate.com/github/Gabkings/the-api/maintainability)   [![Coverage Status](https://coveralls.io/repos/github/Gabkings/the-api/badge.svg?branch=develop)](https://coveralls.io/github/Gabkings/the-api?branch=develop)
## My api sample documentation
url(https://web.postman.co/collections/5297757-5bd5506e-1a6e-4b9b-9d90-1700f714f895?workspace=53e189ce-e915-4e5b-8e11-c56791173e49 )

## Use the following endpoints to perform the specified tasks

  ## Use the following endpoints to perform the specified tasks

  |   Endpoint                         | Functionality                                  |                  
  | ---------------------------------- | -----------------------------------------------|
  | POST /v2/users/orders              | Create an order                                |
  | GET /v2/orders/                    | Retrieve posted orders                         |
  | PUT /v2/orders/<int:order_id>      | Update a specific order                        |                         
  | GET /v2/orders/<int:order_id>      | Get a specific posted order                    |
  | DELETE /v2/orders/<int:order_id>   | DELETE a specific posted order                 |
  | GET /v2/users/orders/<int:order_id>| GET a specific user's orders                   |
  | POST /v2/menu                      | Create food item                               |
  | GET /v2/menu                       | Retrieve posted food                           |
  | PUT /v2/food/<int:food_id>         | Update a specific food                         |                         
  | GET /v2/food/<int:food_id>         | Get a specific posted food                     |
  | DELETE /v2/food/<int:food_id>      | DELETE a specific posted food                  |
  | POST /v2/auth/signup               | Sign up User                                   |
  | POST /v2/auth/login                | Login User                                     |
  | PUT /v2/users/<int:id>             | Update a specific user                         |                         
  | GET /v2/users/<int:id>             | Get a specific signed up user                  |
  | DELETE /v2/users/<int:id>          | DELETE a specific signed up user               |
  | GET /v2/users                      | Get all signed up users                        |
  | GET /v2/auth/logout                | Logout a user                                  |

  ## Features Present in the app

  1. Create new orders.
  2. view, accept, decline and complete an order.
  3. Create, edit and delete Food items.
  4. Authentication.
  <br>

  **Users can do the following**

  * Users can create an account and log in.
  * Users can order food.
  * Users can view history of their order.

  **Admin can do the following**
  * Admin can add, edit and delete food items.
  * Admin can view, accept, decline and complete an order.

  ## How to Test Manually
  1. Clone the project to your local machine <br>
      ` https://github.com/Gabkings/the-api`
  2. Create Virtual Environment <br>
      `virtualenv venv`
  3. Activate Virtual Environment<br>
      `source venv/bin/activate`
  4. Install Dependencies<br>
      `(venv)$ pip3 install -r requirements.txt` <br>
      `(venv)$ pip3 freeze > requirements.txt` <br>
  5. Set up database.    
  6. Run the app <br>
      `python3 run.py`<br>
  7. Run tests <br>
      `pytest`
      <br>
  ## How to Contribute to this project?

  1. Fork the project to your github account.

  2. Clone it to your local machine.

  3. Create a feature branch from develop branch :

  4. git checkout -b `ft-name-of-the-feature`

  5. Update and Push the changes to github.

  6. git push origin `ft-name-of-the-feature`

  7. Create Pull Request to my develop branch as base branch.
        <br>
