
class LLNode:
    """Defines the value-containing node object for a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Defines a linked list object, consisting of a linked set of LLNode objects."""

    def __init__(self):
        """Initializes a linked list to be empty."""
        self.first = None

    def prepend(self, value):
        """Adds a node with `value` to the front of a linked list."""
        newNode = LLNode(value)
        newNode.next = self.first
        self.first = newNode

    def output(self):
        """Output the linked list's values, line by line. """
        current = self.first
        while current is not None:
            print(current.value)   # Print the contents of each node.
            current = current.next

    def append(self, value):
        "Adds a node with `value` to the end of a linked list."""
        if self.first is None:
            self.first = LLNode(value)
        else:
            current = self.first
            # Scan looking for the last node.
            while current.next is not None:
                current = current.next
            current.next = LLNode(value)

    def contains(self, value):
        """Returns whether `value` is in the linked list."""
        current = self.first
        while current is not None:
            if current.value == value: # If it is found...
                return True
            current = current.next
        return False  # Scanned the whole list, not found.

    def asString(self):
        """Returns a string that is the linked list's sequence."""
        if self.first is None:
            return "<>"
        else:
            s = "<" + str(self.first.value)
            current = self.first.next
            while current is not None:
                s = s + ", " + str(current.value)
                current = current.next
            s = s + ">"
            return s

    def length(self):
        """Returns the number of nodes in the linked list."""
        count = 0
        current = self.first
        while current is not None:
            count = count + 1      # Count each node.
            current = current.next
        return count

    def isEmpty(self):
        """Returns whether the linked list is empty."""
        return (self.first is None)

    def display(self):
        """Outputs the linked list as a sequence."""
        print(self.asString())

    def delete(self, value):
        """Removes `value` from the linked list if there."""
        previous = None  # Track the node one behind.
        current  = self.first
        # Scan all the nodes looking for the value.
        while current is not None and current.value != value:
            previous = current
            current = current.next
        # Stop scan when we've found it or scanned them all.
        if current is not None:   # If it was found...
            if previous is None:  # If it was found at the front...
                # Remove from the front.
                if current.next is None:
                    print("a")
                    self.first = None
                    self.last = None    
                else:
                    print("b")
                    self.first = current.next
                    self.first.prev = None

            else:                 # If it was one of the later nodes...
                if current.next is not None:# Skip past it with the previous node's link.
                    print("c")
                    previous.next = current.next
                else:
                    print("d")
                    self.last = current.prev
                    self.last.next = None

    def __str__(self):
        return self.asString()

    def __repr__(self):
        return self.asString()

    def __bool__(self):
        return not self.isEmpty()

    def sum(self):
        s = 0
        prev = None
        curr = self.first
        while curr is not None:
            s += curr.value
            prev = curr
            curr = curr.next
        return s

    def count(self, num):
        s = 0
        prev = None
        curr = self.first
        while curr is not None:
            if curr.value == num:
                s += 1
            prev = curr
            curr = curr.next
        return s
    
    def apply(self,f):
        prev = None
        curr = self.first
        while curr is not None:
            curr.value = f(curr.value)
            prev = curr
            curr = curr.next
        
    def deleteAll(self,num):
        prev = None
        curr  = self.first
        while curr is not None: 
            if curr.value == num:
                if prev == None:
                    self.first = curr.next
                    curr = self.first
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
            
class Queue(LinkedList):

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        if self.first == None:
            self.first = LLNode(value)
            self.last = LLNode(value)
        else:
            curr = self.first
            while curr.next != None:
                curr = curr.next
            curr.next = LLNode(value)
            self.last = curr.next
    
    def dequeue(self):
        x = self.first.value
        self.first = self.first.next
        return x

    def head(self):
        if self.first != None:
            return self.first.value
        else:
            return None

        
class Sorted(LinkedList):
    def append(self,val):
        curr = self.first
        prev = None
        if curr == None:
            self.first = LLNode(val)
            return
        if self.first.value >= val:
            x = self.first
            self.first = LLNode(val)
            self.first.next = x
            return
        while curr is not None: #and curr.value > val:
            if curr.value < val:
                prev = curr
                curr = curr.next
            
            else:
                prev.next = LLNode(val)
                prev.next.next = curr
                return
       
        prev.next = LLNode(val)
    