#from math import cos, radians

## Create a string with spaces proportional to a cosine of x in degrees
#def make_dot_string(x):
#    rad = radians(x)                             # cos works with radians
#    numspaces = int(20 * cos(radians(x)) + 20)   # scale to 0-40 spaces
#    st = ' ' * numspaces + 'o'                   # place 'o' after the spaces
#    return st

#def main():
#    for i in range(0, 1800, 12):
#        s = make_dot_string(i)
#        print(s)

#main()

#from math import radians
#import numpy as np     # installed with matplotlib
#import matplotlib.pyplot as plt

#def main():
#    x = np.arange(0, radians(1800), radians(12))
#    plt.plot(x, np.cos(x), 'b')
#    plt.show()

#main()

#Câu hỏi:

#Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
#Các số thu được sẽ được in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy.

#Gợi ý:

#Sử dụng range(#begin, #end)
#Code mẫu: 

j=[]
for i in range(0, 3201):
    if (i%7==0) and (i%5!=0):
       j.append(str(i))
print (','.join(j))

#Bài 02: 

#Câu hỏi: 

#Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. 
#Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.

#Gợi ý: 

#Trong trường hợp dữ liệu đầu vào được cung cấp, bạn hãy chọn cách để người dùng nhập số vào.
#Code mẫu:

x=int(input("Nhập số cần tính giai thừa:"))
def fact(x):
    if x == 0:
      return 1
      return x * fact(x - 1)
print (fact(x))