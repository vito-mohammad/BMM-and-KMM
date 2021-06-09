# hello world
# this program is  written by Vito On 23,Jan,2021, to calculate BMM & KMM.
#Now we import tkinter pkg

from tkinter import *

#Now we create a window and resize that
window = Tk()
window.title("BMM and KMM")
window.geometry("400x400")
window.minsize(400 , 400)
window.config(bg="#800011")
window.iconbitmap("icon1.ico")          #this the icon of the program  that should be near the py file if you don't have icon1.ico you should delete this line.



#here is the brain of the program that calculate BMM and KMM
#there is two founction that first one calculate BMM and second calculate KMM
def bmm():
      try:
            sumit2.config(text="")
            sumit.config(text="")
            sumit3.config(text="")                                                          
            if int(entry1st.get()) == int(entry2nd.get()):
                  sumit2.config(text="Your KMM is: {}".format(int(entry1st.get())))
                  sumit.config(text="Your BMM is: {}".format(int(entry1st.get())))
            if int(entry2nd.get()) == 0:
                  sumit2.config(text="Your KMM is: {}".format(0))
                  sumit.config(text="Your BMM is: {}".format(0))
            if  int(entry1st.get()) == 0:
                  sumit2.config(text="Your KMM is: {}".format(0))
                  sumit.config(text="Your BMM is: {}".format(0))
            if int(entry1st.get()) == 1:
                  sumit2.config(text="Your KMM is: {}".format(int(entry2nd.get())))
                  sumit.config(text="Your BMM is: {}".format(1))
            if  int(entry2nd.get()) == 1:
                  sumit2.config(text="Your KMM is: {}".format(int(entry1st.get())))
                  sumit.config(text="Your BMM is: {}".format(1))
            else:
                  if int(entry1st.get())%int(entry2nd.get())==0:
                        sumit.config(text="Your BMM is: {}".format(int(entry2nd.get())))
            #these was some addintion to improve to program
                  else:
                        def b_m_m(a,b):
                              if a%b==0:
                                    return b
                              return (b_m_m(b,a%b))
                        sumit.config(text="Your BMM is: {}".format(b_m_m(int(entry1st.get()),int(entry2nd.get()))))
                  def kmm():
                        sumit2.config(text="Your KMM is: {}".format((int(int(entry1st.get())*int(entry2nd.get()))/(b_m_m(int(entry1st.get()),int(entry2nd.get()))))))
                  kmm()
      except NameError:                    #Some except to improve program
            None
      except ValueError:            # if you enter a string this execpt print please give me number
            sumit3.config(text="Please give me number")
      except ZeroDivisionError:
            sumit3.config(text="a number you give shouldn't be zero")



#here is labels , entries and button.            
first_label = Label(window , text = "Give me first number", bg="#800011")
first_label.pack()


entry1st = Entry(window, bg="#5F5F5F",width="30",font="200")
entry1st.pack()
 

second_label = Label(window , text = "Give me second number", bg="#800011")
second_label.pack()

entry2nd = Entry(window, bg="#5F5F5F",width="30",font="200")
entry2nd.pack()


sumit1 = Label (window, text = "", bg="#800011",width = 30)
sumit1.pack()

botton = Button(window, text= "calculate", bg="#006A84",command=bmm)
botton.pack()

sumit3 = Label (window, text = "", bg="#800011",font="Lato")
sumit3.pack()

                          
sumit = Label (window, text = "", bg="#800011",font="Tahoma")
sumit.pack()

sumit2 = Label (window, text = "", bg="#800011",font="Tahoma")
sumit2.pack()




#Enjoy using this program


window.mainloop()









#if you found a bug or s,th that can improve  my program Email:   mohammad.avatar2014@gmail.com with bug subject
#good luck
#I'm Vito print("hello world")
