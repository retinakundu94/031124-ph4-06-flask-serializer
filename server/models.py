from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# Politician ###########
# name          string #
# position      string #
########################

class Politician():
    pass



# Scandal ##############
# headline      string #
# date          string #
########################
# (for the date we could use db.DateTime instead...)

class Scandal():
    pass



# Involvement ###########
# politician_id integer #
# scandal_id    integer #
# role          string  #
#########################

class Involvement():
    pass