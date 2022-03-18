from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
        return System.register_software(hardware_name, sw)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        sw = LightSoftware(name, capacity_consumption, memory_consumption)
        return System.register_software(hardware_name, sw)

    @staticmethod
    def register_software(hardware_name, software_instance):
        hw = next((hw for hw in System._hardware if hw.name == hardware_name), None)
        if hw is None:
            return "Hardware does not exist"
        hw.install(software_instance)
        System._software.append(software_instance)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hw = next((hw for hw in System._hardware if hw.name == hardware_name), None)
        sw = next((sw for sw in System._software if sw.name == software_name), None)
        if hw and sw:
            hw.uninstall(sw)
            System._software.remove(sw)
            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        mem_consumption = sum(sw.memory_consumption for sw in System._software)
        mem_capacity = sum(hw.memory for hw in System._hardware)
        space_consumption = sum(sw.capacity_consumption for sw in System._software)
        space_capacity = sum(hw.capacity for hw in System._hardware)
        retval = "System Analysis"
        retval += f'\nHardware Components: {len(System._hardware)}'
        retval += f'\nSoftware Components: {len(System._software)}'
        retval += f'\nTotal Operational Memory: {mem_consumption} / {mem_capacity}'
        retval += f'\nTotal Capacity Taken: {space_consumption} / {space_capacity}'
        return retval

    @staticmethod
    def system_split():
        retval = ''
        for hw in System._hardware:
            retval += hw.analyze() + '\n'
        return retval
