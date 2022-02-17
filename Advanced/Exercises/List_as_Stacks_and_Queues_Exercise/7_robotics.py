# Somewhere in the future, there is a robotics factory. The current project is assembly line robots.
# Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free it should take a product for processing and log his name, product and processing start time.
# Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
# The robots are standing on the line in the order of their appearance.
# Input
# •	On the first line, you will receive the names of the robots and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
# •	On the second line, you will get the starting time in format "hh:mm:ss"
# •	Next, until the "End" command, you will get a product on each line.
# Output 
# •	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"



from collections import deque
import datetime as dt

processing_queue = deque()
robots = []

class Robot:
    def __init__(self, name: str, work_time: int) -> None:
        self.name = name
        self.available = True
        self.queue = []
        self.work_time = work_time

    def start(self, product: str) -> None:
        self.available = False
        self.queue.append(product)
        self.starttime = current_time
        start_time = current_time.strftime("%H:%M:%S")
        print(f"{self.name} - {self.queue[0]} [{start_time}]")

    def update(self):
        global current_time
        if not self.available and (current_time - self.starttime).total_seconds() >= self.work_time:
            self.queue.clear()
            self.available = True
    
    def __repr__(self) -> str:
        return f'Robot({self.name},{self.work_time})'


input_data = input().split(';')
for data in input_data:
    robot_name, work_time = data.split('-')
    robots.append(Robot(robot_name, int(work_time)))

current_time = dt.datetime.strptime(input(), '%H:%M:%S')

while True:
    product = input() 
    if product == 'End':
        break
    processing_queue.appendleft(product)

while processing_queue:
    current_time += dt.timedelta(seconds=1)
    product_pass = True
    for robot in robots:
        robot.update()
        if robot.available:
            robot.start(processing_queue.pop())
            product_pass = False
            break
    if product_pass:
        processing_queue.rotate(1)