# ESP8266 Button
# micropython exercise
#

# the machine library lets us interact with the microcontroller, like setting inputs and outputs.
 

# define the pin the button is attached to


# the Pin function takes a pin number and sets it to either input or output
# 1. The board pin number, the same as creating a digital output pin.
# 2. The type of pin, in this case a digital input with the value machine.Pin.IN. This means the pin will be set 
#    as an input that can read high or low levels.
# 3. The third parameter is the constant value machine.Pin.PULL_UP to enable an internal pull-up resistor on the 
#    pin. This pulls the pin up so that it defaults to a high value. 
#    If you don't use this parameter, the pin will default to a low value (or a high value. It depends on the pin).


while True:
    # When the button is pressed, it will pull the logic value on the input pin down. So if the button is pressed 
    # and we read the value of the button, it will read as a 0. When the button is released it will read as a 1.
    # We can use a NOT operator to invert the logic values of the button.

