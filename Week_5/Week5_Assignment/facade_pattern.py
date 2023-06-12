""" Provides a unified interface to a set of interfaces in a subsystem. It makes the subsystem easier to use.
(Source 'Head First - Design Patterns', p.266) """


class DrivingFacade:
    def __init__(self, start_engine, engage_gears, press_gas_pedal, apply_breaks):  #
        """
        Facade interfaces to the drving subsystem
        own.
        """
        self._start_engine = start_engine
        self._engage_gears = engage_gears
        self._press_gas = press_gas_pedal
        self._apply_brakes = apply_breaks

    def driving(self):
        """ Facade driving method that calls the subsystem functions """

        print('Facade orders system to start driving')
        print(self._start_engine.start_engine())
        print(self._engage_gears.engage_drive())
        print(self._press_gas.press_gas_pedal())
        print('the vehicle is going')
        print('\nFacade orders system to stop driving')
        print(self._press_gas.stop_pressing_gas_pedal())
        print(self._apply_brakes.apply_brakes())
        print(self._apply_brakes.vehicle_stops())
        print(self._start_engine.engine_running())
        print('the vehicle is not going')
        # return "\n".join(driving)


class StartEngineSubsystem:
    """ Start Engine """

    def start_engine(self):
        return 'engine has started'

    def engine_running(self):
        return 'engine is running'


class EngageGearSubsystem:

    def engage_drive(self):
        return 'vehicle is in drive'

    def engage_reverse(self):
        return 'vehicle is in reverse'


class PressGasPedalSubsystem:

    def press_gas_pedal(self):
        return 'gas pedal is being pressed'

    def stop_pressing_gas_pedal(self):
        return 'gas pedal disengaged'


class ApplyBreaksSubsystem:

    def apply_brakes(self):
        return 'breaks have been applied'

    def vehicle_stops(self):
        return 'vehicle is stopped'


def client(facade):
    facade.driving()


# class PressGasPedalSubsystem:
#

if __name__ == "__main__":

    start = StartEngineSubsystem()
    engage = EngageGearSubsystem()
    gas = PressGasPedalSubsystem()
    brake = ApplyBreaksSubsystem()
    facade = DrivingFacade(start, engage, gas, brake)
    client(facade)
