#Max Heap --> All child nodes of a node are smaller than the node (Root node is the largest node)
#Min Heap --> All child nodes of a node are larger than the node (Root node is the smllest node)

class MinHeap:

    def __init__(self):
        self.heap=[]
    
    def insert(self,val):
        self.heap.append(val)
        index=len(self.heap)-1
        while index>0:
            parent_index=(index-1)//2
            if self.heap[parent_index]<=self.heap[index]:
                break
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            index=parent_index
    
    def delete(self):      #We remove the top element from the heap and rearrange the heap
        if not self.heap:
            return False
        val=self.heap[0]
        # Move the last element to the root and remove the last element
        temp=self.heap.pop()
        if self.heap:
            self.heap[0]=temp
        # Perform the bubble-down (heapify-down) operation to maintain the heap property
        index=0
        length=len(self.heap)
        while True:
            left_child_index=2*index+1
            right_child_index=2*index+2
            smallest_index=index
            if left_child_index<length and self.heap[left_child_index]<self.heap[smallest_index]:
                smallest_index=left_child_index
            if right_child_index<length and self.heap[right_child_index]<self.heap[smallest_index]:
                smallest_index=right_child_index
            if smallest_index==index:
                break
            # Swap the current element with the smallest of its children
            self.heap[index],self.heap[smallest_index]=self.heap[smallest_index],self.heap[index]
            index=smallest_index
        return val
    
    def display(self):
        if not self.heap:
            print('Heap is empty')
        for i in self.heap:
            print(i,end=' ')

#############################################################################################################

class MaxHeap:

    def __init__(self):
        self.heap=[]
    
    def insert(self,val):
        self.heap.append(val)
        index=len(self.heap)-1
        while index>0:
            parent_index=(index-1)//2
            if self.heap[parent_index]>=self.heap[index]:
                break
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            index=parent_index
    
    def delete(self):      #We remove the top element from the heap and rearrange the heap
        if not self.heap:
            return False
        val=self.heap[0]
        # Move the last element to the root and remove the last element
        temp=self.heap.pop()
        if self.heap:
            self.heap[0]=temp
        # Perform the bubble-down (heapify-down) operation to maintain the heap property
        index=0
        length=len(self.heap)
        while True:
            left_child_index=2*index+1
            right_child_index=2*index+2
            smallest_index=index
            if left_child_index<length and self.heap[left_child_index]>self.heap[smallest_index]:
                smallest_index=left_child_index
            if right_child_index<length and self.heap[right_child_index]>self.heap[smallest_index]:
                smallest_index=right_child_index
            if smallest_index==index:
                break
            # Swap the current element with the smallest of its children
            self.heap[index],self.heap[smallest_index]=self.heap[smallest_index],self.heap[index]
            index=smallest_index
        return val
    
    def display(self):
        if not self.heap:
            print('Heap is empty')
        for i in self.heap:
            print(i,end=' ')