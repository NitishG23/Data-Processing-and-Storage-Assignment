class InMemoryDB:
    def __init__(self):
        self.main_store = {}
        self.transaction_store = None
        self.in_transaction = False

    def get(self, key):
        return self.main_store.get(key, None)
    
    def put(self, key, val):
        if not self.in_transaction:
            raise Exception("no active transaction -> cannot put values outside of a transaction")
        self.transaction_store[key] = val

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("a transaction is already in progress")
        self.in_transaction = True
        self.transaction_store = {}

    def commit(self):
        if not self.in_transaction:
            raise Exception("there is no open transaction to commit")
        for k, v in self.transaction_store.items():
            self.main_store[k] = v
        self.transaction_store = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise Exception("there is no ongoing transaction to rollback")
        self.transaction_store = None
        self.in_transaction = False
