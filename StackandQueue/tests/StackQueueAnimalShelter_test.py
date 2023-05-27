import pytest
from StackAndQueue.StackQueueAnimalShelter import Animal, AnimalShelter


@pytest.fixture
def animal_shelter():
    return AnimalShelter()

def test_enqueue_dog(animal_shelter):
    dog = Animal("dog", "dog1 name")
    animal_shelter.enqueue(dog)
    assert len(animal_shelter.dog_queue) == 1

def test_enqueue_cat(animal_shelter):
    cat = Animal("cat", "cat1 name")
    animal_shelter.enqueue(cat)
    assert len(animal_shelter.cat_queue) == 1

def test_dequeue_dog(animal_shelter):
    dog1 = Animal("dog", "dog1 name")
    dog2 = Animal("dog", "dog2 name")
    animal_shelter.enqueue(dog1)
    animal_shelter.enqueue(dog2)

    dequeued_dog = animal_shelter.dequeue("dog")
    assert dequeued_dog == dog1
    assert len(animal_shelter.dog_queue) == 1

def test_dequeue_cat(animal_shelter):
    cat1 = Animal("cat", "cat1 name")
    cat2 = Animal("cat", "Sasha")
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(cat2)

    dequeued_cat = animal_shelter.dequeue("cat")
    assert dequeued_cat == cat1
    assert len(animal_shelter.cat_queue) == 1

def test_dequeue_invalid_preference(animal_shelter):
    cat = Animal("cat", "cat1 name")
    animal_shelter.enqueue(cat)

    dequeued_invalid = animal_shelter.dequeue("dog")
    assert dequeued_invalid is None

    dequeued_cat = animal_shelter.dequeue("cat")
    assert dequeued_cat == cat
    assert len(animal_shelter.cat_queue) == 0