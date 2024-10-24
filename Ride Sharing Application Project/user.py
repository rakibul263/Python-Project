from abc import ABC, abstractmethod
from ride import Ride_Matching, Ride_Request

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name: {self.name} and email: {self.email}') 

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print('got the ride, yay', ride)
            self.current_ride = ride

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')

    def accept_ride(self, ride):
        ride.set_driver(self)