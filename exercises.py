from locale import MON_1
import os
import matplotlib.image as image
from matplotlib import pyplot
import PyPDF2
import numpy as np

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
