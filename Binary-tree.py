#source : https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
# https://www.geeksforgeeks.org/priority-queue-using-linked-list/


class BinaryNode:

    def __init__(self,data, distance):
        self.left = None
        self.right = None
        self.data = data
        self.distance = distance

    def Printtree(self):
        if self.left:
            self.left.Printtree()
        print(self.data)
        if self.right:
            self.right.Printtree()

class BinaryTree:
    def __init__(self,num):
        self.root = BinaryNode(1,0)
        self.island = [0 for i in range(num+1)]
        self.island[1] = self.root

    def insert(self,num ,data, decider):
        node = self.island[num]
        if data != '0':
            Node = BinaryNode(int(data), node.distance+1)
            if decider == "kiri":
                node.left = Node
            elif decider == "kanan":
                node.right = Node
            self.island[int(data)] = Node
            
    
    def Printtree(self):
        if self.root:
            self.root.Printtree()


class PriorityQueueNode:
     
  def __init__(self, value, pr, destination, distance):
       
    self.data = value
    self.priority = pr
    self.next = None
    self.island = destination
    self.distance = distance

         
# Implementation of Priority Queue
class PriorityQueue:
     
    def __init__(self):
         
        self.warehouse = set()
        self.front = None
         
    # Method to check Priority Queue is Empty
    # or not if Empty then it will return True
    # Otherwise False
    def isEmpty(self):
         
        return True if self.front == None else False
     
    # Method to add items in Priority Queue
    # According to their priority value
    def push(self, value, priority, destination, distance):
        # Condition check for checking Priority
        # Queue is empty or not
        if self.isEmpty() == True:
            self.front = PriorityQueueNode(value, priority, destination, distance)
            return 1
        else:
            # Special condition check to see that
            # first node priority value
            if self.front.priority > priority:
                newNode = PriorityQueueNode(value, priority, destination, distance)
                # Updating the new node next value
                newNode.next = self.front
                # Assigning it to self.front
                self.front = newNode
                # Returning 1 for successful execution
                return 1
                 
            else:
                # Traversing through Queue until it
                # finds the next smaller priority node
                temp = self.front
                 
                while temp.next:
                     
                    # If same priority node found then current
                    # node will come after previous node
                    if priority < temp.next.priority:
                        break
                     
                    temp = temp.next
                 
                newNode = PriorityQueueNode(value,
                                            priority, destination, distance)
                newNode.next = temp.next
                temp.next = newNode
                 
                # Returning 1 for successful execution
                return 1
     
    # Method to remove high priority item
    # from the Priority Queue
    def pop(self):
         
        # Condition check for checking
        # Priority Queue is empty or not
        if self.isEmpty() == True:
            return
         
        else: 
             
            # Removing high priority node from
            # Priority Queue, and updating front
            # with next node
            #temp = self.front
            self.front = self.front.next
            
            #self.warehouse.remove(temp.data)
            return 1
             
    def traverse(self):

        # Condition check for checking Priority
        # Queue is empty or not
        if self.isEmpty() == True:
            return 
        else:
            return self.front

    def delete(self,value):
        # Store the head node as temp
        temp = self.front
        # If temp is not empty and if temp holds the value, print "BERHASIL" and return
        if temp is not None:
            if temp.data == value:
                self.front = temp.next
                print("BERHASIL")
                return 
        # If temp is not empty but temp does not holds the value,
        # iterate each data and keep iterating until it find the value
        while temp is not None:
            if temp.data == value:
                print("BERHASIL")
                break
            prev = temp
            temp = temp.next
        # Print out "GAGAL" if the value is not in the linked list
        if temp == None:
            print("GAGAL")
            return 

        prev.next = temp.next



 
def main():

    pq = PriorityQueue()             # set pq as priorityqueue class
    
    inputSatu = input("")           # inputsatu as first input
    bt = BinaryTree(int(inputSatu))
    for j in range(int(inputSatu)):      # for loop based on the first input
        inputDua = input("")
        akarKiri = inputDua.split()[0]
        akarKanan = inputDua.split()[1]
        bt.insert(j+1, akarKiri, "kiri")
        bt.insert(j+1, akarKanan, "kanan")
        

    inputKetiga = input("")             # receive second input
    for i in range(int(inputKetiga)):
        inputKeempat = input("")
        dibagi = inputKeempat.split()
        if dibagi[0] == "1":
            distance = bt.island[int(dibagi[3])].distance
            # VALUE, PRIORITY, DESTINATION, DISTANCE
            pq.push(dibagi[1],int(dibagi[2]), int(dibagi[3]), distance)

        elif dibagi[0] == "2":
            pq.delete(dibagi[1])
        elif dibagi[0] == "3":
            result = []
            listDua = []
            listTiga = []

            test = pq.traverse()
            for j in range(int(dibagi[1])):
                if test != None:
                    pq.pop()
                    distance = test.distance

                    island = test.island

                    name = test.data

                    result.append(name)            # Result is filled with name of the package
                    listDua.append(int(distance))  # ListDua is filled with the distance from warehouse to island destination
                    listTiga.append(int(island))   # lisTiga is filled with the island number

                    test = test.next

            panjang = len(result)
            # Make the sorting method based on
            # what is asked on the question
            for j in range(panjang):
                for i in range(int(panjang)-1):
                    if listDua[i] > listDua[i+1]:
                        result[i], result[i+1] = result[i+1],result[i]
                        listDua[i], listDua[i+1] = listDua[i+1], listDua[i]
                        listTiga[i], listTiga[i+1] = listTiga[i+1], listTiga[i]
                    elif listDua[i] == listDua[i+1]:
                        if listTiga[i] > listTiga[i+1]:
                            result[i], result[i+1] = result[i+1],result[i]
                            listDua[i], listDua[i+1] = listDua[i+1], listDua[i]
                            listTiga[i], listTiga[i+1] = listTiga[i+1], listTiga[i]
                        elif listTiga[i] ==listTiga[i+1]:
                            if result[i]>result[i+1]:
                                result[i], result[i+1] = result[i+1],result[i]
                                listDua[i], listDua[i+1] = listDua[i+1], listDua[i]
                                listTiga[i], listTiga[i+1] = listTiga[i+1], listTiga[i]
                

            for i in result:
                print(i)

if __name__ == "__main__":
    main()