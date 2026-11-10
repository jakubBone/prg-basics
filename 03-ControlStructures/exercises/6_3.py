# A program that tells how many bulbs are lit in a room with three bulbs and two switches.
# Switch one lights one bulb, switch two lights the other two bulbs. 

 # False - switch off, True - switch on
light_switch1 = True 
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f'Bulbs on: {bulbs_on}')
