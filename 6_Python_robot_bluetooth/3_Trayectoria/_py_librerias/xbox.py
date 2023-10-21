from inputs import get_gamepad
import math
import threading

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.xDPad = 0
        self.yDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def stop(self):
        self._monitor_thread._stop()

    def read(self): # return the buttons/triggers that you care about in this methode
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        a = self.A
        b = self.X # b=1, x=2
        rb = self.RightBumper
        return [x, y, a, b, rb]
    
    def read_abxy(self): # return the buttons/triggers that you care about in this methode
        a = self.A
        b = self.B 
        x = self.X
        y = self.Y
        rb = self.RightBumper 
        return [a, b, x, y, rb]
    
    def read_abxy_joystick(self): # return the buttons/triggers that you care about in this methode
        a = self.A
        b = self.B 
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        rb = self.RightBumper 
        return [a, b, x, y, rb]
    
    def read_control1_abxy(self): # return the buttons/triggers that you care about in this methode
        a = self.A
        b = self.B 
        x = self.X
        y = self.Y
        rb = self.RightBumper 
        return [a, b, x, y, rb]
    
    def read_control2_joystick_right(self): # return the buttons/triggers that you care about in this methode
        x = self.RightJoystickX
        y = self.RightJoystickY
        rb = self.RightBumper 
        return [ x, y, rb]
    
    def read_control3_PAD_Left(self): # return the buttons/triggers that you care about in this methode
        x = self.xDPad
        y = self.yDPad
        rb = self.RightBumper 
        return [x, y, rb]
    
    def read_control4_joystick_Left(self): # return the buttons/triggers that you care about in this methode
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        rb = self.RightBumper 
        return [ x, y, rb]
    
    def read_lb(self): # return the buttons/triggers that you care about in this methode
        lb = self.LeftBumper
        return lb


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'ABS_HAT0X':
                    self.xDPad = event.state
                elif event.code == 'ABS_HAT0Y':
                    self.yDPad = event.state

# if __name__ == '__main__':
#     joy = XboxController()
#     while True:
#         print(joy.read_control3_PAD_Left())