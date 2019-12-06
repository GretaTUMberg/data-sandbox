import csv
import numpy as np
import matplotlib.pyplot as plt

def delta_t(a, b, l):
	return (b-a)/l

def normalize(samples, step_size):
	return [x for (i, x) in enumerate(samples) if i % step_size == 0]

color_gps = 'tab:red'
color_acc = 'tab:blue'

fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')

with open('acc_sess_2.csv', newline='') as acc_data:
	ax1.set_ylabel('x-acceleration (m^2/s)', color=color_acc)
	reader = csv.reader(acc_data, delimiter=',', quotechar='"')
	time_vals = []
	acc_x = []
	acc_y = []
	acc_z = []
	abs_vals = []
	error_margin = 0.7
	next(reader)
	for row in reader:
		time_vals.append(float(row[0]))
		x = float(row[1])
		y = float(row[2])
		z = float(row[3])
		acc_x.append(x if (x <= -error_margin or x >= error_margin) else 0)
		acc_y.append(y if (y <= -error_margin or y >= error_margin) else 0)
		acc_z.append(z if (z <= -error_margin or z >= error_margin) else 0)
		abs_vals.append(float(row[4]))
	plt.xlabel('Time (s)')
	plt.ylabel('Acceleration')
	delta_t = delta_t(time_vals[0],time_vals[-1],len(time_vals))
	sample_size = 30000
	step_size = int(0.25/delta_t)
	time_norm = normalize(time_vals, step_size)
	acc_x_norm = normalize(acc_x, step_size)
	acc_y_norm = normalize(acc_y, step_size)
	acc_z_norm = normalize(acc_z, step_size)
	abs_acc_norm = normalize(abs_vals, step_size)
	# threshold = max(abs_acc_norm) / 2
	# peaks = 
	# plt.plot(time_norm[:sample_size], abs_acc_norm[:sample_size])
	ax1.plot(time_norm[:sample_size], acc_x_norm[:sample_size], color=color_acc)
	ax1.tick_params(axis='y',labelcolor=color_acc)
	plt.show()

# ax2 = ax1.twinx()

# with open('acc_sess_2.csv', newline='') as gps_data:
# 	ax2.set_ylabel('speed (m/s)', color=color_gps)
# 	reader = csv.reader(gps_data, delimiter=',', quotechar='"')
# 	speed_vals = []
# 	times = []
# 	next(reader)
# 	for row in reader:
# 		times.append(float(row[0]))
# 		speed_vals.append(float(row[4]))

# 	delta_t1 = delta_t(times[0], times[-1], len(times))
# 	sample_size1 = 30000
# 	step_size1 = int(1/delta_t1)
# 	time_norm = normalize(times, step_size1)
# 	speeds_norm = normalize(speed_vals, step_size1)
# 	ax2.plot(time_norm[:sample_size1], speeds_norm[:sample_size1], color=color_gps)
# 	ax2.tick_params(axis='y', labelcolor=color_gps)
