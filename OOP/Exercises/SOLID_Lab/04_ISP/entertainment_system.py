from abc import ABC, abstractmethod


class ConnectionInterface(ABC):
    """
    Abstract base class defining connection interfaces. Each interface has a port_type (e.g. HDMI, RCA, ETH),
    a connected status (True/ False) and tracks connected device (except for 'power' interface where device
    is always None.
    """

    @abstractmethod
    def __init__(self, port_type):
        self.port_type = port_type
        self._connected = False
        self._connected_device = None

    @property
    def connected(self):
        return self._connected

    @property
    def connected_device(self):
        return self._connected_device

    def connect(self, device):
        self._connected = True
        self._connected_device = device

    def disconnect(self):
        self._connected = False
        self._connected_device = None


class HDMIPort(ConnectionInterface):
    def __init__(self):
        super().__init__('HDMI')


class EthernetPort(ConnectionInterface):
    def __init__(self):
        super().__init__('ETH')


class PowerPort(ConnectionInterface):
    def __init__(self):
        super().__init__('power')


class RCAPort(ConnectionInterface):
    def __init__(self):
        super().__init__('RCA')


class EntertainmentDevice(ABC):
    """
    Abstract base class for an entertainment device. To be connectable each device must have a list of interface ports.
    Use set_ports() method to set the list of available ports in each child object.
    """

    def __init__(self):
        self.ports = self.set_ports()

    @abstractmethod
    def set_ports(self):
        pass

    def plug_in_power(self):
        if 'power' not in [p.port_type for p in self.ports]:
            return f'{self.__class__.__name__} does not have a free "power" port.'

        free_port = self.__find_available_port_by_type('power')
        if free_port and not free_port.connected:
            free_port.connect(None)
            return f'{self.__class__.__name__} connected to power outlet.'
        return f'{self.__class__.__name__} already connected to power outlet.'

    def _connect_to_device_via_port(self, device, port_type: str):
        if any(p.connected_device == device for p in self.ports):
            return f'{self.__class__.__name__} already connected to {device.__class__.__name__}.'

        free_port = self.__find_available_port_by_type(port_type)
        if free_port:
            free_port.connect(device)
            return f'{self.__class__.__name__} {port_type} port connected to {device.__class__.__name__}.'
        return f'{self.__class__.__name__} does not have a free {port_type} port.'

    def __find_available_port_by_type(self, port_type):
        try:
            return next(p for p in self.ports if p.port_type == port_type and not p.connected)
        except StopIteration:
            return None


class Television(EntertainmentDevice):

    def __init__(self):
        super().__init__()

    def set_ports(self):
        return [HDMIPort(), RCAPort(), PowerPort(), EthernetPort()]

    def connect_to_dvd(self, dvd_player):
        return self._connect_to_device_via_port(dvd_player, 'RCA')

    def connect_to_game_console(self, game_console):
        return self._connect_to_device_via_port(game_console, 'HDMI')

    def connect_to_router(self, router):
        return self._connect_to_device_via_port(router, 'ETH')


class DVDPlayer(EntertainmentDevice):

    def __init__(self):
        super().__init__()

    def set_ports(self):
        return [RCAPort(), PowerPort()]

    def connect_to_tv(self, television):
        return self._connect_to_device_via_port(television, 'RCA')


class GameConsole(EntertainmentDevice):

    def __init__(self):
        super().__init__()

    def set_ports(self):
        return [HDMIPort(), RCAPort(), PowerPort(), EthernetPort()]

    def connect_to_tv(self, television):
        return self._connect_to_device_via_port(television, 'HDMI')

    def connect_to_router(self, router):
        return self._connect_to_device_via_port(router, 'ETH')


class Router(EntertainmentDevice):

    def __init__(self):
        super().__init__()

    def set_ports(self):
        return [EthernetPort(), EthernetPort(), PowerPort()]

    def connect_to_tv(self, television):
        return self._connect_to_device_via_port(television, 'ETH')

    def connect_to_game_console(self, game_console):
        return self._connect_to_device_via_port(game_console, 'ETH')


if __name__ == '__main__':
    t = Television()
    dvd = DVDPlayer()
    r = Router()
    game = GameConsole()
    game2 = GameConsole()

    print(t.connect_to_router(r))
    print(t.connect_to_router(r))
    print(r.connect_to_tv(t))
    print(game.connect_to_router(r))
    print(r.connect_to_game_console(game))

    print(t.connect_to_dvd(dvd))
    print(dvd.connect_to_tv(t))

    print(t.connect_to_game_console(game))
    print(game.connect_to_tv(t))

    print(t.plug_in_power())
    print(game.plug_in_power())
    print(dvd.plug_in_power())
    print(r.plug_in_power())

