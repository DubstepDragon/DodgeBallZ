import pygame

pygame.joystick.init()


class Controller:
    def __init__(self):
        """init for overall controller"""
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            pygame.joystick.Joystick(i).init()

    @property
    def get_id(self):
        """get controller id for current controller"""
        x = []
        for c in self.joysticks:
            x.append(c.get_id())
        return x

    @property
    def play_connected(self):
        """check to see if controller is connected"""
        x = pygame.joystick.get_count()
        for i in range(pygame.joystick.get_count()):
            if pygame.joystick.Joystick(i).get_numbuttons() == 14:
                if x >= 1:
                    return True
                else:
                    return False

    @property
    def xbox_connected(self):
        """check to see if xbox controller connected"""
        x = pygame.joystick.get_count()
        for i in range(pygame.joystick.get_count()):
            if pygame.joystick.Joystick(i).get_numbuttons() == 10:
                if x >= 1:
                    return True
                else:
                    return False


class Xbox_Controller(Controller):
    def __init__(self, cont_num):
        """init joystick and add joystick to a list"""
        super().__init__()
        self.joystick = self.joysticks[cont_num]

    @property
    def NUMBUTTONS_xbox(self):
        """Returns number of buttons on xbox controller (should return 10)"""
        x = self.joystick.get_numbuttons()
        return x

    @property
    def axis_LEFT_STICK(self):
        """return left stick axis as tuple"""
        x = self.joystick.get_axis(0)
        y = self.joystick.get_axis(1)
        return (x, y)

    @property
    def axis_RIGHT_STICK(self):
        """return right stick axis as tuple"""
        x = self.joystick.get_axis(3)
        y = self.joystick.get_axis(4)
        return (x, y)

    @property
    def button_A(self):
        """get state of button_A in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(0)
        return x

    @property
    def button_B(self):
        """get state of button_B in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(1)
        return x

    @property
    def button_X(self):
        """get state of button_X in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(2)
        return x

    @property
    def button_Y(self):
        """get state of button_Y in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(3)
        return x

    @property
    def button_LB(self):
        """get state of left bumper in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(4)
        return x

    @property
    def button_RB(self):
        """get state of right bumper in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(5)
        return x

    @property
    def button_SELECT(self):
        """get state of button_SELECT in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(6)
        return x

    @property
    def button_START(self):
        """get state of button_START in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(7)
        return x

    @property
    def button_STICK_LEFT(self):
        """get state of left_stick_button in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(8)
        return x

    @property
    def button_STICK_RIGHT(self):
        """get state of right_stick_button in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(9)
        return x

    @property
    def dpad_UP(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[1] == 1:
            return True
        else:
            return False

    @property
    def dpad_DOWN(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[1] == -1:
            return True
        else:
            return False

    @property
    def dpad_LEFT(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[0] == -1:
            return True
        else:
            return False

    @property
    def dpad_RIGHT(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[0] == 1:
            return True
        else:
            return False

    @property
    def axis_TRIGGER_LEFT(self):
        """Return axis for left trigger if pressed if not return false"""
        left = self.joystick.get_axis(2)
        if left > 0.01:
            return left
        else:
            return False

    @property
    def axis_TRIGGER_RIGHT(self):
        """Return axis for right trigger if pressed if not return false"""
        right = self.joystick.get_axis(2)
        if right < -0.01:
            return right
        else:
            return False


# ==========================================================================================================
# ==========================================================================================================


class Playstation_Controller(Controller):
    def __init__(self, cont_num):
        """init joystick and add joystick to a list"""
        super().__init__()
        self.joystick = self.joysticks[cont_num]

    @property
    def NUMBUTTONS_playstation(self):
        """Returns number of buttons on playstation controller (should return 14)"""
        x = self.joystick.get_numbuttons()
        return x

    @property
    def axis_STICK_LEFT(self):
        """return left_stick as tuple"""
        x = self.joystick.get_axis(0)
        y = self.joystick.get_axis(1)
        return (x, y)

    @property
    def axis_STICK_RIGHT(self):
        """return right_stick as tuple"""
        x = self.joystick.get_axis(2)
        y = self.joystick.get_axis(3)
        return (x, y)

    @property
    def button_SQUARE(self):
        """get state of button_0 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(0)
        return x

    @property
    def button_X(self):
        """get state of button_1 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(1)
        return x

    @property
    def button_CIRCLE(self):
        """get state of button_2 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(2)
        return x

    @property
    def button_TRIANGLE(self):
        """get state of button_3 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(3)
        return x

    @property
    def button_L1(self):
        """get state of bumper_L1 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(4)
        return x

    @property
    def button_R1(self):
        """get state of bumper_R1 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(5)
        return x

    @property
    def button_L2(self):
        """get state of trigger_L2 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(6)
        return x

    @property
    def axis_L2(self):
        """get axis for trigger_L2 and read back value range from -1 (unpressed) to 1 (pressed)"""
        x = self.joystick.get_axis(5)
        return x

    @property
    def button_R2(self):
        """get state of trigger_R2 in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(7)
        return x

    @property
    def axis_R2(self):
        """get axis for trigger_R2 and return value on range -1 (unpressed) to 1 (pressed)"""
        x = self.joystick.get_axis(4)
        return x

    @property
    def button_SHARE(self):
        """get state of button_SHARE in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(8)
        return x

    @property
    def button_OPTIONS(self):
        """get state of button_OPTIONS in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(9)
        return x

    @property
    def button_STICK_LEFT(self):
        """get state of left_stick_button in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(10)
        return x

    @property
    def button_STICK_RIGHT(self):
        """get state of right_stick_button in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(11)
        return x

    @property
    def button_PLAYSTATION_HOME(self):
        """get state of button_PLAYSTATION_HOME in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(12)
        return x

    @property
    def button_TOUCHPAD(self):
        """get state of button_PLAYSTATION_HOME in 0 or 1: 0 is not pressed, 1 is pressed"""
        x = self.joystick.get_button(13)
        return x

    @property
    def dpad_UP(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[1] == 1:
            return True
        else:
            return False

    @property
    def dpad_DOWN(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[1] == -1:
            return True
        else:
            return False

    @property
    def dpad_LEFT(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[0] == -1:
            return True
        else:
            return False

    @property
    def dpad_RIGHT(self):
        """check state of d_pad_up, return true if pressed"""
        hat = self.joystick.get_hat(0)
        if hat[0] == 1:
            return True
        else:
            return False
