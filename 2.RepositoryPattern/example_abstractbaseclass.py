## https://python-course.eu/oop/the-abc-of-abstract-base-classes.php


from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass

## will fail as not implementing do_something
# class DoAdd42(AbstractClassExample):
#     pass

# x = DoAdd42(4)


## will work as do_something implemented

class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42
    
class DoMul42(AbstractClassExample):
   
    def do_something(self):
        return self.value * 42
    
x = DoAdd42(10)
y = DoMul42(10)

print(x.do_something())
print(y.do_something())

## showing can still call abstract class using super

from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()