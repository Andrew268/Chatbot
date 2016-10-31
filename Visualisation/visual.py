from graphics import *
import csv
import time

window = GraphWin("Visualisation", 300, 300)

#ball = Circle(Point(100,100), 50)
#ball.setFill(color_rgb(0,255,255))
#ball.draw(window)


#text_file = open("data.txt", "r")
#lines = text_file.readlines()
#print lines
#print len(lines)

#text_file.close()

variable = []

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

myList[0]= 52
myList[1]= 47
myList[2]= 57
myList[3]= 49
myList[4]= 59
myList[5]= 62
myList[6]= 44
myList[7]= 76
myList[8]= 52
myList[9]= 52
myList[10]= 44
myList[11]= 59
myList[12]= 59
myList[13]= 79
myList[14]= 59
myList[15]= 42
myList[16]= 57
myList[17]= 48
myList[18]= 80
myList[19]= 43
myList[20]= 72
myList[21]= 74
myList[22]= 59
myList[23]= 44
myList[24]= 57
myList[25]= 55
myList[26]= 49
myList[27]= 54
myList[28]= 54

while myList<90:
    
    ball2 = Circle(Point(myList[1], myList[1]), myList[1])
    ball2.setFill(color_rgb(0,255,255))
    ball2.draw(window)
    
    print '-------------'
    
    #time.sleep(0.1)
    
    myList+=1

#filename = 'data.txt'

#with open(filename) as f:
    #data = f.readlines()
    
#for n, line in enumerate(data, 1):
    #print''.format(n), line.rstrip()
    

        
# Wait until the mouse is clicked before closing the window
window.getMouse()