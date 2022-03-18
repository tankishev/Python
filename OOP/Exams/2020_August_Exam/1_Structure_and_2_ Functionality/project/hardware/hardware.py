from project.software.express_software import ExpressSoftware


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int) -> None:
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def used_memory(self):
        return sum(sw.memory_consumption for sw in self.software_components)

    @property
    def used_capacity(self):
        return sum(sw.capacity_consumption for sw in self.software_components)

    def install(self, software) -> None:
        free_memory = self.memory - self.used_memory
        free_capacity = self.capacity - self.used_capacity
        if software.memory_consumption <= free_memory and software.capacity_consumption <= free_capacity:
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software) -> None:
        sft = next((sft for sft in self.software_components if sft.name == software.name), None)
        if sft:
            self.software_components.remove(sft)

    def analyze(self):
        express_sw_num = len([sw for sw in self.software_components if isinstance(sw, ExpressSoftware)])
        light_sw_num = len(self.software_components) - express_sw_num

        retval = f"Hardware Component - {self.name}"
        retval += f'\nExpress Software Components: {express_sw_num}'
        retval += f'\nLight Software Components: {light_sw_num}'
        retval += f'\nMemory Usage: {self.used_memory} / {self.memory}'
        retval += f'\nCapacity Usage: {self.used_capacity} / {self.capacity}'
        retval += f'\nType: {self.hardware_type}'
        retval += f'\nSoftware Components: {self.list_software_components()}'
        return retval

    def list_software_components(self):
        if self.software_components:
            return f"{', '.join([sw.name for sw in self.software_components])}"
        return 'None'
