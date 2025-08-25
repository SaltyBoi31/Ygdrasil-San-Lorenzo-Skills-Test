class Account:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class StudentAccount(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.classes = []
        self.is_enlistment_locked = False
        self.is_enlisted = False

    def add_class(self, subject):
        if any(subject.lower() == item.lower() for item in self.classes):
            print("Error: " + subject + " has already been added")
        else:
            self.classes.append(subject)

    def lock_enlistment(self):
        if self.is_enlistment_locked:
            print("Enlistment is already locked")
        else:
            self.is_enlistment_locked = True
            print(self.name + " has locked enlistment")

class AdviserAccount(Account):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.advisees = []
        self.enlisted_advisees = []

    def add_advisee(self, advisee):
        if advisee in self.advisees:
            print("Error: " + advisee.name + " is already an advisee of " + self.name)
        else:
            self.advisees.append(advisee)
            print(self.name + " has added " + advisee.name + " as an advisee.")

    def print_advisees(self):
        print("List of UNENLISTED Advisees for " + self.name)
        for i in list(set(self.advisees) - set(self.enlisted_advisees)):
            print("ID: " + i.id + "   NAME: " + i.name)

        print("List of ENLISTED Advisees for " + self.name)
        for i in self.enlisted_advisees:
            print("ID: " + i.id + "   NAME: " + i.name)

    def lock_enlistment_for(self, advisee):
        if advisee not in self.advisees:
            print("Error: " +advisee.name + " is not an advisee of " + self.name + ".")
        else:
            if not advisee.is_enlistment_locked:
                print("Error: " + advisee.name + "'s enlistment is not locked yet.")
            else:
                print(advisee.name + " is now enlisted.")
                self.enlisted_advisees.append(advisee)
        
student1 = StudentAccount("05524", "Ross")
student1.add_class("Class 1")
student1.add_class("Class 2")
student1.add_class("Class 4")
student1.lock_enlistment()


adviser = AdviserAccount("01341", "Rachel")
adviser.add_advisee(student1)
adviser.lock_enlistment_for(student1)


student2 = StudentAccount("12345", "Chandler")
student2.add_class("Class 1")
student2.add_class("Class 3")


adviser.add_advisee(student2)
adviser.lock_enlistment_for(student2)

student3 = StudentAccount("01353", "Joey")
student3.add_class("Class 5")
student3.add_class("Class 9")


adviser.lock_enlistment_for(student3)

adviser.print_advisees()


