[![Build Status](https://travis-ci.com/Gabkings/the-api.svg?branch=develop)](https://travis-ci.com/Gabkings/the-api)   [![Maintainability](https://api.codeclimate.com/v1/badges/341c078ef39e63e8af17/maintainability)](https://codeclimate.com/github/Gabkings/the-api/maintainability)   [![Coverage Status](https://coveralls.io/repos/github/Gabkings/the-api/badge.svg?branch=develop)](https://coveralls.io/github/Gabkings/the-api?branch=develop)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/682f02da75a048b3899a74fe90696dfb)](https://www.codacy.com/app/Gabkings/the-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Gabkings/the-api&amp;utm_campaign=Badge_Grade)
## My api sample documentation
url(https://web.postman.co/collections/5297757-5bd5506e-1a6e-4b9b-9d90-1700f714f895?workspace=53e189ce-e915-4e5b-8e11-c56791173e49 )

## Use the following endpoints to perform the specified tasks

  |     Endpoint                       | Functionality                                  |                  
  | ---------------------------------| -----------------------------------------------|
  | POST /v1/orders                  | Create an order                                |
  | GET /v1/orders                   | Retrieve all posted orders                     |
  | PUT /v1/orders/<int:order_id>    | Update a specific order                        |                         
  | GET /v1/orders/<int:order_id>    | Get a specific posted order                    |
  | DELETE /v1/orders/<int:order_id> | DELETE a specific posted order                 |


### Orders:

POST api/v1/orders  - Create an order
<br>
{       <br>
    "id": 1,
    <br>
    "name": "Rice",
    <br>
    "Price": 123
    <br>
    "description": "sweet rice"
}


GET api/v1/orders -Get all orders


PUT api/v1/orders/1  - Update status of an order automatically
<br>



DELETE api/v1/orders/1  -Delete an order


GET api/v1/orders/1  - Get an order by order id


## Application Features

1. Create orders
2. view, and update order status of an order.


<br>

## How to Test Manually
1. Clone the project to your local machine <br>
        ` https://github.com/Gabkings/the-api/tree/develop`
2. Create Virtual Environment <br>
        `virtualenv env`
3. Activate Virtual ENvironment<br>
        `source venv/Scripts/activate`
4. Install Dependencies<br>
        `(venv)$ pip3 install -r requirements.txt` <br>
        
5. Run the app <br>
        `python3 run.py`<br>
6. Run tests <br>
        `nosetests --with-coverage --cover-package=app/tests/v1`
        <br>
