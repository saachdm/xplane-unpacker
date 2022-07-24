# XPlane Unpacker

XPlane Unpacker is a simple script to help you unpack XPlane's odd data output naming. 

FlightData is a class that reads an XPlane data output .txt file and converts it into two forms: class attribute and pandas dataframe. You can use either of the two, whichever suits your need.

The variable naming is as follows:

| Variable  | data output .txt | Description|
| ------------- | ------------- | ------------- |
| time  | (refer to the time_type)  | |
| Vind_kias  | _Vind,_kias  | Indicated airspeed in KIAS|
| Vind_keas  | _Vind,_keas  | Equivalent airspeed in KEAS|
| Vtrue_ktas  | _Vtrue,_ktas  | True airspeed in KTAS|
| Vtrue_ktgs  | _Vtrue,_ktgs  | True airspeed in KTGS|

(to be continued)

## Usage

This is an example from plotExample.py. In this case, two different flight data are plotted in the same variable axis. flightdata and flightdata2 object represents the XPlane data outputs and the variables are accessed using the object's attributes

```python
import matplotlib.pyplot as plt
from XPU import FlightData

flightdata = FlightData("xplanedataExample.txt", "missn,time")
flightdata2 = FlightData("xplanedataExample2.txt", "missn,time")

fig, ax = plt.subplots(1, 2)
ax[0].plot(flightdata.time, flightdata.pitch_deg)
ax[0].plot(flightdata2.time, flightdata2.pitch_deg)
ax[0].grid()
ax[0].set_ylabel("Pitch (deg)")
ax[1].plot(flightdata.time, flightdata.roll_deg)
ax[1].plot(flightdata2.time, flightdata2.roll_deg)
ax[1].grid()
ax[1].set_ylabel("Roll (deg)")
plt.setp(ax[:], xlabel="Mission Time (s)")
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)
plt.legend(["Flightdata 1", "Flightdata 2"])
plt.show()

```

## Contributing
Any contributions are welcome.


## License
[GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/)
