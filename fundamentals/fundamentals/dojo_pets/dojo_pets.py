import ninja_class
import pets_class

person_1 = ninja_class.Ninja('test', 'test', pets_class.Pet('puppy','dog','sit'), 'bone', 'kibble')

person_1.feed().walk().bathe()

person_2 = ninja_class.Ninja('test 2', 'test 2', pets_class.Dog('doggo', 'roll over'), 'human food', 'anything')
print(person_2.pet.type)
person_2.feed().walk().bathe()
