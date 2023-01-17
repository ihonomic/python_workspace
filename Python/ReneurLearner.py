"""
    #   IMMUTABLE (can't be changed, but allocated a new memory)
    1. None
    2. bool
    3. int
    4. str
    5. tuple
    
    #   MUTABLE (can;t be used as hashable keys in dictionary)
    1. List
    2. set 
    3. dic
    
    # *args, **kwargs
    - *args, recieves positional arguments in a tuple, NOTE: Anything after positional arguments MUST be keyword arguements
    - **kwargs, recieves keyword arguments in a dictionary
    
    # Difference btw List and array
    1. Array accepts only one type of data 
    2. Array length is known
    
    # Similarities btw List and array
    Both are 1-D
    
    # Difference btw list and tuple
    1. Mutate and immutable 
    2. Traditionally, lists are meant to store only 1 type of data, but tuple can hold multiple
    
    # Similarities btw lists and tuples
    1. iterable 
    2. contain anything 
    3. use "in" for search 
    4. both has "count" & "index" methods
    5. index and search with []
    
    # PEP 8 - Python enhancement proposal 
    
    # LOCAL & GLOBAL SCOPES:
    To use a local variable (x) outside a function , 
        use: global x inside the function and then you can call x globally 
        
    # .py and .pyc 
    when modules are imported, python convert the methods to bytes code and makes them easily accessible in 
    subsequents runs. 
    This is what python loads because it is faster 
    
    # EOL - end of line, Syntax Error . If trying to bring a long text into multiple lines 
    
    # Docstrings should follow the convention 
    - Expects:
    - Modifies:
    - Returns : 
    
    # pypi.org - python package index 
    awesome-python.com - website that helps you check trusted modules to install for your projects 
    
    # UnboundLocalError: 
    When the variable is called before definition. Like trying to access a global variable inside a function
    
    #   OOP 
    - Encapsulation: 
        Preventing client from accessing certian properties/ class attributes. Begins with a double underscore 
        self.__price = 0.5
    - Inheritance:
        Inheriting from a main class 
    - Polymorphism:
        This is a greek word meaning: "something that takes on multiple forms"
        Polymorphism refers to a subclass's ability to adapt a method that already exists in its superclass to meet its needs. 
        To put it another way, a subclass can use a method from its superclass as is or modify it as needed
        Usually by calling the super() method. e.g: super().__init__(title, quantity, author, price)
    - Abstraction:
        This is making sure that subclass doesn't make use of the super class method 
        You do this by attaching a decorator: @abstractmethod to the super class method 
        
         @abstractmethod
        def __repr__(self):
            return f"Book: {self.title}"
            
        An error will be thrown if a subclass tries to call this method 
    - Method Overloading and Method Overriding
        Is using multiple methods with the same name. They will be overwritten by the last written method of similar name 
"""


def foo():
    global x
    x = 5


foo()
print(x)
