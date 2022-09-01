## Then Create Classes

class Order():
    def __init__(self, sku, quantity): 
        self.order_reference = 1
        self.sku = sku
        self.quantity = quantity

class Batch():
    def __init__(self, sku, quantity): 
        self.reference = 1
        self.sku = sku
        self.quantity = quantity

    orders = []

    def allocate_order(self,order):
        if(self.sku == order.sku):
            if not (order in (self.orders)):
                if(self.quantity >= order.quantity):
                    self.orders.append(order)
                    self.quantity = self.quantity - order.quantity

## Create Tests (TDD)

def test_cant_allocate_batch_quantity_less_order():
    batch = Batch("BLUE-CUSHION",1)
    order = Order("BLUE-CUSHION",2)
    batch.allocate_order(order)
    assert(batch.quantity == 1), "Batch should not accept orders where batch is less than order quantity."

def test_cant_allocate_batch_same_order():
    batch = Batch("BLUE-VASE",10)
    order = Order("BLUE-VASE",8)
    batch.allocate_order(order)
    batch.allocate_order(order)
    assert(batch.quantity == 2), "Batch should only accept one order of same."

test_cant_allocate_batch_same_order()
test_cant_allocate_batch_quantity_less_order()


