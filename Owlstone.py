### code fro owlstone test###

import numpy as np
import matplotlib.pyplot as plt


def load_csv(filename):
    rough = np.genfromtxt(filename, delimiter=',')
    cv = rough[1:, 0]
    dv = rough[0, 1:]
    data = rough[1:, 1:]
    return cv, dv, data


def data_show(cv, dv, data):
    def onclick(event):
        if 1:
            cor_ax0 = ax0.transAxes.inverted().transform((event.x, event.y))
            inAxis0 = 0 <= cor_ax0[0] < 1 and 0 <= cor_ax0[1] < 1
            if inAxis0:
                i_coor = int(data.shape[0] - event.ydata)
                j_coor = int(event.xdata)
                ax1.cla()
                ax1.plot(cv, data[:, j_coor])
                ax1.set_xlabel('CV')
                ax1.set_ylabel('ion current')
                ax0.set_title('fingerprint CV: %f, DV: %d ion current: %f' %
                              (cv[i_coor], dv[j_coor], data[i_coor, j_coor]))
            else:
                ax0.set_title('fingerprint')
            plt.draw()  # update figure

    fig, (ax0, ax1) = plt.subplots(2, 1)
    ax0.imshow(np.log(data), extent=[0, data.shape[1], 0, data.shape[0]],
               aspect='auto', interpolation='none')
    ax0.set_title('fingerprint')
    ax0.set_xlabel('DV')
    ax0.set_ylabel('CV')
    plt.draw() # force draw for get axis text
    x_labels = [item.get_text() for item in ax0.get_xticklabels()]
#    print x_labels
    new_x_labels = [str(cv[int(x_label)]) if x_label != '' else ' '
                    for x_label in x_labels]
    
    ax0.set_xticklabels(new_x_labels)
    y_labels = [item.get_text() for item in ax0.get_yticklabels()]
    new_y_labels = [str(cv[int(y_label)]) if y_label != '' else ' '
                    for y_label in y_labels]
    ax0.set_yticklabels(new_y_labels)
    ax1.plot(data[:, 0])
    plt.draw()
    cid = fig.canvas.mpl_connect('motion_notify_event', onclick)
    return fig


if __name__ == '__main__':
    filename = raw_input('Enter file name :\n')
    cv, dv, data = load_csv(filename)
    fig = data_show(cv, dv, data)
    plt.show()
