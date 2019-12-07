import csv
import matplotlib.pyplot as plt


def delta_t(a, b, l):
    return (b - a) / l


def normalize(samples, step_size):
    return [x for (i, x) in enumerate(samples) if i % step_size == 0]


color_gps = 'tab:red'
color_acc = 'tab:blue'

fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')

with open('data_pixida/dataframe.csv', newline='') as acc_data:
    ax1.set_ylabel('x-acceleration (m^2/s)', color=color_acc)
    reader = csv.reader(acc_data, delimiter=',', quotechar='"')
    time_vals = []
    acc_x = []
    acc_y = []
    acc_z = []
    abs_vals = []
    error_margin = 0.7
    next(reader)
    last_val = 0
    for row in reader:
        if row[0] == '817ecb00-a229-11e9-a71a-ed8070118358':
            time_vals.append(row[2])
            try:
                x = float(row[13])
                last_val = x
            except ValueError:
                x = last_val
            acc_x.append(x)
        else:
            break
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration')
    ax1.plot(time_vals, acc_x, color=color_acc)
    ax1.tick_params(axis='y', labelcolor=color_acc)
    plt.show()
