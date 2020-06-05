from tkinter import*
from tkinter import filedialog
import zhananjianding as zn
import win32api

mode = 1

def main():
    def run1():
        global mode
        zhijue = 0
        if mode == 2:
            zhijue = messagebox.askyesno('提示', '你怀疑他是潜在渣男吗？')
        if zhijue:
            s = "别测了，相信自己的直觉，他就是铁渣男！"
            messagebox.showwarning('警告!','不用测了，相信你的直觉，他就是铁渣男！！！')
            txt.insert(END, s)
        else:
            zn.znName = inp1.get()
            zn.filename = inp2.get()
            if mode == 3:
                zn.totalPoint -= 70
            zn.zhanan()
            s = zn.end_word(zn.totalPoint, zn.znName)
            txt.insert(END, s)    #显示鉴定结果
            messagebox.showinfo('提示','已生成鉴定报告！')
            
    def run2():
        s = filedialog.askopenfilename()
        inp2.insert(END, s)
        
    def run3():
        win32api.ShellExecute(0, 'open', r'cons\baogao.docx', '','',1)
        
    def run4():
        txt.delete('1.0','end')
        
    
    def mode1():
        global mode
        mode = 1
        
    def mode2():
        global mode
        mode = 2
    
    def mode3():
        def run_mem():
            global mode
            if (inp.get() == "jy6666"):
                mode = 3
                messagebox.showinfo('提示','验证通过，已进入 会员模式 ')
            else:
                messagebox.showinfo('提示','会员验证失败，请检查秘钥是否正确\n或联系开发者购买秘钥')
            password.destroy()
                
        global mode
        password = Tk()
        password.title('身份验证')
        password.geometry('300x100')
        password.iconbitmap('.\material\logo.ico')
        
        lb = Label(password,font=("宋体", 10), text='请输入会员秘钥')
        lb.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
        inp = Entry(password, font=("宋体", 10), justify=CENTER)
        inp.place(relx=0.1, rely=0.4, relwidth=0.5, relheight=0.2)
        btn = Button(password, text='确认', command=run_mem)
        btn.place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.2)    
        password.mainloop()
        
        
    
    
    
    root = Tk()
    root.geometry('800x600')
    root.title('渣男鉴定器')
    root.iconbitmap('.\material\logo.ico')
    
    #菜单
    menubar = Menu(root)
    
    Mmenu = Menu(menubar, tearoff=False)
    
    Mmenu.add_radiobutton(label='标准模式', command=mode1)
    Mmenu.add_radiobutton(label='直觉模式', command=mode2)
    Mmenu.add_radiobutton(label='会员模式', command=mode3)
    
    menubar.add_cascade(label='模式',menu=Mmenu)
    
    
    root['menu']=menubar
    
    
    
    lb1 = Label(root,font=("宋体", 15), text='请输入被试者姓名')
    lb1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)
    inp1 = Entry(root, font=("宋体", 25), justify=CENTER)
    inp1.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.1)
    
    
    
    
    # 方法-直接调用 run1()
    btn1 = Button(root, text='开始鉴定', command=run1, bd=4, bg='#fdd')
    btn1.place(relx=0.35, rely=0.33, relwidth=0.3, relheight=0.1)
    
    btn2 = Button(root, text='导入聊天文件', command=run2)
    btn2.place(relx=0.35, rely=0.27, relwidth=0.1, relheight=0.04)
    inp2 = Entry(root, font=("宋体", 10), justify=CENTER)
    inp2.place(relx=0.45, rely=0.27, relwidth=0.2, relheight=0.04)
    
    
    # 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
    txt = Text(root)
    txt.place(relx=0.1, rely=0.46, relwidth=0.8, relheight=0.3)
    
    btn3 = Button(root, text='鉴定报告', command=run3, bd=4, bg='#ddf')
    btn3.place(relx=0.2, rely=0.80, relwidth=0.2, relheight=0.06)
    btn4 = Button(root, text='重测', command=run4, bd=4, bg='#ddd')
    btn4.place(relx=0.6, rely=0.80, relwidth=0.2, relheight=0.06)
    
    root.mainloop()
    
    
if __name__ == '__main__':
    main()
