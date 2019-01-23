# microbit-traffic-lights
Traffic lights for a microbit

There are 2 circuit diagrams, the simple method has a problem.  When 2 LEDs are on the current takes the easiest route, the red LED glows brightly and the amber one is very dim.  The amber LED and red LED have similar electrical characteristics, should the example require the green and amber LED to be illuminated at the same time one would be almost totally snuffed out.

Solution, just adding transistors balanced the loads sufficiently.  The correct method is to calculate the required resitance for the current drain of the LED. In reality each LED should have it's own individual resistor.
