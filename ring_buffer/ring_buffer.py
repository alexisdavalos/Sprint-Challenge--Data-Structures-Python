from dll import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.marker = None

    def append(self, item):

        print(f'Marker: {self.marker}')
        # check if there is enough room to store item
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            print(f'Buffer Size: {len(self.storage)}/{self.capacity}')
            
            # set marker marker to first node input to list
            if len(self.storage) == 1:
                self.marker = self.storage.head
        # reached max capacity   
        else:
        # overwrite marker value with input item
            self.marker.value = item
            # move marker to the next oldest. loop back to the head upon reaching the tail
            if self.marker.next:
                self.marker = self.marker.next
            else:
                self.marker = self.storage.head
            # print(f'Next Marker: {self.marker}')
        

    def get(self):
         print(self.storage.get_all())
         return self.storage.get_all()

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']