# Define the parent class 'animal'
class animal:
    # Constructor (__init__) to initialize the 'name' attribute
    def __init__(self, name):
        self.name = name

    # Generic 'speak' method for any animal
    def speak(self):
        print("Generic animal sound")

# Define the 'dog' class that inherits from 'animal'
class dog(animal):
    # Override the 'speak' method specifically for dogs
    def speak(self):
        print("The dogs speak Woof !!!") 

# Define the 'cat' class that inherits from 'animal'
class cat(animal):
    # Override the 'speak' method specifically for cats
    def speak(self):
        print("The cat meows !!!")

# --- Creating objects ---

# Create a 'dog' object with name "Scooby"
first_dog = dog("Scooby")

# Create a 'cat' object with name "Marie"
first_cat = cat("Marie")

# Print the name of the dog
print("My dog name is = ", first_dog.name)

# Print the name of the cat
print("My cat name is = ", first_cat.name)

# Call the 'speak' method for the cat (calls overridden method)
first_cat.speak()

# Call the 'speak' method for the dog (calls overridden method)
first_dog.speak()

