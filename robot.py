from templates.robot import RobotTemplate
import commands2, wpilib

class Robot(commands2.TimedCommandRobot):
    # INITIALIZATION
    def robotInit(self):
        self.template = RobotTemplate()
        pass

    def autonomousInit(self):
        pass

    def teleopInit(self):
        pass