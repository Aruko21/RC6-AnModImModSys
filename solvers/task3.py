import numpy as np

import models
import graphics as graph


def task3_solve(Tc, Ts, channels_num):
    channels_number_range = np.arange(1, channels_num + 1, 1)
    model = models.ModelUnlimitedQueue(client_t=Tc, handling_t=Ts, channels=1)
    plots = graph.ModelPlots(name="Model with limited queue")

    channels_busy = []
    busy_coefs = []
    queue_probs = []
    queue_length_expects = []

    for channels in channels_number_range:
        model.channels = channels
        channels_busy.append(model.busy_operators())
        busy_coefs.append(model.busy_coefficient())
        queue_probs.append(model.queue_prob())
        queue_length_expects.append(model.queue_length_expect())

    plots.show_feature_dep_chan(x_axis=channels_number_range, data=channels_busy, label="Math expect of busy operators")
    plots.show_feature_dep_chan(x_axis=channels_number_range, data=busy_coefs, label="Busy channels coefficient")
    plots.show_feature_dep_chan(x_axis=channels_number_range, data=queue_probs, label="Probability of queue existence")
    plots.show_feature_dep_chan(x_axis=channels_number_range, data=queue_length_expects, label="Math expect of queue length")
