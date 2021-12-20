class Vehicle:
    def __init__(self):
        self.fuel = 'diesel'
        self.type = 'Small'


class Cars(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.color = 'grey'
        self.convertible = False
        self.tires = 'Large'
        self.orientation = 'Left'
        self.weight = 3000
        self.drive_requirement = 0

    def Volkswagon(self):
        self.color = 'green'
        self.drive_requirement = 100
        return self.color
    
    def Isuzu(self):
        self.weight = 8000
        self.type = 'Large'
        self.drive_requirement = 450
    
    def Lamborghini(self):
        señf.color = 'Yellow'
        self.tires = 'Small'
        self.orientation = 'Right'
        self.weight = 700
        self.drive_requirement = 700

    def Maseratti(self):
        self.convertible = True
        self.weight = 680
        self.type = 'Small'
        self.tires = 'Small'
        self.orientation = 'Right'
        self.drive_requirement = 1000


class Driver(Cars):
    def __init__(self):
        Cars.__init__(self)
        self.__driver_name = 'Muriithi Gakuru'
        self.skill = 'Intermediate'
        self.experience = 3
        self.location = 'Bomet'
        self.rating = 3.8

    def print_details(self):
        ''' 
        This is the doctype for this method. Just declares what this method is supposed to do. I do not know what it's supposed to do either.
        '''
        return self.__driver_name ,f'Skill-{self.skill}'  ,f'Experience-{self.experience}' ,f'Location-{self.location}' , f'rating-{self.rating}' 

class Drive(Driver):
    def __init__(self):
        Driver.__init__(self)
        self.can_drive = False

    def select_car(self):
        cars = '''
                1. Volkswagon
                2. Isuzu
                3. Lamborghini
                4. Maseratti
        '''
        selection = 0
        choice = int(input('Choose your car sir..'))
        return choice

    def drive(self):
        if select_car(self) == 1:
            return Volkswagon()
        # if self.drive_requirement > 100:
        #     return 'I can drive you'
        # return self.drive_requirement

obj = Driver()
for i in obj.print_details():
    print(i)

obj1 = Drive()
print(obj1.select_car())
