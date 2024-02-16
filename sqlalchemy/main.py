from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base

# Initializing the Base class to create a new instances
Base = declarative_base()


# Extending the base class to create a model
class Person(Base):
    # Specifying the name for the table
    __tablename__ = 'persons'

    # Creating the columns in the table
    # 1st arg - id=> Name of the column in the database
    # 2nd arg - Integer=> Data Type of the column
    # 3rd arg - primary_key=> Constraint for the column

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(128), nullable=False)
    last_name = Column('last_name', String(128), nullable=False)
    age = Column('age', Integer, nullable=False)
    ssn = Column('ssn', Integer, nullable=False)

    # Specifying the required field to create the instance
    def __init__(self, id, first_name, last_name, age, ssn):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.ssn = ssn

    # Customize the Class with meaningful names
    def __repr__(self):
        return f"{self.first_name} : {self.last_name}"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(128))
    person = Column(Integer, ForeignKey("persons.id"))

    def __init__(self, username, person):
        self.username = username
        self.person = person

    def __repr__(self):
        return f"{self.username} >> {self.person}"


# Creating the engine for the database we are working with
engine = create_engine("postgresql+psycopg2://shop_user:12345@localhost:5432/test")
# Creating the tables
Base.metadata.create_all(engine)

# Creating a session for the desired engine
Session = sessionmaker(bind=engine)
# Creating the session object to use further
session = Session()
# Creating an instance of PErson model
# p1 = Person(1, 'Gopi', 'B', 27, 123)
# p2 = Person(2, 'Krishna', 'B', 28, 234)
p3 = Person(3, 'King', 'B', 26, 345)
# print(p1.id)
# u1 = User('BGK', p1.id)
# u2 = User('GK', p2.id)
# Adding the Created person model instance into the database
# session.add(p1)

# Adding the Created person models(Multiple) instances into the database
# session.add_all([p2, p3])
session.add(p3)

# session.add(u1)
# session.add(u2)

# Saving/Committing the changes into the database
session.commit()

# Fetching all the person records from the database
persons = session.query(Person).all()
print(f"[x] Printing the persons list:")
for p in persons:
    print(p.id, p.first_name, p.last_name, p.age, p.ssn)

# Filtering the person records from the database
person_gopi = session.query(Person).filter(Person.first_name == "Gopi")
print(f"\n[x] Printing the person whose name is 'Gopi':")
for p in person_gopi:
    print(p.id, p.first_name, p.last_name, p.age, p.ssn)

# Fetching the first matching person record from the database
p3 = session.query(Person).filter(Person.first_name == "King").first()

print(f"\n[x] Printing the person name Before deleting 'King':")

# Deleting the person record from the database
session.delete(p3)

# Committing the changes to the database after deleting the person record
session.commit()
