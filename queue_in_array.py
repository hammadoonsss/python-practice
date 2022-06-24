class Queue:
    
    def __init__(self,c=7):
        self.queue = []
        self.front=self.rear=0
        self.capacity=c

    def queueEnqueue(self, data):
        
        if self.capacity==self.rear:
            print("OVERFLOW")
        
        else:
            self.queue.append(data)
            self.rear=+1
            
    def queueDequeue(self):
        
        if self.front==self.rear:
            print("Queue is Empty")
        
        else:
            x = self.queue.pop(0)
            self.rear=-1
            print("Remove", x)
    
    def queueDisplay(self):
        
        if self.front==self.rear:
            print("Queue is Empty!")
            
        else:
            for i in self.queue:
                print(i, "<--")
        
        
if __name__ == '__main__':
 
    queue = Queue(8)
    queue.queueDisplay()
    queue.queueEnqueue(10)
    queue.queueEnqueue(20)
    queue.queueEnqueue(30)
    queue.queueEnqueue(40)
    queue.queueDisplay()
    queue.queueDequeue()
    queue.queueDisplay()
        
