class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
            
class Stack:
    def __init__(self):
        self.max = 10000
        self.top = None

    def push(self, *value):
        
        for i in value:
            node = Node(i)
            temp = self.top # temp = None
            self.top = node # top = node(5)
            self.top.next = temp # node(5).next = None
        
        
    def pop(self):
        try:
            temp = self.top.value
            self.top = self.top.next # top = node(5)
            return temp
        except AttributeError as e:
            return f"Empty"
        except Exception as e:
            return f"Some other exception happened!!!"
    def peek(self):
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        if self.top:
            # stack have values 
            return False
        else:
            # stack have no values
            return True
    def __str__(self):
        current = self.top
        output = ''
        while current:
            output += f"[{current.value}]"
            current = current.next
        output=f'Stack {output}'
        return output
    
    def __iter__(self):
            def values_generator():
                current = self.top
                while current:
                    yield current.value
                    current = current.next
            return values_generator()

    def __len__(self):
        return len(list(iter(self)))

    def __getitem__(self, index):
            if index < 0:
                index = len(self) + index

            for i, item in enumerate(self):
                if i == index:
                    return item
            raise IndexError

    def __eq__(self,other):
        return list(iter(self)) == list(iter(other))



if __name__ == '__main__':
    stack=Stack()
    stack2=Stack()
    # stack2.push("a")
    # stack2.push(1)
    stack.push('s','a','l','e','h')
    print(stack)
    print(stack==stack2)