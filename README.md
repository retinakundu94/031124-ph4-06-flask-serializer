# Flask SQLAlchemy Serializer

## Learning Goals

- SerializerMixin for single model

- Using db.ForeignKey

- Using db.relationship

- Using association_proxy

- SerializerMixin for multiple models

## Getting Started

Being with:

```
pipenv install
pipenv shell
cd server
```

The `models.py` file is missing certain important things... be sure to add them!

From there:

```
flask db init
flask db migrate -m "initialize database"
flask db upgrade
```