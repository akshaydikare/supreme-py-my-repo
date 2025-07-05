# Single Inheritance
class Dog:
    def __init__(self, name):
        """
        Initialize the object with a name.

        Args:
            name (str): The name to assign to the object.
        """
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name} from Dog class")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs loudly! Woof Woof! from Labrador class")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name} Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

#==========================================================================
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dogg(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method
    
#==========================================================================
# A Python program to demonstrate inheritance
class Person(object):
  
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)


# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

class Emp(Person):
  
  def Print(self):
    print("Emp class called")
    
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()

#==========================================================================

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

#==============================================================================


# Creating an instance of Dog
dogg = Dogg("Buddy the Dog")
print(dogg.speak())