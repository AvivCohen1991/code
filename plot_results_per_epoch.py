import os
import torch
import matplotlib.pyplot as plt


def rms(loss_list):
    return [sum([sum(trajectory_losses) for trajectory_losses in epoch_losses]) for epoch_losses in loss_list]


def vo(loss_list):
    return [sum([trajectory_losses[-1] for trajectory_losses in epoch_losses]) for epoch_losses in loss_list]


def extract_label(filename):
    components = filename.split('_')
    return components[-1]


def plot(title, y_label, x_label):
    loss_list_dir = "results/loss_lists"

    for filename in os.listdir(loss_list_dir):
        print(filename)
        f = os.path.join(loss_list_dir, filename)
        if os.path.isfile(f):
            loss_list = torch.load(f)
            loss_per_epoch = rms(loss_list)
            label = extract_label(filename)
            label = '.'.join(label.split('.')[:-1])
            plt.plot(loss_per_epoch, label=label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='lower right', fontsize=6)
    print("showing")
    plt.savefig("figure.png")
    plt.show()


if __name__ == '__main__':
    plot('alpha', 'sum rms loss', 'epoch')



