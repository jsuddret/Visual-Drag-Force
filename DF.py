from tkinter import *

# retrieve values from list as float
y = [float(line.strip()) for line in open('y_values_df.txt')]
y.reverse()
v = [float(line.strip()) for line in open('v_values_df.txt')]
v.reverse()
stages = []
index = 0

# create window, set attributes
window = Tk()
h = 1000
w = 800
canvas = Canvas(window, width=w, height=h, background='light blue')
window.title('VGF')
canvas.pack()

wd2_s1 = 10
wd2_s2 = 8
wd2_s3 = 6
h_s1 = 80
h_s2 = 20
stage1 = canvas.create_rectangle(w/2-wd2_s1, h, w/2+wd2_s1, h-h_s1, fill='black')
stages.append(stage1)
stage2 = canvas.create_rectangle(w/2-wd2_s2, h-h_s2, w/2+wd2_s2, h-h_s1-h_s2, fill='black')
stages.append(stage2)
stage3 = canvas.create_rectangle(w/2-wd2_s3, h-2*h_s2, w/2+wd2_s3, h-h_s1-2*h_s2, fill='black')
stages.append(stage3)

while index < len(y) - 1:
    for stage in stages:
        canvas.move(stage, 0, 2*(y[index + 1] - y[index]))
    canvas.update()
    index += 1

window.mainloop()
