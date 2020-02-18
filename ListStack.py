class EmptyStack(Exception):
    """ Stack is empty. """
    pass

class ListStack():
    """ Use Python's list datastructure to implement a Stack Data Structure """
    
    def __init__(self):
        """ Creates a Stack with a list backend """
        
        self._data = []

    def push(self, element):
        """ pushes the element to the top of the stack

            Args:
                param1: the element that is being added to the top of the stack
        """

        self._data.append(element)
    
    def pop(self):
        """ Removes and returns the element at the top of the stack 

            Returns:
                element: the element at the top of the stack

            Raises:
                EmptyStack: if the stack is empty at call time
        """

        if len(self._data) == 0:
            print("EmptyStack: can't call pop on an empty stack")
            raise EmptyStack
        else:
            return self._data.pop()

    def top(self):
        """ Shows the top element in the stack 

            Returns:
                element: shows the element at the top of the stack
            
            Raises:
                EmptyStack: if the stack is empty at call time
        """

        if len(self._data) == 0:
            print("EmptyStack: can't call top on an empty stack")
            raise EmptyStack
        else:
            return self._data[-1]

    def is_empty(self) -> bool:
        """ Returns True or False depending if the stacks is empty or not respectively

            Returns:
                bool: true if stack is empty otherwise false
        """

        return len(self._data) == 0

    def len(self) -> int:
        """ Returns length of the current stack

            Returns:
                int: the length of the current stack (how many elements in the stack)
        """

        return len(self._data)

    
def main():
    my_stack = ListStack()
    my_stack.push(1)
    my_stack.push(5)
    print(f'length of stack is {my_stack.len()}')
    print(f'result after calling top is {my_stack.top()}')
    print(f'result after calling pop is {my_stack.pop()}')
    print(f'length of stack is {my_stack.len()}')
    

if __name__ == "__main__":
    main()

            
        
