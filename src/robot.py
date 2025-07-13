import wpilib
from wpilib import SmartDashboard
from wpimath.geometry import Pose2d
import commands2, rev
import wpilib.drive
from container import RobotContainer


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        self.container = RobotContainer()

        self.field = wpilib.Field2d()
        SmartDashboard.putData("Field", self.field)