# Define a class named 'dog'
class dog:
    # Class attribute: shared by all instances of the class
    species = "Lab"

    # Constructor method to initialize each new dog's name and breed
    def __init__(self, name, breed):
        self.name = name  # Instance attribute for dog's name
        self.breed = breed  # Instance attribute for dog's breed

    # Method for dog to "bark"
    def bark(self):
        print(f"{self.name} says WOOF !!!")  # Print a message with the dog's name

# Create an instance of dog with name "Scooby" and breed "Sitzu"
my_dog = dog("Scooby", "Sitzu")

# Create another instance of dog with name "Bruno" and breed "Street Dog"
another_dog = dog("Bruno", "Street Dog")

# Print the object reference (default will show object type and memory address)
print(my_dog)

# Print the second object reference (also shows object type and memory address)
print(another_dog)

# Print the name of my_dog ("Scooby")
print(my_dog.name)

# Print the breed of another_dog ("Street Dog")
print(another_dog.breed)

# Call the bark() method for my_dog (Scooby will "bark")
print(my_dog.bark())  # Note: bark() already prints, so this will print "None" after bark because bark() returns nothing.

# Print the species of another_dog (which is "Lab" from class attribute)
print(another_dog.species)
