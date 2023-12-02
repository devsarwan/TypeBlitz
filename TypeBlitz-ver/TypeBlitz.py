import tkinter
from tkinter import *
from ctypes import *
import ctypes
from PIL import Image, ImageTk
import datetime
from datetime import datetime

splash = Tk()
splash.title("Welcome")
splash.overrideredirect(True)
splash.iconbitmap("TypeBlitz.ico")
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
        bgcolor="#f3eadd"
        hdroot_sec.config(bg=bgcolor)
        hdroot_sec.title("TypeBlitz")
        hdroot_sec.overrideredirect(True)
        hdroot_sec.iconbitmap("TypeBlitz.ico")
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
