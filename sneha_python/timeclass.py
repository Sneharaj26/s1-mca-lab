class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def __add__(self, other):
        # Calculate total seconds for both time instances
        total_seconds = (self.__hour * 3600 + self.__minute * 60 + self.__second) + \
                        (other.__hour * 3600 + other.__minute * 60 + other.__second)

        # Convert total seconds back to hours, minutes, and seconds
        new_hour = total_seconds // 3600
        total_seconds %= 3600
        new_minute = total_seconds // 60
        new_second = total_seconds % 60

        return Time(new_hour, new_minute, new_second)

    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

# Example usage:
time1 = Time(2, 30, 45)
time2 = Time(1, 15, 20)

sum_time = time1 + time2

print(f"Time 1: {time1}")
print(f"Time 2: {time2}")
print(f"Sum of Time 1 and Time 2: {sum_time}")
