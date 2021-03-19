import numpy as np

import models
import graphics as graph


def task2_solve(Tc, Ts, channels_num):
    model = models.ModelAdjustersClosed(broken_t=Tc, handling_t=Ts, channels=channels_num, adjusters=1)
    plots = graph.ModelPlots(name="Model with adjusters")

    adjusters_number_range = np.arange(1, channels_num + 1, 1)

    broken_channels = []
    waited_channels = []
    waiting_probs = []
    busy_adjusters = []
    busy_adjucters_coefs = []

    for adjusters in adjusters_number_range:
        model.adjusters = adjusters
        broken_channels.append(model.broken_channels())
        waited_channels.append(model.waited_channels())
        waiting_probs.append(model.waiting_probability())
        busy_adjusters.append(model.busy_adjusters())
        busy_adjucters_coefs.append(model.busy_adjucters_coef())

    plots.show_feature_dep_chan(x_axis=adjusters_number_range, data=broken_channels,
                                label="Math expect of broken machines", x_label="Number of adjusters")
    plots.show_feature_dep_chan(x_axis=adjusters_number_range, data=waited_channels,
                                label="Math expect of adjuster waiting machines", x_label="Number of adjusters")
    plots.show_feature_dep_chan(x_axis=adjusters_number_range, data=waiting_probs,
                                label="Probability of adjuster waiting", x_label="Number of adjusters")
    plots.show_feature_dep_chan(x_axis=adjusters_number_range, data=busy_adjusters,
                                label="Math expect of busy adjusters", x_label="Number of adjusters")
    plots.show_feature_dep_chan(x_axis=adjusters_number_range, data=busy_adjucters_coefs,
                                label="Busy adjusters coefficient", x_label="Number of adjusters")
