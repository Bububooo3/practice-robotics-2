import wpilib
from systems.io.keyboard import KeyboardController


class RobotTemplate:
    def __int__(self):
        self.auto_chooser = wpilib.SendableChooser()
        wpilib.SmartDashboard.putData(self.auto_chooser)

        self.controller = KeyboardController()

    def get_auto(self):
        return self.auto_chooser.getSelected()