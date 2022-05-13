class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, _hours: int, _minutes: int, _seconds: int) -> None:
        self.hours = _hours
        self.minutes = _minutes
        self.seconds = _seconds

    def set_time(self, _hours: int, _minutes: int, _seconds: int):
        self.hours = _hours
        self.minutes = _minutes
        self.seconds = _seconds

    def get_time(self):  # needs 0s
        if self.hours < 10 and self.minutes < 10 and self.seconds < 10:
            return f"0{self.hours}:0{self.minutes}:0{self.seconds}"
        elif self.minutes < 10 and self.seconds < 10:
            return f"{self.hours}:0{self.minutes}:0{self.seconds}"
        elif self.hours < 10 and self.minutes < 10:
            return f"{self.hours}:0{self.minutes}:0{self.seconds}"
        elif self.hours < 10 and self.seconds < 10:
            return f"0{self.hours}:{self.minutes}:0{self.seconds}"
        elif self.seconds < 10:
            return f"{self.hours}:{self.minutes}:0{self.seconds}"
        elif self.hours < 10:
            return f"0{self.hours}:{self.minutes}:{self.seconds}"
        elif self.minutes < 10:
            return f"{self.hours}:0{self.minutes}:{self.seconds}"
        else:
            return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        if (
            self.seconds == Time.max_seconds
            and self.minutes == Time.max_minutes
            and self.hours == Time.max_hours
        ):
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif (
            self.seconds == Time.max_seconds
            and self.minutes == Time.max_minutes
        ):
            self.hours += 1
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == Time.max_seconds:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
