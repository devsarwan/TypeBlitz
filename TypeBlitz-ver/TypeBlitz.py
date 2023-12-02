from tkinter import *
import webbrowser
from tkinter import messagebox
from ctypes import *
import ctypes
from PIL import Image, ImageTk
import datetime
from datetime import datetime

splash = Tk()
splash.title("Welcome")
splash.overrideredirect(True)
splash.iconbitmap("TypeBlitz_Icon.ico")
splash.resizable(False, False)
splash.attributes("-topmost", True)

# Get the screen resolution
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

def check_screen_default():
    print("Checking Screen")

    def scheme_first():
        
        def move_app_sec(e):
            hdroot_sec.geometry(f"+{e.x_root}+{e.y_root}")
    
        global hdroot_sec
        hdroot_sec = Tk()
        bgcolor="#6e83b7"
        hdroot_sec.config(bg=bgcolor)
        hdroot_sec.title("TypeBlitz")
        hdroot_sec.overrideredirect(True)
        hdroot_sec.iconbitmap("TypeBlitz_Icon.ico")
        hdroot_sec.resizable(False, False)
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        screen_widthhd = hdroot_sec.winfo_screenwidth()
        screen_heighthd = hdroot_sec.winfo_screenheight()
        
        if screen_width == 1366:
            hdroot_sec.geometry("1280x700+30+26")
        elif screen_width == 1360:
            hdroot_sec.geometry("1280x700+18+18")
        elif screen_width == 1280 and screen_heighthd == 960:
            hdroot_sec.geometry("1280x700+0+60")
        elif screen_width == 1280 and screen_heighthd == 800:
            hdroot_sec.geometry("1280x700+0+10")
        elif screen_width == 1280 and screen_heighthd >= 700:
            hdroot_sec.geometry("1280x700+0+0")
        else:
            hdroot_sec.geometry("1280x700+0+0")
        
        def open_web():
            try:
                print("\033[32m ---->> Redirected to Browser\033[0m")
                webbrowser.open("https://sarwanboi.github.io/Skill-Improver.github.io")
            except webbrowser.Error as web_error:
                messagebox.showerror("Web Browser Error", f"Could not open the web page: {web_error}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
                        
        def about_app():
            about_tk = Toplevel(hdroot_sec)
            about_tk.config(bg="#FCFCFC")
            about_tk.geometry("340x230")
            about_tk.title("About")
            about_tk.iconbitmap("TypeBlitz_Icon.ico")
            about_tk.resizable(False, False)
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            acolo = "#EEE"
            half_frame = Frame(about_tk, width=340, height=60, bg=acolo)
            half_frame.place(x=0, y=0)
            ld = Label(half_frame, text="TYPEBLITZ", border=0, background=acolo, fg="#CDCDCD",
                    font=("Calibri (Body)", 20, "bold"))
            ld.place(relx=0.5, rely=0.5, anchor="center")

            labels_data = [
                ("UI:", 26, 80),
                ("1.2", 200, 80),
                ("Version:", 26, 120),
                ("1.8 (Production)", 200, 120),  # Indicate that version 3.6 is the production version
                ("Released Date:", 26, 160),
                ("December 06, 2023", 200, 160),
                ("Developer:", 26, 200),
                ("Sarwan Yadav", 200, 200)
            ]

            for i, (text, x, y) in enumerate(labels_data):
                label = Label(about_tk, text=text, border=0, background="#FCFCFC", fg="#010101",
                            font=("Calibri (Body)", 10, "bold"))
                label.place(x=x, y=y)
                if i % 2 == 1:
                    label = Label(about_tk, text=text, border=0, background="#FCFCFC", fg="#000",
                                font=("Calibri (Body)", 10, "bold"))
                    label.place(x=x, y=y)

            print("\033[34m ---->> About Application\033[0m")
            about_tk.mainloop()
        
        def home_page():
            print("\033[37m -->> Home Page\033[0m")
            default = Frame(hdroot_sec,bg=bgcolor, width=1280, height=700)
            default.pack()
            
            # ***************************************************************************************************************************************************  #
            
            def load_images(image_files):
                images = {}
                try:
                    for file in image_files:
                        with Image.open(file) as img:
                            images[file] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f" -->> \033[37mCache: \033[31mError loading image {file}: {str(e)}")
                    return None
                return images
            image_files = ["TypeBlitz2.png", "exit.png", "TypeBlitz_side.png", "TypeBlitz_side_in_a.png", "TypeBlitz_side_in_b.png", 
                           "button_word.png", "button_paragraph.png", "web.png", "about.png", "update.png"]
            images = load_images(image_files)
            
            # ***************************************************************************************************************************************************  #
            
            la = Label(hdroot_sec, image=images["TypeBlitz2.png"], border=0, background=bgcolor)
            la.place(x=100, y=100)
            
            option = Frame(hdroot_sec, width=500, height=500)
            option.place(x=700, y=100)
            lb = Label(option, image=images["TypeBlitz_side.png"], border=0, background=bgcolor)
            lb.pack()   
            closebtn = Button(option, image=images["exit.png"], background="#466089", activebackground="#466089", command=hdroot_sec.destroy, border=0)
            closebtn.place(x=440, y=10)
            
            option_in_a = Frame(option, width=350, height=210, bg="#466089")
            option_in_a.place(x=75, y=65)
            lc = Label(option_in_a, image=images["TypeBlitz_side_in_a.png"], border=0, background="#466089")
            lc.pack()   
            header = Label(option_in_a, text="Type Test", font=("Helvetica", 17, "bold"), bg="#FFF", fg="#000")
            header.place(x=20, y=24) 
            sub_header = Label(option_in_a, text="Select a Type of Test:", font=("Helvetica", 13), bg="#FFF", fg="#75a7e5")
            sub_header.place(x=26, y=70)
            wordbtn = Button(option_in_a, image=images["button_word.png"], background="#FFF", activebackground="#FFF", border=0)
            wordbtn.place(x=36, y=140)
            parabtn = Button(option_in_a, image=images["button_paragraph.png"], background="#FFF", activebackground="#FFF", border=0)
            parabtn.place(x=176, y=140)
                        
            option_in_b = Frame(option, width=350, height=120, bg="#FFF")
            option_in_b.place(x=75, y=330)
            ld = Label(option_in_b, image=images["TypeBlitz_side_in_b.png"], border=0, background="#466089")
            ld.pack() 
            Webbtn = Button(option_in_b, image=images["web.png"], background="#FFF", activebackground="#FFF", border=0, command=open_web)
            Webbtn.place(x=30, y=35)
            Aboutbtn = Button(option_in_b, image=images["about.png"], background="#FFF", activebackground="#FFF", border=0, command=about_app)
            Aboutbtn.place(x=144, y=35)
            updatebtn = Button(option_in_b, image=images["update.png"], background="#FFF", activebackground="#FFF", border=0)
            updatebtn.place(x=260, y=35)
            
            default.bind("<B1-Motion>", move_app_sec)
            mainloop()
            
            # ***************************************************************************************************************************************************  #
            
        home_page()
        
        hdroot_sec.bind("<B1-Motion>", move_app_sec)
        mainloop()
    
    def splash_screen():
        try:
            gif = Image.open("TypeBlitz.gif")
        except FileNotFoundError:
            messagebox.showerror("File Missing", "The file skill_gif.gif was not found.")
            splash.destroy()
            return
        def animate(frame):
            if gif_label.winfo_exists():
                gif_label.config(image=frames[frame])
                splash.after(40, animate, (frame + 1) % len(frames))
            if frame == len(frames) - 1:
                gifframe.destroy()
                
                close = Label(splash, text="", bg="#FFF", font=("Leelawadee UI", 20), bd=182)
                print("\033[35m -->> Greeting Screen\033[0m")
                if current_hour < 12:
                    close.config(text="Welcome, Good morning", fg="#1E90FF", font=("Leelawadee UI", 20, "bold"))
                elif 12 <= current_hour < 18:
                    close.config(text="Welcome, Good afternoon", fg="#000", font=("Leelawadee UI", 20, "bold"))
                else:
                    close.config(text="Welcome, Good Evening", fg="#FFF", bg="#020202", font=("Leelawadee UI", 20, "bold"))
                close.pack()
                
                def close_splash():
                    gif = None
                    if gif:
                        gif.__del__()
                    else:
                        del gif
                    splash.destroy()
                    scheme_first()
                close.after(3200, close_splash)

        def show_splash():
            print("\033[33m -->> Splash Screen\033[0m")
            # Create a list of PhotoImage objects to store the frames of the GIF
            global frames, gif_label, gifframe
            frames = []
            for frame in range(gif.n_frames):
                gif.seek(frame)
                resized_image = gif.resize((400, 400))
                frames.append(ImageTk.PhotoImage(resized_image))
            # Create a frame and a label to display the GIF
            gifframe = Frame(splash)
            gifframe.pack()
            gif_label = Label(gifframe, image=frames[0], bg="#ccc")
            gif_label.pack()
            # Start the animation
            animate(0)
    
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2
        splash.geometry(f"400x400+{x}+{y}")
        current_hour = int(datetime.now().strftime("%H"))
        show_splash()
        splash.mainloop()

    if screen_height < 700:
        splash.withdraw()
        messagebox.showerror("Display Error", "Unsupported display resolution for application")
        splash.destroy()

    elif screen_width > 1460:
        print("1460")
        print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)

    elif screen_width >= 1360:
        print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)
        splash_screen()
    elif screen_width >= 1280:
        if screen_height == 960:
            print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)
            splash_screen()
        elif screen_height == 800:
            print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)
            splash_screen()
        elif screen_height == 768:
            print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)
            splash_screen()
        elif screen_height == 720:
            print( "\033[32m* Detected Screen Resolution:","\033[32m","\033[31m",screen_width,"\033[37mx\033[31m",screen_height,".\033[0m",)
            splash_screen()
    else:
        splash.withdraw()
        messagebox.showerror("Display Error", "Unsupported display resolution for application")
        splash.destroy()
        
check_screen_default()
