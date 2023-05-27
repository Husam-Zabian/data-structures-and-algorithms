class Animal:
    def __init__(self, species, name):
        """
        Initializes an empty Animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        """
        Initializes an empty AnimalShelter.
        """
        self.dog_queue = []
        self.cat_queue = []

    def __str__(self):
        """
        returns a string representation of the class AnimalShelter
        """
        return f"AnimalShelter(dog_queue={self.dog_queue}, cat_queue={self.cat_queue})"

    def enqueue(self, animal):
        """
        add animal value to the end of list.
        """
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        """
        Removes and returns the value of the front list.
        """
        if pref == "dog":
            if len(self.dog_queue) > 0:
                return self.dog_queue.pop(0)
        elif pref == "cat":
            if len(self.cat_queue) > 0:
                return self.cat_queue.pop(0)
        return None