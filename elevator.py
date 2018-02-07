
from abc import ABC, abstractmethod

FLOORS = 10
ELEVATORS = 1
MAX_PEOPLE = 5
MIN_FLOOR = -1
MAX_FLOOR = FLOORS + 1

ZERO = 0
UP = 1
DOWN = 2

class DIRECTION:
    ZERO = 0
    UP = 1
    DOWN = 2


def Request:
    self.request_type
    self.request_button
    self.elevator
    
class ElevatorEventListener(ABC):
    @abstractmethod
    def onStopped(sender):
        pass

class Flore:
    def __init__(self, flore_id):
        self.flore_id = flore_id 
        self.button = Button()
        self.eventlistner = None

class Button:
    self __init__(self):
        self.up = False
        self.down = False

class Elevator:
    def __init__(self, numFloors):
        self.direction = DIRECTION.ZERO
        self.min_flore = MIN_FLOOR
        self.max_flore = MAX_FLOOR

        self.cf = ZERO
        self.numFloors = numFloors
        self.flore_button = {}
        i = 0
        while i <  0:
            self.flore = Flore(i)
            self.flore_button[i] = self.flore
            i = i + 1
    
    def get_current_floor(self):
        return self.cf

    def moveNext(self, direction, flore_id):
        if direction == DIRECTION.UP:
            self.cf = self.cf + 1
            self.move_to_floor(self.cf)
            elEventListener = self.Flore[self.cf].eventlistner
            if elEventListener != None and self.Flore[self.cf].UP == True:
                elEventListener.onStopped()

        elif direction == DIRECTION.DOWN:
            self.cf = self.cf - 1
            elEventListener = self.Flore[self.cf].eventlistner
            if elEventListener != None and self.Flore[self.cf].DOWN == True:
                elEventListener.onStopped()

    def move_to_floor(self, gf):
        if gf < 0 or gf >= self.numFloors:
            return
        
        if self.cf == self.gf:
            return
       

        if gf > self.cf: 
            self.max_flore = max(self.max_flore, gf)
        if gf < self.cf:
            self.min_flore = max(self.min_flore, gf)

        if gf > self.cf:
            self.direction = DIRECTION.UP
        elif gf < self.cf:
            self.direction = DIRECTION.DOWN
        else:
            self.direction = DIRECTION.ZERO


     def reset(self): 
         self.cf= 0
         self.direction = DIRECTION.NONE
         self.max_flore = MAX_FLOOR
         self.min_flore = MIN_FLOOR

     def getDirection(self):
         return self.direction

     def pickup(self, floor,direction):
         self.move_to_flore(flore, direction)

class ElevatorController(ElevatorEventListener):
    def __init__(self):
        self.numElevators = ELEVATORS 
        self.numFloors = FLOORS
        self.passengers = []
        self.sensors = Sensors()
        self.priorty_queue = Queue()
        self.elevator = Elevator()
        

    def calculate_direction(self, source, destination, elevatorid):
        # Calculate the Direction on the basis of elevator current flore and next request
        # Also what is the current move
        
        return self.direction

    def update(self, elevatorId , floor):
        el.move_to_flore(floor)

    def move_next(self, elevator):
        elevator.moveNext()

    def onStopped(self, sender):
        sender.move_to_floor(gf)

    def register_request(self, elevator, Flore, request_type):
        self.priorty_queue.put(elevator, request_type, Flore)

    def genearate_alarm(self, request_type):
        self.sensors.notify()

    def process_request(self, request):

        while worker_queue():
        elevator = request.elevator
        flore_number = request.flore
        if elevator.move == True:
            flore = Flore[flore_number]
            flore.setEventListner()
            flore.button.UP = True if request.button.up else False
            flore.button.DOWN = True if request.button.DOWN else False
            elevator.direction = request.direction
        elevator.moveNext(Flore.flore_number)
        
    def worker_thread(self, priorty_queue):
        # Process the Request on the basis of elevatorID
        # Direction
        # Flore Request Number         
        while True:
            request = priorty_queue.get()
            worker_queue(request)
            
    def RequestHandler(self, request):
        elevator = self.request.elevator
        flore_number = self.request.flore_number
        self.request_type = self.request.request_type

        if self.request.type == "Move":
            self.register_request(request_type, floor_number)

        if self.request.type == "GateOpen":
            self.register_request(request_type, floor_number)

        if self.request_type == "Sensors":
            self.genrate_alarm(self.request_type)

        if self.request_type == "Stopped":
            elevator.eventListner = "Stopped"
            self.onStopped(elevator)

 
class Sensors(ABC):
    def __init__(self):
        self.alarm = AlarmFactory()

    @abstractmethod
    def set_alarm(self):
        pass

    @abstractmethod
    def detect_sensor(self)
        pass

def FireSensor(Sensors):
    
    def detect_sensor(self):
        self.alarm.notify("Fire")

def AlarmFactory():
    def __init__(self, alarm_type):
        if alarm_type == "Fire":
            return FireAlarm()

class Alarm(ABC):
    
    @abstractmethod
    def notify(self):
        pass

class FireAlarm(Alarm):
    def notify(self):
        print "Fire Alarm"
   

class SmokeAlarm(Alarm):
    def notify(self):
        print "Smoke Alarm"


class OverWeightAlarm(Alarm)
    def notify(self):
        print "Over Weight Alarm"


