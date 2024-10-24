from ride import Ride, Ride_Request, Ride_Matching, Ride_Sharing
from user import Rider, Driver
from vehicle import Vehicle, car, bike

GoShare = Ride_Sharing('Niye Jao')
Shuvo = Rider("Shuvo", 'rakibulhasanshuvo206@gmail.com', 48252345627, 'Mirpur', 1200)
GoShare.add_rider(Shuvo)
Rohim = Driver('Rohim', 'kala@sada.com', 56489582734, 'Gaibandha')
GoShare.add_driver(Rohim)
print(GoShare)
Shuvo.request_ride(GoShare, 'uttara')
Shuvo.show_current_ride()
