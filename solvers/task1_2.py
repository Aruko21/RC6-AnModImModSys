import numpy as np

import models
import graphics as graph


def task1_2_solve(Tc, Ts, channels_num, q_len_max):
    channels = 1
    queue_len_range = np.arange(1, q_len_max + 1, 1)
    channels_number_range = np.arange(1, channels_num + 1, 1)
    model = models.ModelLimitedQueue(client_t=Tc, handling_t=Ts, channels=channels, q_len=1)
    plots = graph.ModelPlots(name="Model with limited queue")

    queue_denials = []
    queue_channels_busy = []
    channels_busy_coefs = []
    queue_probs_all = []
    queue_length_expects_all = []
    queue_busy_coefs_all = []

    for q_len in queue_len_range:
        model.q_len = q_len

        denials = []
        channels_busy = []
        busy_coefs = []
        queue_probs = []
        queue_length_expects = []
        queue_busy_coefs = []

        for channels in channels_number_range:
            model.channels = channels
            denials.append(model.denial_prob())
            channels_busy.append(model.busy_operators())
            busy_coefs.append(model.busy_coefficient())
            queue_probs.append(model.queue_prob())
            queue_length_expects.append(model.queue_length_expect())
            queue_busy_coefs.append(model.queue_busy_coef())

        queue_denials.append(denials)
        queue_channels_busy.append(channels_busy)
        channels_busy_coefs.append(busy_coefs)
        queue_probs_all.append(queue_probs)
        queue_length_expects_all.append(queue_length_expects)
        queue_busy_coefs_all.append(queue_busy_coefs)

    plots.show_feature_family_dependency(x_axis=channels_number_range, data=queue_denials,
                                         label="Probability of denial", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    plots.show_feature_family_dependency(x_axis=channels_number_range, data=queue_channels_busy,
                                         label="Math expect of busy operators", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    plots.show_feature_family_dependency(x_axis=channels_number_range, data=channels_busy_coefs,
                                         label="Busy channels coefficient", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    plots.show_feature_family_dependency(x_axis=channels_number_range, data=queue_probs_all,
                                         label="Probability of queue", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    plots.show_feature_family_dependency(x_axis=channels_number_range, data=queue_length_expects_all,
                                         label="Math expect of queue length", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    plots.show_feature_family_dependency(x_axis=channels_number_range, data=queue_busy_coefs_all,
                                         label="Busy queue coefficient", family_features=queue_len_range,
                                         family_feature_label="Queue capacity", x_label="Number of channels")
    # --------

    queue_denials = []
    queue_channels_busy = []
    channels_busy_coefs = []
    queue_probs_all = []
    queue_length_expects_all = []
    queue_busy_coefs_all = []

    for channels in channels_number_range:
        model.channels = channels

        denials = []
        channels_busy = []
        busy_coefs = []
        queue_probs = []
        queue_length_expects = []
        queue_busy_coefs = []

        for q_len in queue_len_range:
            model.q_len = q_len
            denials.append(model.denial_prob())
            channels_busy.append(model.busy_operators())
            busy_coefs.append(model.busy_coefficient())
            queue_probs.append(model.queue_prob())
            queue_length_expects.append(model.queue_length_expect())
            queue_busy_coefs.append(model.queue_busy_coef())

        queue_denials.append(denials)
        queue_channels_busy.append(channels_busy)
        channels_busy_coefs.append(busy_coefs)
        queue_probs_all.append(queue_probs)
        queue_length_expects_all.append(queue_length_expects)
        queue_busy_coefs_all.append(queue_busy_coefs)

    plots.show_feature_family_dependency(x_axis=queue_len_range, data=queue_denials,
                                         label="Probability of denial", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="Queue capacity")
    plots.show_feature_family_dependency(x_axis=queue_len_range, data=queue_channels_busy,
                                         label="Math expect of busy operators", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="Queue capacity")
    plots.show_feature_family_dependency(x_axis=queue_len_range, data=channels_busy_coefs,
                                         label="Busy channels coefficient", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="queue capacity")
    plots.show_feature_family_dependency(x_axis=queue_len_range, data=queue_probs_all,
                                         label="Probability of queue", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="Queue capacity")
    plots.show_feature_family_dependency(x_axis=queue_len_range, data=queue_length_expects_all,
                                         label="Math expect of queue length", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="Queue capacity")
    plots.show_feature_family_dependency(x_axis=queue_len_range, data=queue_busy_coefs_all,
                                         label="Busy queue coefficient", family_features=channels_number_range,
                                         family_feature_label="Number of channels", x_label="Queue capacity")
