from tkinter import *
import random

root = Tk()
root.title('Sales Application')
root.geometry('500x500')

months  = Label(root)
profit = Label(root)
maxProfitlabel = Label(root)
minProfitlabel = Label(root)

months['text'] = 'Months: ' + ('Janurary','Feburary','March','April','May','June','July','August','September','October','November','December')
profit['text'] = 'Profits: ' + (2000,45000,78000,97000,12000,465000,65000,5400,10000,30000,70000,90000)


maxProfit = max(profit)
maxIndexProfit = profit.index(maxProfit)
maxIndexMonth = months[maxIndexProfit]

minProfit = min(profit)
minIndexProfit = profit.index(minProfit)
minIndexMonth = months[minIndexProfit]

def stuff():
    maxProfitlabel['text'] = 'Maximum Profit of ' + (maxProfit) + ' was given in the month of ' + (maxIndexMonth)
    
    
def stuff2():
    minProfitlabel['text'] = 'Minimum Profit of ' + (minProfit) + ' was given in the month of ' + (minIndexMonth) 
    

btn = Button(root,text = 'Show Max Profitable Month',command = stuff)
btn2 = Button(root,text = 'Show Min Profitable Month',command = stuff2)

months.place(relx = 0.5,rely = 0.1,anchor=CENTER)
profit.place(relx = 0.5,rely = 0.2,anchor=CENTER)
btn.place(relx = 0.5,rely = 0.3,anchor=CENTER)
maxProfitlabel.place(relx = 0.5,rely = 0.6,anchor=CENTER)
btn2.place(relx = 0.5,rely = 0.7,anchor=CENTER)
minProfitlabel.place(relx = 0.5,rely = 0.8,anchor=CENTER)