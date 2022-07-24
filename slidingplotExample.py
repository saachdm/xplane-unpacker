import seaborn as sns
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
from XPU import FlightData


def slidingplot(flightdata_objs, x, y):

    sns.set_style("whitegrid")
    fig, ax = plt.subplots()
    lines = {}
    for i in range(len(y)):
        (lines["line{0}".format(i)],) = plt.plot(
            flightdata_objs.data_df[x[0]], flightdata_objs.data_df[y[i]]
        )
    plt.legend(y, loc="upper right")
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.subplots_adjust(
        left=0.125, bottom=0.25, top=0.963, right=0.955, wspace=0.5, hspace=0.5
    )
    axSlider1 = plt.axes([0.2, 0.1, 0.6, 0.02])
    slder1 = Slider(
        axSlider1,
        "Left limit",
        valmin=0,
        valmax=max(flightdata_objs.time_initial) - 10,
        valinit=1,
    )
    axSlider2 = plt.axes([0.2, 0.05, 0.6, 0.02])
    slder2 = Slider(
        axSlider2,
        "Right limit",
        valmin=10,
        valmax=max(flightdata_objs.time_initial) - 10,
        valinit=30,
        valstep=1,
        slidermin=slder1,
        closedmax=True,
    )

    def valupdate(val):
        min_time = slder1.val
        max_time = slder2.val
        min_temp = []
        max_temp = []
        flightdata_objs.update(min_time, max_time)
        for i, (k, v) in enumerate(lines.items()):
            v.set_data(flightdata_objs.data_df[x[0]], flightdata_objs.data_df[y[i]])
            min_temp.append(min(list(flightdata_objs.data_df[y[i]])))
            max_temp.append(max(list(flightdata_objs.data_df[y[i]])))
        ax.set_ylim(
            min(min_temp) - 0.1 * (abs(max(max_temp) - min(min_temp))),
            max(max_temp) + 0.1 * (abs(max(max_temp) - min(min_temp))),
        )
        ax.set_xlim(min_time, max_time)

    slder1.on_changed(valupdate)
    slder2.on_changed(valupdate)
    ax.margins(0, 0)
    plt.show()


flight_data = FlightData("xplanedataExample.txt")
slidingplot(flight_data, ["time"], ["thro1_part", "alpha_deg"])
