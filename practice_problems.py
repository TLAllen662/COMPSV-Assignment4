"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # A set fits because it stores only distinct product IDs and supports fast membership checks.
    # Each ID is checked and added once, giving expected O(n) time and O(n) additional space.
    seen_ids = set()
    for product_id in product_ids:
        if product_id in seen_ids:
            return True
        seen_ids.add(product_id)
    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # A deque fits a FIFO queue because it supports adding at the back and removing from the front efficiently.
        # Both append and popleft take expected O(1) time, while the queue uses O(n) space for n pending tasks.
        from collections import deque

        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        return self.tasks.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        # A set fits because it automatically keeps only one copy of each value.
        # Adding and counting are expected O(1), so the tracker uses O(n) space for n distinct values.
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)
