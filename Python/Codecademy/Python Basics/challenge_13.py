class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        DriveBot.count += 1
        self.id = DriveBot.count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot(10, 180, 20)
robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)
DriveBot.all_disabled = True
DriveBot.latitude = -50
DriveBot.longitude = 50

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)