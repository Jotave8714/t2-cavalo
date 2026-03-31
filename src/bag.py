class Bag:
    """Linked-list style bag (LIFO iteration order)."""

    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.insert(0, item)  # prepend – last in, first out

    def __iter__(self):
        return iter(self._items)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        return " ".join(str(i) for i in self._items)
