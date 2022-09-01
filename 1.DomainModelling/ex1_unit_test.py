from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set

## Then Create Classes

@dataclass(frozen=True) ## Immutable Class with no Behaviour
class OrderLine:
    orderid: str
    sku: str
    qty: int

class Batch():
    def __init__(self, ref:str, sku:str, qty:int, eta: Optional[date]): 
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_qty = qty
        self._allocations = set() # type: Set[OrderLine]

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


## Create Tests (TDD)

## helper function
def make_batch_and_line(sku, batch_qty, line_qty):
    return (
         Batch("batch-001",sku, batch_qty, eta=date.today()),
         OrderLine("order-123",sku, line_qty)
    )
   
def test_can_allocate_if_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP",20,2)
    assert large_batch.can_allocate(small_line), "Should be able to allocate if batch quantity greater than line order quantity"

def test_cannot_allocate_if_greater_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP",2,20)
    assert small_batch.can_allocate(large_line) is False, "Should not be able to allocate if batch quantity less than line order quantity"

def test_can_allocate_if_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP",2,2)
    assert batch.can_allocate(line), "Should be able to allocate if batch quantity equal to line order quantity"

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001","BAD-CHAIR", 100, eta=None)
    different_sku_orderline = OrderLine("order-123","BAD-TABLE", 10)
    assert batch.can_allocate(different_sku_orderline) is False, "Should not be able to allocate if skus do not match"

def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("STUPID-DESK",20,2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18, "Should not be able to allocate if line order already exists"

test_cannot_allocate_if_greater_than_required()
test_can_allocate_if_greater_than_required()
test_can_allocate_if_equal_to_required()
test_cannot_allocate_if_skus_do_not_match()
test_allocation_is_idempotent()



