from tkinter import *

# retrieve values from list as float
y = [float(line.strip()) for line in open('y_values_df.txt')]
# d = [float(line.strip()) for line in open('d_values_df.txt')]
y.reverse()
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
exhaust = canvas.create_polygon(w/2-wd2_s1, h+2, w/2+wd2_s1, h+2, w/2+1, h+2+wd2_s1, fill='orange')
stages.append(exhaust)
velocity = canvas.create_text(725, 975, text='v='+str(round(y[len(y) - 1], 6)))
# drag = canvas.create_text(725, 980, text='d='+str(round(d[0], 6)))

while index < len(y) - 1:
    for stage in stages:
        canvas.move(stage, 0, (y[index]*0.00000435)*(y[len(y) - 1] - y[len(y) - index - 1]))
    canvas.itemconfigure(velocity, text='v='+str(round(y[len(y) - 1 - index], 6)))
    canvas.update()
    index += 1

window.mainloop()
