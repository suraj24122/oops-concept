# Define a class named 'dog'
class dog:
    # Class attribute: species is common for all dog instances
    species = "German shepard"

    # Constructor method (__init__) to initialize each dog's name and breed
    def __init__(self, name, breed):
        self.name = name  # Instance attribute for dog's name
        self.breed = breed  # Instance attribute for dog's breed

# Create an instance of dog with name "Aana" and breed "Indian"
my_dog = dog("Aana", "Indian")

# Print the name attribute of my_dog
print(my_dog.name)

# Print the breed attribute of my_dog
print(my_dog.breed)
