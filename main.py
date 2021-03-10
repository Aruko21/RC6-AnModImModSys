import numpy

import models
import graphics as graph

Tc = 37
Ts = 229
Tw = 591


def main():
    task1Model = models.ModelWithoutQueue(client_t=Tc, handling_t=Ts)
    task1Plots = graph.ModelPlots(name="Model without queue")

    channels = 1
    denials = [task1Model.denial_prob(channels)]
    channels_busy = [task1Model.busy_operators(channels)]
    busy_coefs = [task1Model.busy_coefficient(channels)]

    while denials[channels - 1] >= 0.01:
        channels += 1
        denials.append(task1Model.denial_prob(channels))
        channels_busy.append(task1Model.busy_operators(channels))
        busy_coefs.append(task1Model.busy_coefficient(channels))

    task1Plots.show_feature_dep_chan(channels=channels, data=denials, label="Probability of denial")
    task1Plots.show_feature_dep_chan(channels=channels, data=channels_busy, label="Math expect of busy operators")
    task1Plots.show_feature_dep_chan(channels=channels, data=busy_coefs, label="Busy channels coefficient")


if __name__ == '__main__':
    main()
