

from tkinter import *
from tkinter.filedialog import *
from tkinter import colorchooser

canvas_width = 1000
canvas_height = 600 #画布宽和高

current_color=['#000000'] #用于储存当前选中的颜色
thickness=3 #默认画笔粗细为3

#保存文件
def Save():
   filetype=[('JPEG','*.jpg'),('PNG','*.png')]
   b=asksaveasfile(defaultextension='.png',filetypes=filetype,
                       initialdir='C:\\',initialfile='未命名',title='另存为')
   print(b)
#选择画笔颜色的函数
def ColorChoice():
    s = colorchooser.askcolor(color="black", title="选择画笔颜色") #返回一个tuple,index为1时为颜色的十六进制值
    current_color[0]=s[1]
#选择画笔粗细的函数
def ThicknessChoice_1px():
    global thickness #全局变量才可修改
    thickness=1
def ThicknessChoice_3px():
    global thickness
    thickness=3
def ThicknessChoice_5px():
    global thickness
    thickness=5
def ThicknessChoice_8px():
    global thickness
    thickness=8

#绘图的函数
def paint( event ):
   color = current_color #选择画笔颜色
   x1, y1 = ( event.x - thickness ), ( event.y - thickness )
   x2, y2 = ( event.x + thickness), ( event.y + thickness ) #thickness为圆点半径，代表画笔粗细
   canvas.create_oval( x1, y1, x2, y2, fill = color,outline="" ) #以点连成线
   print(thickness)


win=Tk()
win.title("画图工具") #窗口设置

#画布设置
canvas = Canvas(win, width=canvas_width, height=canvas_height)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind( "<B1-Motion>", paint ) #拖动鼠标绘制

#菜单栏设置
menu1=Menu(win,background='#C3DEEF')
menu2_1=Menu(menu1,tearoff=False)
win.config(menu=menu1)
menu1.add_command(label='保存',command=Save)
menu1.add_command(label='颜色',command=ColorChoice)
menu1.add_cascade(label='粗细',menu=menu2_1)
menu2_1.add_command(label='1px',command=ThicknessChoice_1px)
menu2_1.add_command(label='3px',command=ThicknessChoice_3px)
menu2_1.add_command(label='5px',command=ThicknessChoice_5px)
menu2_1.add_command(label='8px',command=ThicknessChoice_8px)
menu1.add_command(label='形状')
menu1.add_command(label='自定义')


win.mainloop()
