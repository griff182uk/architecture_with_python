from __future__ import annotations

from src.allocation.domain import model
from src.allocation.domain.model import OrderLine, Batch
from src.allocation.adapters.repository import AbstractRepository

class InvalidSku(Exception):
    pass

def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}


def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
    batches = repo.list()
    if not is_valid_sku(line.sku, batches):
        raise InvalidSku(f"Invalid sku {line.sku}")
    batchref = model.allocate(line, batches)
    session.commit()
    return batchref

def add_batch(reference, sku, qty, eta, repo: AbstractRepository, session):
    batch = Batch(ref = reference, sku = sku, qty = qty, eta = eta)
    repo.add(batch)
    session.commit()

def deallocate(line: OrderLine, batch: Batch, session) -> str:
    batch.deallocate(line)
    session.commit()