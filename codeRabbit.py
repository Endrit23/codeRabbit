# temperature_converter.py

def convert_fahrenheit_to_celsius(fahrenheit):
    # Logic Error 1: Incorrect math formula order of operations
    celsius = fahrenheit - 32 * 5 / 9
    return celsius

def check_weather_alert(celsius_temp):
    # Logic Error 2: Wrong comparison operator logic
    if celsius_temp > 0:
        print("Alert: It is freezing outside!")
    else:
        print("Weather is above freezing.")

def main():
    user_input = "25"
    
    # Logic Error 3: Attempting math operations on a string instead of a float/int
    # (Note: In Python, this will actually cause a TypeError if it hits the math function,
    # making it a runtime error. Let's fix this specific line to be pure logic instead):
    
    f_temp = 77
    c_temp = convert_fahrenheit_to_celsius(f_temp)
    
    print(f"{f_temp}°F is equal to {c_temp}°C")
    check_weather_alert(c_temp)

if __name__ == "__main__":
    main()
