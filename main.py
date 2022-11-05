
def describe_pet(animal_type, pet_name):
    # Information about pet_name
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s is {pet_name.title()}.")
    
# describe_pet("cat", "vasya")
describe_pet("cat", "semen")
print("I love my pet")
print("Whatever happens,\nall my pets are always with me.")

# Transition to a branch test
def test_count_quantity(kittens, puppies):
    quantity = kittens + puppies
    print(quantity)

test_count_quantity(3,3)
print("It is a joke.")
