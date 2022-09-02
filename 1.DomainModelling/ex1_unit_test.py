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

def test_deallocate():
    batch, line = make_batch_and_line("EXPENSIVE-FOOTSTOOL", 20, 2)
    batch.allocate(line)
    batch.deallocate(line)
    assert batch.available_quantity == 20, "Should be able to deallocate"

def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20, "Should only be able to deallocate allocated lines"

test_cannot_allocate_if_greater_than_required()
test_can_allocate_if_greater_than_required()
test_can_allocate_if_equal_to_required()
test_cannot_allocate_if_skus_do_not_match()
test_allocation_is_idempotent()
test_deallocate()
test_can_only_deallocate_allocated_lines()



today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)

def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
    shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_prefers_earlier_batches():
    earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
    medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
    latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine("order1", "MINIMALIST-SPOON", 10)

    allocate(line, [medium, earliest, latest])

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    assert allocation == in_stock_batch.reference


def test_raises_out_of_stock_exception_if_cannot_allocate():
    batch = Batch("batch1", "SMALL-FORK", 10, eta=today)
    allocate(OrderLine("order1", "SMALL-FORK", 10), [batch])

    with pytest.raises(OutOfStock, match="SMALL-FORK"):
        allocate(OrderLine("order2", "SMALL-FORK", 1), [batch])



