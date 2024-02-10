from python_trait import Trait, trait_to


class Animal(Trait['Animal']):
    def name(self) -> str:
        raise NotImplementedError

    def noise(self) -> str:
        raise NotImplementedError

    def talk(self):
        print(f"{self.name()} says {self.noise()}.")


as_animal = Animal()


class Person(Trait['Person']):
    def first_name(self) -> str:
        raise NotImplementedError

    def last_name(self) -> str:
        raise NotImplementedError


as_person = Person()


@trait_to(Person)
class ImplAnimal(Animal):
    """All people are also animals"""

    def __init__(self, person: Person):
        self.person = person

    def name(self) -> str:
        return f"{self.person.first_name()} {self.person.last_name()}"

    def noise(self) -> str:
        return "Hello"


class Englishman:
    def __init__(self, first_name: str):
        self.first_name = first_name

    def noise(self) -> str:
        return "Good day to you, sir!"


@trait_to(Englishman)
class ImplPerson(Person):
    def __init__(self, englishman: Englishman):
        self.englishman = englishman

    def first_name(self) -> str:
        return self.englishman.first_name

    def last_name(self) -> str:
        return "Smith"


def test_english_man_talk():
    johnny = Englishman("John")
    person = as_person(johnny)
    as_animal(person).talk()
