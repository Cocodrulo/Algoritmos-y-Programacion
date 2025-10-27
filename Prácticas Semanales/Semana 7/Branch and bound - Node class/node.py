from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room
        return

    def estimate(self, items):
        current_estimate = self.value

        for node_idx in range(self.index, len(items)):
            current_estimate += items[node_idx].value

        return current_estimate
