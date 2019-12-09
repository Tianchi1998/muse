import csv
import pygame
import time

r = csv.reader(open('messy_data_in_60_seconds.csv'))
lines = list(r)
# Delete the first line of data which is the table head
lines = lines[1:]

# Get the min and max values of those four signals
all_TP9 = []
all_AF7 = []
all_AF8 = []
all_TP10 = []

for line in lines:
    all_TP9.append(float(line[1]))
    all_AF7.append(float(line[2]))
    all_AF8.append(float(line[3]))
    all_TP10.append(float(line[4]))

min_all_TP9 = min(all_TP9)
max_all_TP9 = max(all_TP9)
min_all_AF7 = min(all_AF7)
max_all_AF7 = max(all_AF7)
min_all_AF8 = min(all_AF8)
max_all_AF8 = max(all_AF8)
min_all_TP10 = min(all_TP10)
max_all_TP10 = max(all_TP10)

# print("Min value of TP9: ", min_all_TP9)
# print("Max value of TP9: ", max_all_TP9)
# print("Min value of AF7: ", min_all_AF7)
# print("Max value of AF7: ", max_all_AF7)
# print("Min value of AF8: ", min_all_AF8)
# print("Max value of AF8: ", max_all_AF8)
# print("Min value of TP10: ", min_all_TP10)
# print("Max value of TP10: ", max_all_TP10)

# Scale those four signals to the range of 0 to 255 which is then processed to generate the RGB values
# For example, if a signal's range is from -124 to +123, then firstly I add 124 to all the data
# to make the range 0 to 247. Then every piece of date is divided by the new max value which is 247
# to get a proportion from 0 to 1. Finally, multiply that value with 255.
for i in range(0, len(lines)):
    lines[i][1] = ((float(lines[i][1])+abs(min_all_TP9))/(float(max_all_TP9)+abs(min_all_TP9))) * 255
    lines[i][2] = ((float(lines[i][2])+abs(min_all_AF7))/(float(max_all_AF7)+abs(min_all_AF7))) * 255
    lines[i][3] = ((float(lines[i][3])+abs(min_all_AF8))/(float(max_all_AF8)+abs(min_all_AF8))) * 255
    lines[i][4] = ((float(lines[i][4])+abs(min_all_TP10))/(float(max_all_TP10)+abs(min_all_TP10))) * 255

# print(lines)

# All colors go here
colors = []
for i in range(0, len(lines)):
    colors.append([])

for i in range(0, len(lines)):
    colors[i].append(lines[i][1])
    colors[i].append(lines[i][2])
    # This is the Blue value of a RGB which is derived from calculating the average of AF8 and TP10
    colors[i].append((lines[i][3] + lines[i][4])/2)

# print(colors)

# Use pygame to show those colors

pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
screen.fill(white)
pygame.display.set_caption("My program")
pygame.display.flip()

for color in colors:
    screen.fill(color)
    pygame.display.update()
    time.sleep(0.5)

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
