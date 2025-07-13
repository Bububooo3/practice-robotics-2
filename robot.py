import wpilib
from wpilib import SmartDashboard
from wpimath.geometry import Pose2d
import commands2, rev
import wpilib.drive


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        left_drive, right_drive = wpilib.PWMSparkMax(0), wpilib.PWMSparkMax(1)

        self.field = wpilib.Field2d()
        SmartDashboard.putData("Field", self.field)

        self.drive = wpilib.drive.DifferentialDrive(left_drive, right_drive)
        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())