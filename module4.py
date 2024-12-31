class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self):
              print(f"{self.owner} is the owner of this car")

            
Vehicle1 = Vehicle("2345", "honda", "Matthew")
vehicle2 = Vehicle("5566", "Ford", "Travis")

Vehicle1.update_owner()
vehicle2.update_owner()


class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date

        def add_participant(self):
              print(f"adding {self.name} participants!")
        
        def get_participant_count(self):   
            print(f"there are {self.name} people at the event")

adding_people = Event(20,2024)
counting_people = Event(20,2024)
adding_people.add_participant()
counting_people.get_participant_count()

        
    