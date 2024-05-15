from abc import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]
        
    def add_rider(self,rider):
         self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}"

class User(ABC):
    def __init__(self,name,email,nid):

        self.name=name
        self.email=email
        self.__nid=nid
        self.wallet

        #will change letter
        self.__id=0

    @abstractmethod

    def display_profile(self):
        raise NotImplementedError
        

class Rider(User):
    def __init__(self, name, email, nid,current_location,initial_amount):
        self.current_ride=None
        self.current_location=current_location
        self.wallet=initial_amount
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Rider:\n NAME:{self.name}, EMAIL: {self.email}")

    def load_cash(self,amount):
        if amount>=0:
            self.wallet+=amount

    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            ride_request=Ride_Request(self,destination)
            ride_matcher=Ride_Matching(ride_sharing.drivers)
            self.current_ride=ride_matcher.find_driver(ride_request)

    def update_location(self,current_location):
        self.current_location=current_location

    def show_current_ride(self):
        print(self.current_ride)
        
class Driver(User):
    def __init__(self, name, email, nid,current_location,initial_amount):
        self.current_location=current_location
        self.wallet=initial_amount
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Driver:\n Name: {self.name}, Email: {self.email}")

    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fair=None


    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self,amount):
        self.end_time=datetime.now()
        self.rider.wallet-=self.estimated_fair
        self.driver.wallet+=self.estimated_fair
    
    def __repr__(self) -> str:
        return f'Started Ride From {self.start_location} To {self.end_location}'


class Ride_Request:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location


class Ride_Matching:
    def __init__(self,drivers):
        self.available_drivers=drivers


    def find_driver(self,ride_request):
        if len(self.available_drivers)>0:
            driver=self.available_drivers[0]
            ride=Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):

    {
        "car": 50,
        "bike": 60,
        "cng": 15
    }

    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        self.status="available"
        super().__init__()  

        @abstractmethod
        def start_drive(self):
            pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

        def start_drive(self):
            self.status="unavailable"

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

        def start_drive(self):
            self.status="unavailable"
        
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

        def start_drive(self):
            self.status="unavailable"





#check the class integration


niye_jao=Ride_Sharing("Niye Jao")

sakib=Rider("Sakib Khan", "sakib.khan@gmail.com",12453, "Mohakhali", 1200)
niye_jao.add_rider(sakib)
sakib.display_profile()

Rakib=Driver("Rakib Hassan", "rakib.hassan@gmail.com", 13245, "Golshan-1", 200)
niye_jao.add_driver(Rakib)
print(niye_jao)
sakib.request_ride(niye_jao,"Uttara")
sakib.show_current_ride()