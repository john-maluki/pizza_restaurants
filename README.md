# Flask Code Challenge - Pizza Restaurants

For this assessment, you'll be working with a Pizza Restaurant domain.
Your job is to build out the Flask API to add the functionality described in the deliverables below.

Test you endpoints as stated below

- Running the Flask server and using Postman to make requests

## Models

You need to create the following relationships:

- A `Restaurant` has many `Pizza`'s through `RestaurantPizza`
- A `Pizza` has many `Restaurants` through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`

Start by creating the models and migrations for the following database tables:

<img src="doc/screenshots/domain.png" alt="table relations for models">

## Validations

Add validations to the RestaurantPizza model:

- must have a `price` between `1` and `30`

Add validations to Restaurant Model:

- must have a name less than 50 words in length
- must have a unique name

## Routes

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.

**GET /restaurants**
Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
```

**GET /restaurants/:id**
If the `Restaurant` exists, return JSON data in the format below:

```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```

If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

**DELETE /restaurants/:id**
If the `Restaurant` exists, it should be removed from the database, along with any `RestaurantPizzas` that are associated with it (a `RestaurantPizza` belongs to a `Restaurant`, so you need to delete the `RestaurantPizzas` before the `Restaurant` can be deleted).

After deleting the `Restaurant`, return an empty response body, along with the appropriate HTTP status code.

If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

**GET /pizzas**
Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

**POST /restaurant_pizzas**
This route should create a new `RestaurantPizza` that is associated with an existing `Pizza` and `Restaurant`. It should accept an object with the following properties in the body of the request:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

If the `RestaurantPizza` is created successfully, send back a response with the data related to the `Pizza`:

```json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```

If the `RestaurantPizza` is not created successfully, return the following JSON data, along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

## Technologies Used

The following have been used on this project:

- [Python3](https://docs.python.org/3.10/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [Pytest](https://docs.pytest.org/en/latest/contents.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask Restful](https://flask-restful.readthedocs.io/en/latest/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Faker](https://faker.readthedocs.io/en/master/)

## Database

This project uses SQLit3:

[SQLite](https://www.sqlite.org/docs.html) - Acording to [SimpleLearn](www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite) SQLite is one of the most popular and easy-to-use relational database systems. It possesses many features over other relational databases. Many big MNCs such as Adobe, use SQLite as the application file format for their Photoshop Lightroom product. Airbus, a European multinational aerospace corporation, uses SQLite in the flight software for the A350 XWB family of aircraft. You will learn various concepts and get hands-on practice in this SQLite tutorial.

## Project Setup

- Clone the repository: `git clone <repository-url>`
- Navigate to cloned repository: `cd pizza_restaurants`
- Create pipenv environment and Install dependencies: `pipenv install`
- Activate environment: ` pipenv shell`
- Then run this commands: `export FLASK_APP=run.py && export FLASK_RUN_PORT=5555`
- Create db with flask migrate: `cd app && flask db updgrade head`
- Populate db with seed file: `cd .. && python3 seed.py`
- Then, start flask applcation: `python run.py` or `flask run` or `gunicorn run:app`

## How to run tests.

Use pytest to run tests

- From the root directory (`pizza_restaurants`) run pytest: `pytest` or `pytest -x`

## Authors

- [John Maluki](https://github.com/john-maluki)

## Copyright

Released under the MIT License. See the [LICENSE](https://github.com/john-maluki/pizza_restaurants/blob/main/LICENSE) file.
