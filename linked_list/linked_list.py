
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head:
            return self.head.value 
        return None


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        i = 0
        current = self.head
        while i < index and current:
            current = current.next
            i += 1

        if current:
            return current.value
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next

        return current.value
        

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if not self.head:
            self.add_first(value)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if not self.head:
            return None

        max_hold = self.head.value
        current = self.head

        while current:
            if max_hold < current.value:
                max_hold = current.value
            current = current.next
        
        return max_hold

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            return None

        current = self.head

        if current.value == value:
            self.head = current.next
            return

        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        current = self.head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        self.head = prev

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        outside_walker = self.head
        mid_walker = self.head
        count = 0

        while outside_walker:
            outside_walker = outside_walker.next
            count += 1
            if count % 2 == 0:
                mid_walker = mid_walker.next

        return mid_walker.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        outside_walker = self.head
        nth_walker = self.head
        count = 0

        while outside_walker:
            outside_walker = outside_walker.next
            if count > n:
                nth_walker = nth_walker.next
            count += 1

        if count < n +1:
            return None
        return nth_walker.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        seen_set = set(())
        current = self.head

        while current:
            if current in seen_set:
                return True
            seen_set.add(current)
            current = current.next

        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
