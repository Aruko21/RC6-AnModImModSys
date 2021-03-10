import matplotlib.pyplot as plt
import numpy as np

SAVE_DPI = 300
SAVE_IMG_LOCATION = 'graphics'
FIGSIZE = (8, 6)


class ModelPlots:
    def __init__(self, dpi=200, save_file=False, name="model"):
        self.dpi = dpi
        self.save_file = save_file
        self.name = name

    def show_feature_dep_chan(self, channels, data, label):
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=FIGSIZE, dpi=self.dpi)
        axes.plot(np.arange(1, channels + 1, 1), data, linestyle='--', marker="o", color="blue", label="{} depends on number of channels".format(label))
        axes.set_ylabel(label)
        axes.set_xlabel('Number of channels')
        axes.legend(loc='best')
        axes.grid()
        plt.show()

        if self.save_file:
            fig.savefig(SAVE_IMG_LOCATION + "/" + self.name + "_" + label + ".png", dpi=SAVE_DPI)

        return
