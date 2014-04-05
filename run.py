from tkinter import *
class Main(object):
  def __init__(self):
    self.root=Tk()
    self.root.title("Audio Control")
    self.root.geometery("230x254")
    self.root.configure(background="#88ffff")
    self.buttonHDMI=Button(self.root, text="Force Audio to HDMI", command=self.hdmiButtonCall)
    self.buttonHDMI.pack()
    self.buttonHeadphone=Button(self.root, text="Force Audio to Headphones (3.5mm audio jack)", command=self.headphoneButtonCall)
    self.buttonHeadphone.pack()
    self.slider=Scale(self.root, from_=0, to=99, orient=HORIZONTAL, command=self.slide, length=198, background="#88ffff")
    self.slider.pack()
  def hdmiButtonCall():
    os.system("sudo amixer cset numid=3 2")
  def headphoneButtonCall():
    os.system("sudo amixer cset numid=3 1")
  def slide(self, x):
    os.system("sudo amixer cset numid=3 " + str(x) + “%”)
