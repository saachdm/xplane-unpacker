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
