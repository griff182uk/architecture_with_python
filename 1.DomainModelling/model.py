from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

## Then Create Classes

## Immutable Class with no Behaviour. A VALUE OBJECT as has no identity.
## Remember OrderId is for order and not for OrderLine
@dataclass(frozen=True) 
class OrderLine:
    orderid: str
    sku: str
    qty: int

## Batch has a reference so has a long lived identity
## Therefore domain object called ENTITY
class Batch():
    def __init__(self, ref:str, sku:str, qty:int, eta: Optional[date]): 
        self._reference = ref ## make read only. Underscore is private by convention
        self.sku = sku
        self.eta = eta
        self._purchased_qty = qty
        self._allocations = set() # type: Set[OrderLine]

    ## Making reference read only by making it a property
    @property
    def reference(self):
        return self._reference

    ## make official string representation of object
    ## this good for debugging and can be whatever you want
    ## print(repr(batch))
    def __repr__(self):
        return f"<Batch {self.reference}>"

    ## how does it determine if it is the same as another batch
    ## it compares the reference property values
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    ## hashes its batch reference property to uniquely identify self
    ## this dictates how object behaves when added to sets or dict keys
    def __hash__(self):
        return hash(self.reference)

    ## allows for less than or equal operators on the batch object
    ## based on the eta property
    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line : OrderLine):
        if(self.can_allocate):
            self._allocations.add(line)

    def deallocate(self, line : OrderLine):
        if(line in self._allocations):
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_qty - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty


## Create domain service "allocate" as does not belong in an entity
def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")

class OutOfStock(Exception):
    pass