from dataclasses import dataclass

## Value Object - Defined by its Attributes
# Name
## The names tested are not the same

@dataclass(frozen=True) 
class Name:
    first_name: str
    surname: str

def test_name_equality():
    assert Name("Harry","Percival") != Name("Barry","Percival")


## Entity Person 

## People persist and can change their names

class Person:
    def __init__(self, name: Name):
        self.name = name

def test_barry_is_harry():
    harry =  Person(Name("Harry","Percival"))
    barry = harry

    barry.name = Name("Barry","Percival")

    assert harry is barry and barry is harry