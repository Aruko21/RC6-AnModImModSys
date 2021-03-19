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

    def show_feature_dep_chan(self, x_axis, data, label, x_label="Number of channels"):
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=FIGSIZE, dpi=self.dpi)
        axes.plot(x_axis, data, linestyle='--', marker="o", color="blue",
                  label="{} depends on {}".format(label, x_label))
        axes.set_ylabel(label)
        axes.set_xlabel(x_label)
        axes.legend(loc='upper right')
        axes.grid()
        plt.show()

        if self.save_file:
            fig.savefig(SAVE_IMG_LOCATION + "/" + self.name + "_" + label + ".png", dpi=SAVE_DPI)

        return

    def show_feature_family_dependency(self, x_axis, data, label, family_features, x_label, family_feature_label):
        color_map = plt.cm.get_cmap("cool", len(data))

        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=FIGSIZE, dpi=self.dpi)

        for i in range(len(data)):
            axes.plot(x_axis, data[i], linestyle='--', marker="o", color=color_map(i))

        # Writing custom mark in the legend, taking into account existing ones
        # Because this is the better way for legend family of Ln(x).
        legend = plt.Line2D([], [], color=color_map(0), linestyle="--", marker="o", label=label)

        # [0] at the end of expression means the first return value from the function
        handles = axes.get_legend_handles_labels()[0]
        handles.append(legend)
        axes.legend(handles=handles, loc="upper right")

        sm = plt.cm.ScalarMappable(cmap=color_map,
                                   norm=plt.Normalize(vmin=family_features[0], vmax=family_features[-1]))
        color_bar = plt.colorbar(sm)
        color_bar.ax.set_ylabel(family_feature_label)

        axes.set_ylabel(label)
        axes.set_xlabel(x_label)
        axes.grid()
        plt.show()

        if self.save_file:
            fig.savefig(SAVE_IMG_LOCATION + "/" + self.name + "_" + label + "_" + family_feature_label + ".png",
                        dpi=SAVE_DPI)
