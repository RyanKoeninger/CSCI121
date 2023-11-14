class DLLNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def prepend(self,value):
        if self.first is not None:
            newNode = DLLNode(value)
            x = self.first
            newNode.next = self.first
            self.first = newNode
            x.prev = self.first
        else:
            newNode = DLLNode(value)
            self.first = newNode
            self.last = newNode

    def output(self):
        current = self.first
        while current is not None:
            print(current.value)   # Print the contents of each node.
            current = current.next

    def append(self, value):
        "Adds a node with `value` to the end of a linked list."""
        if self.first is None:
            newNode = DLLNode(value)
            self.first = newNode
            self.last = newNode
        else:
            newNode = DLLNode(value)
            current = self.last
            current.next = newNode
            self.last = newNode
            self.last.prev = current

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
          # Track the node one behind.
        current  = self.first
        # Scan all the nodes looking for the value.
        while current is not None and current.value != value:
            current = current.next
        # Stop scan when we've found it or scanned them all.
        if current is not None:   # If it was found...
            if current.prev is None:  # If it was found at the front...
                # Remove from the front.
                self.first = current.next
                current.next.prev = None
            elif current.prev is not None and current.next is not None:
            # If it was one of the later nodes..
                # Skip past it with the previous node's link.
                current.prev.next = current.next
                current.next.prev = current.prev
                current.prev = None
                current.next = None
            else:
                self.last = current.prev
                current.prev = None
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