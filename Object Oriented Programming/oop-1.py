class SoftwareEngineer:
    # class attribute
    alias = "KeyBoard Magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code ...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name} , age = {self.age}, level = {self.level}, salary = {self.salary}"
    #     return information

    # dunder method
    def __str__(self):
        information = f"name = {self.name} , age = {self.age}, level = {self.level}, salary = {self.salary}"
        return information

# print(SoftwareEngineer.alias)

se1 = SoftwareEngineer("Additya", 24, "SDE", 999)

# print(se1.name, se1.salary)

# print(se1.alias)

se1.code()
se1.code_in_language("Python")


# print(se1.information())

print()