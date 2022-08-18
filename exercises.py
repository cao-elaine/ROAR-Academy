from locale import MON_1
import os
import matplotlib.image as image
from matplotlib import pyplot
import PyPDF2
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


#11.1
# file_name = 'motto.txt'
# path = os.path.dirname(os.path.abspath(__file__))


# file = open(path+'/' + file_name, 'w')
# file.write('Fiat Lux!')
# file.close()

# file = open(path+'/' + file_name, 'r')
# for line in file:
#     print(line)

# file = open(path+'/' + file_name, 'a')
# file.write('Let there be light!')






#11.2
# lenna = image.imread('samples/lenna.bmp')
# flag = image.imread('united-states-of-america-flag-xs.jpg')

# lenna_width = lenna.shape[1]
# lenna_height = lenna.shape[0]
# flag_width = flag.shape[1]
# flag_height = flag.shape[0]
# for w in range(flag_width):
#     for h in range(flag_height):
#         lenna[h][lenna_width - flag_width + w] = flag[h][w]
# pyplot.imshow(lenna)
# pyplot.show()






#11.3
# file_handle = open('Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(file_handle)
# page_number = pdfReader.numPages
# page_text =''
# for page in range(page_number):
#     page_object = pdfReader.getPage(page)
#     page_text += page_object.extractText()

# histogram = {}
# modified_text = ''
# for c in page_text:
#     if c.isalpha():
#         c = c.lower()
#         modified_text += c
#     elif c.isspace():
#         modified_text += c
#     else:
#         modified_text += ' '
# words = modified_text.split()
# for w in words:
    
#     if 'httpswwwfulltextarchivecom' not in w:
#         if w not in histogram:
#             histogram[w] = 1
#         else:
#             histogram[w] += 1
    
# for key in histogram:
#     print(key + "({num})".format(num = histogram[key]), end = ' ')






#12.1
# v = np.array([2., 2., 4.])
# e0 = np.array([1.0, 0, 0])
# e1 = np.array([0, 1.0, 0])
# e2 = np.array([0, 0, 1.0])
# v0 = v@e0
# v1 = v@e1
# v2 = v@e2
# print(v0, v1, v2)






# #12.2
# #1
# m1 = np.array([[6, -9, 1],[4, 24, 8]])
# print (2*m1)
# #2
# m2 = np.array([[1,0],[0,1]])
# print(m2@m1)
# #3
# m3 = np.array([[4, 3],[3, 2]])
# m4 = np.array([[-2, 3],[3, -4]])
# print(m3@m4)






#12.3
# def swap_rows(M,a,b):
#     if a < 0 or b < 0 or a >= M.shape[0] or b >= M.shape[0]:
#         raise ValueError ('invalid input')
#     temp = M[a].copy()
#     M[a] = M[b]
#     M[b] = temp

# def swap_columns(M,a,b):
#     if a < 0 or b < 0 or a >= M.shape[1] or b >= M.shape[1]:
#         raise ValueError ('invalid input')
#     for i in range (M.shape[0]):
#         temp = M[i,a]
#         M[i,a] = M[i,b]
#         M[i,b] = temp

# m = np.array([[6, -9, 1],[4, 24, 8],[10,3,5]])
# swap_columns(m, 1, 2)
# print(m)






#12.4
# def set_array(L, rows, cols):
#     if rows * cols != len(L):
#         raise ValueError('invalid input')
#     numpy_array = np.zeros((rows, cols))
#     index = 0
#     for i in range(rows):
#         for j in range(cols): 
#             numpy_array[i][j] = L[index]
#             index += 1
#     return numpy_array

# L = [1,2,3,4,5,6,7,8]
# print(set_array(L, 8, 1))






# #12.5
# arr = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55]])
# blue = np.array(arr[:6, 1])
# print(blue)
# pink = np.array(arr[1, 2:4])
# print(pink)
# green = np.array(arr[2:4, 4:6])
# print(green)
# orange = np.array(arr[2:5:2, 0:5:2])
# print(orange)






#13.1
# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/samples/airplane.bmp'
background = plt.imread(filename)

second_hand_length = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 6
hour_hand_length = 100
hour_hand_width = 10
gmt_hour_hand_length = 100
gmt_hour_hand_width = 10
center = np.array([256, 256])

def clock_hand_vector(angle, length):
    return np.array([length * np.sin(angle), -length * np.cos(angle)])

# draw an image background
fig, ax = plt.subplots()

while True:
    plt.imshow(background)
    plt.axis('off')
    # First retrieve the time
    now_time = datetime.now()
    hour = now_time.hour
    gmt_hour = int(now_time.strftime('%H')) + 8
    if hour>12: hour = hour - 12
    if gmt_hour > 24: gmt_hour = gmt_hour - 24
    minute = now_time.minute
    second = now_time.second

    # Calculate end points of hour, minute, second

    hour_vector = clock_hand_vector(hour/12*2*np.pi+second/(3600*60)*2*np.pi, hour_hand_length)
    minute_vector = clock_hand_vector(minute/60*2*np.pi+second/3600*2*np.pi, minute_hand_length)
    second_vector = clock_hand_vector(second/60*2*np.pi, second_hand_length)
    gmt_hour_vector = clock_hand_vector(gmt_hour/24*2*np.pi+second/(3600*60*2)*2*np.pi, gmt_hour_hand_length)

    plt.arrow(center[0], center[1], hour_vector[0], hour_vector[1], head_length = 3, linewidth = hour_hand_width, color = 'black')
    plt.arrow(center[0], center[1], minute_vector[0], minute_vector[1], linewidth = minute_hand_width, color = 'black')
    plt.arrow(center[0], center[1], second_vector[0], second_vector[1], linewidth = second_hand_width, color = 'red')
    plt.arrow(center[0], center[1], gmt_hour_vector[0], gmt_hour_vector[1], linewidth = gmt_hour_hand_width, color = 'yellow')

    plt.pause(0.1)
    plt.clf()
