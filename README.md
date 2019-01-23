# Tachometer Tool Version 1.03 for Raspberry Pi by Ben Cheney
This program is a tool to verify the accuracy of an automotive tachometer using the Raspberry Pi GPIO and a simple circuit.  The input parameters are tailored to conventional cylinder options and RPM operating range, however the formula would support any combination.

The formula is based on the principal of a four stroke engine having one ignition pulse per cylinder for every two revolutions of the crankshaft.  For example; a one cylinder engine at 1,000 revolutions per minute produces 500 ignition pulse signals.

- Pulse Per Minute = (Revolutions Per Minute * (Cylinders / 2))

- Pulse Per Second = (Pulse Per Minute / 60)

- Thus the signal to the tachometer in the form of pulse frequency within one second equals:
(1 / ((RPM * (Cylinders / 2)) / 60)

As the formula exists in the code it is divided by two to compensate for the period of time being doubled in the loop to execute the ON and OFF condition.

The next version may have two RPM entries to display the tachometer's sweep between the two values.  There is consideration for a hardware based input version that would use a knob for cylinder selection and RPM selection.  More to come, if you’ve read this far I thank you.
