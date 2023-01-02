from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()
    
    if email=='saurabh@gmail.com' and password=='12345':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed') 
    
root=Tk()
root.title('Login Form')
#root.iconbitmap('icon path name')
root.geometry('400x500')
root.configure(bg='teal')
# img=ImageTk.Photoimage(Image.open('flipkart-logo.png'))
# img_label=Lable(root,image=img)
text_label=Label(root,text='flipkart',fg='blue',bg='yellow')
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack()
email_label.config(font=('verdana',12))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input =Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='Login Here',bg='white',fg='black',width=30,height=3,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',8))

root.mainloop()
