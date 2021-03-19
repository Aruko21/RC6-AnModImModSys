import numpy as np

import models
import graphics as graph


def task1_3_solve(Tc, Ts, channels_num):
    channels_number_range = np.arange(1, channels_num + 1, 1)

    model = models.ModelUnlimitedQueue(client_t=Tc, handling_t=Ts, channels=1)
    plots = graph.ModelPlots(name="Model with limited queue")

    min_channels = 0

    for channels in channels_number_range:
        model.channels = channels
        if model.is_a_coef_valid():
            min_channels = channels
            break

    if min_channels == 0:
        raise ValueError("'a' coefficient is more than 1 for '{}' channels".format(channels_num))

    print("Number of channels with 'a' coefficient less than 1: ", min_channels)

    channels_number_range_trim = channels_number_range[min_channels - 1:]

    busy_coefs = []
    queue_length_expects = []

    for channels in channels_number_range:
        model.channels = channels
        busy_coefs.append(model.busy_coefficient())
        queue_length_expects.append(model.queue_length_expect())

    plots.show_feature_dep_chan(x_axis=channels_number_range, data=busy_coefs, label="Busy channels coefficient")
    plots.show_feature_dep_chan(x_axis=channels_number_range, data=queue_length_expects,
                                label="Math expect of queue length")

    channels_busy = []
    busy_coefs = []
    queue_probs = []
    queue_length_expects = []

    for channels in channels_number_range_trim:
        model.channels = channels
        channels_busy.append(model.busy_operators())
        busy_coefs.append(model.busy_coefficient())
        queue_probs.append(model.queue_prob())
        queue_length_expects.append(model.queue_length_expect())

    plots.show_feature_dep_chan(x_axis=channels_number_range_trim, data=channels_busy, label="Math expect of busy operators")
    plots.show_feature_dep_chan(x_axis=channels_number_range_trim, data=busy_coefs, label="Busy channels coefficient")
    plots.show_feature_dep_chan(x_axis=channels_number_range_trim, data=queue_probs, label="Probability of queue existence")
    plots.show_feature_dep_chan(x_axis=channels_number_range_trim, data=queue_length_expects, label="Math expect of queue length")
