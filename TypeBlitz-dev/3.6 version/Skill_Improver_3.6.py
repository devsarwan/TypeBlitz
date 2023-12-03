import ctypes
import datetime
import os
import random
import re
import sqlite3
import subprocess
import threading
import time
import webbrowser
from ctypes import *
from datetime import datetime
from tkinter import *
from tkinter import PhotoImage, font, messagebox, ttk

import pandas as pd
import requests
import ttkthemes
from PIL import Image, ImageTk
from requests.exceptions import RequestException
from ttkthemes import ThemedStyle

splash = Tk()
splash.title("Welcome")
splash.overrideredirect(True)
splash.iconbitmap("skill.ico")
splash.resizable(False, False)
splash.attributes("-topmost", True)

# Get the screen resolution
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def check_screen():
    print("\033[32m* Detected Screen Resolution:", 
          "\033[32m","\033[31m",
          screen_width, "\033[37mx\033[31m", 
          screen_height,".\033[0m")

    def contion_second():
        ## Main GUI
        global hdroot_sec
        hdroot_sec = Tk()
        bgcolor="#f3eadd"
        hdroot_sec.config(bg=bgcolor)
        hdroot_sec.overrideredirect(True)
        hdroot_sec.iconbitmap("skill.ico")
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
        stop_flag = [True]
        
        def move_app_sec(e):
            hdroot_sec.geometry(f"+{e.x_root}+{e.y_root}")
        
        def on_exit_sec():
            rr = messagebox.askyesno("Exit", "Are you sure you want to exit?")
            if rr:
                hdroot_sec.title("Closing")
                print("\033[31m// Application Closed!!\033[0m")
                hdroot_sec.after(2000,on_operation_complete_sec)
            else:
                pass
        
        def on_operation_complete_sec():
            try:
                print("\033[31m// Exist: TK\033[0m")
                hdroot_sec.destroy()
            except TclError as e:
                if str(e) == "\033[31m// can't invoke \"destroy\" command: application has been destroyed":
                    # Window is already closed or destroyed, no further action needed
                    pass
                else:
                    # Handle other possible errors gracefully
                    print("\033[31m// An error occurred while destroying the tkinter window:", e)
                    # Perform any necessary cleanup or error handling here
            except Exception as e:
                # Handle any other unexpected exceptions
                print("\033[31m// An unexpected error occurred:", e)
                # Perform appropriate error handling or logging here
            finally:
                print("\033[31m// Exist: 0\033[0m")
                os._exit(0)
        
        def open_webiste_sec():
            try:
                print("\033[32m ---->> Redirected to Browser\033[0m")
                webbrowser.open("https://sarwanboi.github.io/Skill-Improver.github.io")
            except webbrowser.Error:
                messagebox.showerror("Error","Could not open the web page. Please check your internet connection and try again.",)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        
        def about_app_sec():
            about_tk = Toplevel(hdroot_sec)
            about_tk.config(bg="#FCFCFC")
            about_tk.geometry("340x230")
            about_tk.title("About")
            about_tk.iconbitmap("skill.ico")
            about_tk.resizable(False, False)
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            acolo = "#EEE"
            half_frame = Frame(about_tk, width=340, height=60, bg=acolo)
            half_frame.place(x=0, y=0)
            ld = Label(half_frame, text="SKILL IMPROVER", border=0, background=acolo, fg="#CDCDCD",
                    font=("Calibri (Body)", 20, "bold"))
            ld.place(relx=0.5, rely=0.5, anchor="center")

            labels_data = [
                ("UI:", 26, 80),
                ("2.8", 200, 80),
                ("Version:", 26, 120),
                ("3.6 (Production)", 200, 120),  # Indicate that version 3.6 is the production version
                ("Released Date:", 26, 160),
                ("November 30, 2023", 200, 160),
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

        
        def app_updator_sec():
            print("\033[33m ---->> Started Updator\033[0m")
                        
            droot = Tk()
            droot.title("Stay Updated - Skill Improver")
            droot.iconbitmap("skill.ico")
            droot.overrideredirect(True)
            droot.geometry("400x350+750+280")
            droot.resizable(False, False)
            droot.attributes("-topmost", True)
            droot.config(bg="#f1f1f1")
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            
            def move_updator(e):
                droot.geometry(f"+{e.x_root}+{e.y_root}")
                            
            # Frame 0
            update_half_frame = Frame(droot, width=400, height=150, background="#1E90FF")    
            update_half_frame.place(x=0, y=0)
            head = Label(update_half_frame, text="STAY UPDATED", borderwidth=0, relief="flat")
            head.configure(foreground="#FCFCFC", background="#1E90FF", font=("Calibri (Body)", 22, "bold"), anchor="center")
            head.place(relx=0.5, rely=0.5, anchor="center")
            cl_btn = Button(update_half_frame, command=droot.destroy)
            cl_btn.configure(fg="#000", bg="#FFF", text="X", border=0, width=4)
            cl_btn.place(x=356,y=10)
            
            # Frame 1
            update_info = Frame(droot, width=400, height=120, background="#f1f1f1")    
            update_info.place(x=0, y=150)
            labeln = Label(master=update_info, text="Press the button to download the latest version", background="#F1F1F1")
            labeln.place(relx=0.5, rely=0.5, anchor="center")
                        
            # Frame 2
            update_half = Frame(droot, width=400, height=80, background="#f1f1f1")    
            update_half.place(x=0, y=270)
            
            def updator_engine():
                print("\033[36m     >> Application Ready For Update\033[0m")
                
                local_version = "3.6.0.0"          
                print("\033[36m     >> Current Application Version:\033[33m", local_version)
                
                def is_uptodated():
                    update_btn.configure(text="", state=DISABLED, cursor="arrow", foreground="#eee", background="#eee")
                    header = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Referer": "https://www.google.com/"
                    }
                    response = requests.get(version_url, headers=header)
                    latest_version = response.text.strip()

                    if latest_version > local_version:
                        print("\033[36m >> Available Application Version:\033[33m", latest_version)

                        def ask_continue():
                            droot.attributes("-topmost", False)
                            msg_box = messagebox.askquestion("Update?", "Are you want to download the latest version?", icon="info")
                            if msg_box == "yes":
                                exe_url = "https://sarwanboi.github.io/Skill-Improver.github.io/redic/download/Skill_Improver%20-%20Setup.exe"
                                headers = {
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                                }

                                try:
                                    def run_download():
                                        droot.lift()
                                        print("\033[35m >> Thread: Threading - Start Download\033[0m")
                                        def install():
                                            droot.destroy()
                                            hdroot_sec.destroy()
                                            os.startfile("Skill_Improver - Setup.exe")
                                            subprocess.run(["taskkill", "/f", "/im", "python.exe"], shell=False)

                                        def complete():
                                            droot.lift()
                                            print(" >> \033[30mOpening the installer... ")
                                            labeln.configure(text="Please wait while opening the installer...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                            droot.lift()
                                            labeln.after(3800, install)

                                        def download(url):
                                            filename = "Skill_Improver - Setup.exe"
                                            headers = {
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                                            }
                                            labeln.configure(text="Downloading...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                            print(" >> \033[37mDownloading...")
                                            response = requests.get(url, headers=headers)
                                            with open(filename, "wb") as f:
                                                f.write(response.content)
                                            os.chmod(filename, 0o644)
                                            droot.lift()
                                            labeln.configure(text="Download Completed", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                            print(" >> \033[33mDownload Completed")
                                            droot.wm_attributes("-topmost", True)
                                            labeln.after(2000, complete)
                                                                        
                                        response = requests.head(exe_url, headers=headers, timeout=30)
                                        response.raise_for_status()

                                        if response.status_code == 301:
                                            new_url = response.headers["Location"]
                                            print(" >> \033[32mRedirection detected. \033[33mNew URL:\033[35m", new_url, "\033[34mStatus:\033[33m", response)
                                            droot.lift()
                                            lsr1 = ("Calibri (Body)", 10, "bold")
                                            labeln.configure(text="Starting download...", foreground="#1E90FF", font=lsr1,)
                                            print(" >> \033[36mStarting download...")
                                            droot.wm_attributes("-topmost", True)
                                            labeln.after(2000, lambda: threading.Thread(target=download, args=(new_url,)).start())
                                        else:
                                            print(" >> \033[31mNo redirection. \033[33mUsing Old Url:\033[36m", exe_url,"\n      \033[34mStatus:\033[33m", response)
                                            droot.lift()
                                            lsr1 = ("Calibri (Body)", 10, "bold")
                                            labeln.configure(text="Starting download...", foreground="#282828", font=lsr1,)
                                            print(" >> \033[36mStarting download...")
                                            droot.wm_attributes("-topmost", True)
                                            labeln.after(2000, lambda: threading.Thread(target=download, args=(exe_url,)).start())
                                                                        
                                    droot.lift()
                                    lsr1 = ("Calibri (Body)", 10, "bold")
                                    labeln.configure(text="Starting download...", foreground="#1E90FF", font=lsr1,)
                                    print(" >> \033[36mStarting download...")
                                    droot.wm_attributes("-topmost", True)
                                    labeln.after(2000, run_download)
                                                                    
                                except RequestException as e:
                                    if hasattr(e, 'response') and e.response.status_code == 404:
                                        print(" >> \033[33mIssue: \033[31mFile not found")
                                        messagebox.showerror("Error", "We were unable to locate the requested file. Please make sure the file still exists and is accessible, and then try again.")
                                    else:
                                        print("\033[31m >> Error: {}".format(e))

                            else:
                                messagebox.showinfo("Return", "You will now return to the application screen")
                                droot.lift()
                                labeln.configure(text="Please wait while closing the updator...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                labeln.after(1400, droot.destroy)
                                                
                        labeln.configure(text="The latest release version \nof the software is now available...", fg="#000")
                        labeln.place(relx=0.5, rely=0.8, anchor="center")
                        labeln.after(2000, ask_continue)
                                                        
                    else:
                        update_half_frame.config(bg="#FCFCFC")
                        update_info.config(bg="#50C878")
                        update_half.config(bg="#50C878")
                        update_btn.config(bg="#50C878")
                        cl_btn.config(bg="#F1F1F1")
                        head.config(fg="#50C878", bg="#FCFCFC", text="Congratulations!")
                        labeln.config(fg="#FFF", text="Your software is up-to-date.\n No New Updates Available.", bg="#50C878", font=("Calibri (Body)", 16, "bold"))
                        labeln.place(relx=0.5, rely=0.8, anchor="center")
                        print("\033[37m >> No new update available.\033[36m The latest version is already installed.")
                        
                version_url = "https://sarwanboi.github.io/Skill-Improver.github.io/redic/download/version.txt"
                header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
                
                try:
                    response = requests.head(version_url, headers=header)
                    print("\033[37m     >> Connection Status:\033[32m   Positive\033[0m")
                    response.raise_for_status()
                    is_uptodated()
                except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
                    droot.withdraw()
                    messagebox.showerror("Connection Error", "Sorry, we're having trouble connecting to the internet. Please check your connection and try again.")
                    print("\033[35m     >> Connection Status:\033[31m   Negative\033[0m")
            
            # Function to check if the local version is up-to-date
            def thread_st():
                print("\033[35m     >> Thread:  Threading Requests\033[0m")
                threading.Thread(target=updator_engine).start()

            update_btn = Button(update_half,border=0,font=("Calibri (Body)", 14, "bold"), text="Update", fg="#FFF", bg="#1E90FF", width=15,command=thread_st)
            update_btn.place(relx=0.5, rely=0.5, anchor="center")

            droot.bind("<B1-Motion>", move_updator)
            droot.mainloop()
        
        def word_page_sec():
            wordbg = "#66a0f8"
            print("\033[37m -->> Word Page\033[0m")
            worddef = Frame(hdroot_sec, width=1800, height=900, background=wordbg)
            worddef.pack()
            
            def history_panel():
                global history_tk, data
                data = None

                def read_file():
                    global data
                    with open("history.txt", "r", encoding="utf-8") as file:
                        data = re.split(r"-{8,}", file.read().strip())
                        
                def highlight_matches(text_widget, search_string):
                    if not search_string.strip():
                        return
                    text_widget.tag_remove("highlight", "1.0", "end")
                    start = "1.0"
                    while True:
                        start = text_widget.search(search_string, start, "end")
                        if not start:
                            break
                        end = f"{start}+{len(search_string)}c"
                        text_widget.tag_add("highlight", start, end)
                        start = end

                def search_records():
                    query = search_entry.get().strip()
                    if not query:
                        results_text.delete("1.0", "end")
                        results_text.insert("end", "Please enter a query to search")
                        return
                    results_text.delete("1.0", "end")
                    results = [record for record in data if query in record]
                    if results:
                        insert_text_and_highlight_matches(results_text, results, query)
                    else:
                        results_text.insert("end", "No results found")

                def search_by_date():
                    query = date_entry.get().strip()
                    if not query:
                        results_text.delete("1.0", "end")
                        results_text.insert("end", "Please enter a query to search")
                        return
                    results_text.delete("1.0", "end")
                    results = [
                        record
                        for record in data
                        if re.search(rf"Date ->> {query}", record)
                    ]
                    if results:
                        insert_text_and_highlight_matches(results_text, results, query)
                        highlight_matches(results_text, rf"Date ->> {query}")
                    else:
                        results_text.insert("end", "No results found")

                def insert_text_and_highlight_matches(
                    result_text, results, search_string
                ):
                    result_text.insert("end", "\n\n".join(results))
                    highlight_matches(result_text, search_string)

                history_tk = ttkthemes.ThemedTk()

                history_tk.get_themes()
                history_tk.set_theme("breeze")
                history_tk.title("Word Challenge- History Panel")
                history_tk.resizable(0, 0)
                history_tk.config(bg="#F2F2F2")
                history_tk.iconbitmap("skill.ico")
                history_tk.geometry("1000x520")
                v_s = ttk.Scrollbar(history_tk)
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
                history_tk.attributes("-topmost", True)
                v_s.pack(side=RIGHT, fill=Y)
                h_s = ttk.Scrollbar(history_tk, orient=HORIZONTAL)
                h_s.pack(side=BOTTOM, fill=X)
                results_frame = Frame(history_tk, bg="#FFF")
                results_frame.place(x=4, y=100)
                f = "'Tahoma',36,'bold'"
                results_label = ttk.Label(history_tk,text="Your Score Records Are Stored Here",font=f,background="#F2F2F2",border=8,foreground="#000")
                results_label.place(x=40, y=32)

                search_frame = Frame(history_tk, bg="#FCFCFC", width=456, height=92)
                search_frame.place(x=530, y=4)

                search_label = ttk.Label(search_frame,text="Search:",font="Tahoma,20,bold",background="#FCFCFC")
                search_label.place(x=10, y=16)
                search_entry = ttk.Entry(search_frame)
                search_entry.place(x=190, y=10)

                search_button = ttk.Button(search_frame, text="Search", command=search_records)
                search_button.place(x=350, y=11)

                date_label = ttk.Label(search_frame,text="by date (DD/MM/YYYY):",font=("Tahoma", 11),border=0,background="#FCFCFC")
                date_label.place(x=10, y=64)

                date_entry = ttk.Entry(search_frame)
                date_entry.place(x=190, y=58)

                date_button = ttk.Button(search_frame, text="Search", command=search_by_date)
                date_button.place(x=350, y=58)
                results_text = Text(results_frame,width=134,height=25,yscrollcommand=v_s.set,xscrollcommand=h_s.set,bd="0",bg="#fff")
                results_text.pack(side=LEFT, fill=BOTH, expand=True, padx=18)
                results_text.tag_configure("highlight", background="yellow")

                v_s.config(command=results_text.yview)
                h_s.config(command=results_text.xview)

                read_file()
                results_text.insert(END, "".join(data))
                history_tk.mainloop()
                
            
            back_img_sec = history_img_sec = wordtext_img = wordtop_img = word_footer_img = word_main_img = word_fr_img = entry_name_img = None

            def destroy_images(*images):
                for image in images:
                    try:
                        if image:
                            count = len(images)
                            print(" -->> \033[30mNumber of images:", count)
                            image.__del__()
                        else:
                            del image
                    except Exception as e:
                        print(f" -->> \033[37mCache: \033[31mError Occurred: \033[35mWORD PAGE", e)
                        
                print(" -->> \033[32mCache Successfully Cleared: \033[33mWORD PAGE")
                
            def returnhome():
                try:
                    destroy_images(back_img_sec, history_img_sec, wordtext_img, wordtop_img, word_footer_img, word_main_img, word_fr_img, entry_name_img)
                    worddef.destroy()
                    print(" -->> \033[35mWORD PAGE: \033[36mReturned To Home Successfully")
                    home_page_sec()
                except Exception as e:
                    print(f" -->> \033[31mAn error occurred while returning to the home page: \033[37m{str(e)}")

            image_files = ["homie.png", "histor.png", "wordtext_lowrel.png", "wordtop_lowrel.png", "wordfooter_lowrel.png", "wordmain_lowrel.png", "wordresult_lowrel.png","textarea_lowrel.png"]
            image_variables = []

            for file in image_files:
                try:
                    with open(file, "rb") as f:
                        image_variables.append(PhotoImage(data=f.read()))
                except FileNotFoundError as e:
                    print(f"Error: File {file} not found.")
                except IOError as e:
                    print(f"Error reading file {file}: {e}")
            try:
                back_img_sec, history_img_sec, wordtext_img, wordtop_img, word_footer_img, word_main_img, word_fr_img, entry_name_img = image_variables
            except ValueError as e:
                print("Error: Incorrect number of images provided.")
            
            words = ['ability','artist','able','about','above','accept','according','account','across','act','action','activity','actually','add','address','administration','admit','adult','affect','after','again','against','age','agency','agent','ago','agree','agreement','ahead','air','all','allow','almost','alone','along','already','also','although','always','American','among','amount','analysis','and','animal','another','answer','any','anyone','anything','appear','apply','approach','area','argue','arm','around','arrive','art','article','artist','as','ask','assume','at','attack','attention','attorney','audience','author','authority','available','avoid','away','baby','back','bad','bag','ball','bank','bar','base','be','beat','beautiful','because','become','bed','before','begin','behavior','behind','believe','benefit','best','better','between','beyond','big','bill','billion','bit','black','blood','blue','board','body','book','born','both','box','boy','break','bring','brother','budget','build','building','business','but','buy','by','call','camera','campaign','can','cancer','candidate','capital','car','card','care','career','carry','case','catch','cause','cell','center','central','century','certain','certainly','chair','challenge','chance','change','character','charge','check','child','choice','choose','church','citizen','city','civil','claim','class','clear','clearly','close','coach','cold','collection','college','color','come','commercial','common','community','company','compare','computer','concern','condition','conference','Congress','consider','consumer','contain','continue','control','cost','could','country','couple','course','court','cover','create','crime','cultural','culture','cup','current','customer','cut','dark','data','daughter','day','dead','deal','death','debate','decade','decide','decision','deep','defense','degree','Democrat','democratic','describe','design','despite','detail','determine','develop','development','die','difference','different','difficult','dinner','direction','director','discover','discuss','discussion','disease','do','doctor','dog','door','down','draw','dream','drive','drop','drug','during','each','early','east','easy','eat','economic','economy','edge','education','effect','effort','eight','either','election','else','employee','end','energy','enjoy','enough','enter','entire','environment','environmental','especially','establish','even','evening','event','ever','every','everybody','everyone','everything','evidence','exactly','example','executive','exist','expect','experience','expert','explain','eye','face','fact','factor','fail','fall','family','far','fast','father','fear','federal','feel','feeling','few','field','fight','figure','fill','film','final','finally','financial','find','fine','finger','finish','fire','firm','first','fish','five','floor','fly','focus','follow','food','foot','for','force','foreign','forget','form','former','forward','four','free','friend','from','front','full','fund','future','game','garden','gas','general','generation','get','girl','give','glass','go','goal','good','government','great','green','ground','group','grow','growth','guess','gun','guy','hair','half','hand','hang','happen','happy','hard','have','he','head','health','hear','heart','heat','heavy','help','her','here','herself','high','him','himself','his','history','hit','hold','home','hope','hospital','hot','hotel','hour','house','how','however','huge','human','hundred','husband','idea','identify','if','image','imagine','impact','important','improve','in','include','including','increase','indeed','indicate','individual','industry','information','inside','instead','institution','interest','interesting','international','interview','into','investment','involve','issue','it','item','its','itself','job','join','just','keep','key','kid','kill','kind','kitchen','know','knowledge','land','language','large','last','late','later','laugh','law','lawyer','lay','lead','leader','learn','least','leave','left','leg','legal','less','let','letter','level','lie','life','light','like','likely','line','list','listen','little','live','local','long','look','lose','loss','lot','love','low','machine','magazine','main','maintain','major','majority','make','man','manage','management','manager','many','market','marriage','material','matter','may','maybe','me','mean','measure','media','medical','meet','meeting','member','memory','mention','message','method','middle','might','military','million','mind','minute','miss','mission','model','modern','moment','money','month','more','morning','most','mother','mouth','move','movement','movie','much','music','must','myself','name','nation','national','natural','nature','near','nearly','necessary','need','network','never','new','news','newspaper','next','nice','night','no','none','nor','north','not','note','nothing','notice','now','number','occur','off','offer','office','officer','official','often','oil','old','on','once','one','only','onto','open','operation','opportunity','option','or','order','organization','other','our','out','outside','over','own','owner','page','pain','Painting','paper','parent','part','participant','particular','particularly','partner','party','pass','past','patient','pattern','pay','peace','people','per','perform','performance','perhaps','period','person','personal','phone','political','politics','poor','popular','population','position','positive','possible','power','quite','race','radio','raise','range','rate','rather','reach','read','ready','real','reality','realize','really','reason','receive','recent','recently','recognize','record','red','reduce','reflect','region','relate','relationship','religious','remain','remember','remove','report','represent','Republican','require','research','resource','respond','response','responsibility','run','safe','same','save','say','scene','school','science','scientist','score','sea','season','seat','second','section','security','see','seek','seem','sell','send','senior','sense','series','serious','serve','service','set','seven','several','shake','share','she','shoot','short','shot','should','shoulder','show','side','sign','significant','similar','simple','simply','since','sing','single','sister','sit','site','situation','six','size','skill','skin','small','smile','so','social','society','soldier','some','somebody','someone','something','sometimes','speech','spend','sport','spring','staff','stage','stand','standard','star','start','state','statement','station','stay','step','still','stock','stop','store','story','strategy','street','strong','structure','student','study','stuff','style','subject','success','successful','such','suddenly','suffer','suggest','summer','support','sure','surface','system','table','take','talk','task','tax','teach','teacher','team','technology','television','tell','ten','tend','term','test','than','thank','thing','think','third','this','those','though','thought','thousand','threat','three','through','throughout','throw','thus','time','to','today','together','tonight','too','top','total','tough','toward','town','trade','traditional','training','travel','treat','treatment','tree','trial','trip','trouble','true','truth','try','turn','TV','two','type','under','understand','unit','until','up','upon','us','use','usually','value','various','very','victim','view','violence','visit','voice','vote','wait','weapon','wear','week','weight','well','west','western','what','whatever','when','where','whether','whose','why','wide','wife','will','win','wind','window','wish','with','within','without','woman','wonder','word','work','worker','world','worry','would','write','writer','wrong','yard','yeah','year','yes','yet','you','young','your','yourself']
            global score, miss, current_word, total_words, mistakes, wrong_words, timer
            
            def time_io():
                global timer, score, miss, total_words, mistakes, wrong_words
                if timer > 30:
                    pass
                else:
                    timerlabelcount.configure(fg="orange")
                if timer > 11:
                    pass
                else:
                    timerlabelcount.configure(fg="red")
                if timer > 0:
                    timer -= 1
                    timerlabelcount.configure(text=timer)
                    Accuracy_Result.config(fg="#282C34")
                    word_per_m_Result.config(fg="#282C34")
                    Hit_Result.config(fg="#282C34")
                    Miss_Result.config(fg="#282C34")
                    Tscore_Result.config(fg="#282C34")
                    timerlabelcount.after(1000, time_io)
                else:
                    accuracy = (
                        (total_words - mistakes) / total_words * 100
                        if total_words > 0
                        else 0
                    )
                    wpm = int(score / 0.5)
                    resul = score - miss
                    if score == resul:
                        startlabel.configure(text="Well Done Buddy", fg="#60ee6a", font=("Calibri (Body)", 12, "bold"))
                    else:
                        startlabel.configure(text="You Can Try Better", fg="lightgrey",font=("Calibri (Body)", 12, "bold"))

                    fscore = score - miss
                    faccuracy = f"{accuracy:.2f}"
                    Accuracy_Result.configure(text="{}%".format(faccuracy), fg="blue")
                    word_per_m_Result.configure(text=wpm, fg="blue")
                    Hit_Result.configure(text=score, fg="#60ee6a")
                    Miss_Result.configure(text=miss, fg="#60ee6a")
                    Tscore_Result.configure(text=fscore, fg="#60ee6a")
                    
                    TimeVar = time.strftime("%I:%M:%S %p")
                    full_date = time.localtime()
                    day = str(full_date.tm_mday)
                    month = str(full_date.tm_mon)
                    year = str(full_date.tm_year)
                    date = ("Date ->> "+ day+ "/" + month + "/" + year + ", " + "Time - " + TimeVar)
                    
                    try:
                        with open("history.txt", "a") as files:
                            files.write(
                                """\n--------        --------        --------        --------        ---------        ---------\n\n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Result ->> Accuracy: {} | WPM: {} |  Hit = {} | Miss = {} | Total Score = {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Wrong Words: {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n""".format(
                                    date,faccuracy,wpm,score,miss,fscore,", ".join(wrong_words),
                                )
                            )
                            print("\033[36m ---->>       File Writtened")
                    except FileNotFoundError:
                        try:
                            with open("history.txt", "w") as files:
                                files.write(
                                    """\n--------        --------        --------        --------        ---------        ---------\n\n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Result ->> Accuracy: {} | WPM: {} |  Hit = {} | Miss = {} | Total Score = {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Wrong Words: {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n""".format(
                                        date,faccuracy,wpm,score,miss,fscore,", ".join(wrong_words),
                                    )
                                )
                            print("\033[36m ---->>       File Created and Written")
                        except Exception as e:
                            print("\033[35m     >> File error:", e)
                    except Exception as e:
                        print("\033[35m     >> File error:", e)

                    
                    rr = messagebox.askretrycancel("Notification", "Wanna Play Again!!!!")
                    if rr == True:
                        score = 0
                        miss = 0
                        timer = 60
                        total_words = 0
                        mistakes = 0
                        wrong_words = []
                        timerlabelcount.configure(text=timer, fg="#60ee6a")
                        wordlabel.configure(text=words[0])
                        scorelabelcount.configure(text=score)
                        startlabel.configure(text="Start Typing", fg="#ccc")
                        Accuracy_Result.config(text="...", fg="#ccc")
                        word_per_m_Result.config(text="...", fg="#ccc")
                        Hit_Result.config(text="...", fg="#ccc")
                        Miss_Result.config(text="...", fg="#ccc")
                        Tscore_Result.config(text="...", fg="#ccc")
                        wordentry.delete(0, END)
                    else:
                        startlabel.configure(text="Closing",fg="lightgrey",font=("Calibri (Body)", 14, "bold") )
                        startlabel.after(2800, returnhome)
                        
            def startgame(event):
                global score, miss, current_word, total_words, mistakes, wrong_words
                if timer == 60:
                    time_io()
               
                if wordentry.get() == current_word:
                    score += 1
                    scorelabelcount.configure(text=score)
                else:
                    miss += 1
                    mistakes += 1
                    wrong_words.append(current_word)
                total_words += 1
                random.shuffle(words)
                current_word = words[0]
                wordlabel.configure(text=current_word)
                wordentry.delete(0, END)

                Accuracy_Result.config(text="...")
                word_per_m_Result.config(text="...")
                Hit_Result.config(text="...")
                Miss_Result.config(text="...")
                Tscore_Result.config(text="...")
                startlabel.configure(text="Give Your Best")
              
            
            score = 0
            miss = 0
            timer = 60
            count = 0

            current_word = ""
            score = 0
            mistakes = 0
            wpm = 0
            total_words = 0
            wrong_words = []

            word_footer = Frame(worddef, width=440, height=200)
            word_footer.config(bg="#fff")
            word_footer.place(x=35, y=50)
            p0 = Label(word_footer, image=word_footer_img, border=0, background=wordbg)
            p0.pack()

            backbtn = Button(word_footer)
            backbtn.configure(image=back_img_sec, background="#FFF", activebackground="#FFF", command=returnhome, border=0)
            backbtn.place(x=90, y=80)
            historybtn = Button(word_footer)
            historybtn.configure(image=history_img_sec, background="#FFF", activebackground="#FFF", command=history_panel, border=0)
            historybtn.place(x=300, y=80)
            
            word_main = Frame(worddef, width=720, height=600)
            word_main.config(bg="#FFF")
            word_main.place(x=530, y=50)
            pb = Label(word_main, image=word_main_img, border=0, background=wordbg)
            pb.pack()
            
            word_top = Frame(word_main, width=640, height=240)
            word_top.config(bg="#eeeae7")
            word_top.place(x=40, y=40)
            p1 = Label(word_top, image=wordtop_img, border=0, background="#FFF")
            p1.pack()
            
            reporthead = Label(word_top,text="Report",font=("Calibri (Body)", 20, "bold"),fg="#000",bg="#eeeae7",border=0,)
            reporthead.place(x=40, y=20)
            scorelabel = Label(word_top,text="Your Score:",font=("Calibri (Body)", 12, "bold"),fg="#282C34",bg="#eeeae7",border=0,)
            scorelabel.place(x=40,y=100)
            scorelabelcount = Label(word_top,text=score,font=("Calibri (Body)", 12, "bold"),fg="#66a0f8",bg="#eeeae7")
            scorelabelcount.place(x=170,y=100)
            timerlabel = Label(word_top,text="Time Left:",font=("Calibri (Body)", 12, "bold"),fg="#282C34",bg="#eeeae7")
            timerlabel.place(x=39,y=140)
            timerlabelcount = Label(word_top,text=timer,font=("Calibri (Body)", 12, "bold"),fg="#60ee6a",bg="#eeeae7")
            timerlabelcount.place(x=170,y=140)
            msg = Label(word_top,text="Message: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#eeeae7")
            msg.place(x=40,y=180)
            startlabel = Label(word_top,text="Start Typing",font=("Calibri (Body)", 12, "bold"),bg="#eeeae7",fg="#ccc",)
            startlabel.place(x=170,y=180)
            
            wordframe = Frame(word_top, width=280, height=200)
            wordframe.config(bg="#FFF")
            wordframe.place(x=340, y=20)
            pwt = Label(wordframe, image=wordtext_img, border=0, background="#eeeae7")
            pwt.pack()
            
            wordhead = Label(wordframe,text="Write This Word",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#FFF")
            wordhead.place(x=20, y=30)
            wordheads = Label(wordframe,text="In Entry Box",font=("Calibri (Body)", 14, "bold"),foreground="#282C34",background="#FFF")
            wordheads.place(x=20, y=60)
            wordlabel = Label(wordframe,text=words[0],font=("Calibri (Body)", 16, "bold"),foreground="grey",background="#FFF")
            wordlabel.place(x=20, y=120)
            
            word_fr = Frame(worddef, width=440, height=340)
            word_fr.config(bg="#fff")
            word_fr.place(x=35, y=310)
            pa = Label(word_fr, image=word_fr_img, border=0, background=wordbg)
            pa.pack()
            
            resultframe = Frame(word_fr, width=360, height=280)
            resultframe.config(bg="#fff")
            resultframe.place(x=40, y=30)
            
            resultheading = Label(resultframe,text="Result",font=("Calibri (Body)", 28, "bold"),fg="#007bff",bg="#FFF",border=0)
            resultheading.place(x=15, y=10)

            Accuracy_Label = Label(resultframe,text="Accuracy: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#fff")
            Accuracy_Result = Label(resultframe,text="0",font=("Calibri (Body)", 12, "bold"),foreground="#ccc",background="#fff")
            word_per_m_Label = Label(resultframe,text="WPM: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#fff")
            word_per_m_Result = Label(resultframe,text="0",font=("Calibri (Body)", 12, "bold"),foreground="#ccc",background="#fff")

            Accuracy_Label.place(x=15, y=80)
            Accuracy_Result.place(x=200, y=80)
            word_per_m_Label.place(x=15, y=120)
            word_per_m_Result.place(x=200, y=120)

            Hit_Label = Label(resultframe,text="Hit: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#fff")
            Hit_Result = Label(resultframe,text="0",font=("Calibri (Body)", 12, "bold"),foreground="#ccc",background="#fff")
            Miss_Label = Label(resultframe,text="Miss: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#fff")
            Miss_Result = Label(resultframe,text="0",font=("Calibri (Body)", 12, "bold"),foreground="#ccc",background="#fff")
            Tscore_Label = Label(resultframe,text="Total: ",font=("Calibri (Body)", 12, "bold"),foreground="#282C34",background="#fff")
            Tscore_Result = Label(resultframe,text="0",font=("Calibri (Body)", 12, "bold"),foreground="#ccc",background="#fff")

            Hit_Label.place(x=15, y=160)
            Hit_Result.place(x=200, y=160)
            Miss_Label.place(x=15, y=200)
            Miss_Result.place(x=200, y=200)
            Tscore_Label.place(x=14, y=240)
            Tscore_Result.place(x=200, y=240)
            
            entry_frame = Frame(word_main, bg="#fff", width=320, height=70)
            entry_frame.place(x=180, y=440)
            entry_image = Label(entry_frame, image=entry_name_img, border=0)
            entry_image.config(bg="#FFF")
            wordentry = Entry(word_main, width=12, border=0, font=("bold", 36),justify='center')
            wordentry.config(bg="#eeeae7", fg="#000")
            entry_image.grid()
            wordentry.place(x=198, y=450)
            
            wordentry.focus_set()
            wordentry.bind("<Return>", startgame)
            worddef.mainloop()
        
        def para_page_sec():
            print("\033[37m -->> Paragraph Page\033[0m") 
            def para_history_panel():
                print("\033[35m ---->>       Paragraph Challenge: Stats Viewer")
                # Check if the database file exists
                if not os.path.exists("typing_stats.db"):
                    # Create the database file and table
                    print("\033[33m ---->>       Checking if the database file exists...")
                    print("\033[31m ---->>       No database file exists:\033[32m TRUE")
                    print("\033[32m ---->>       Connecting to sqlite3 for databse creation.")
                    conn = sqlite3.connect("typing_stats.db")
                    conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                    print("\033[36m ---->>       DATABASE CREATED SUCCESSFULLY")
                    print("\033[36m ---->>       TABLE CREATED SUCCESFULLY INTO DATBASE")
                    conn.close()
                    print("\033[31m ---->>       Connection Closed Successfulyy")
                #else:
                    #print("\033[31m ---->>       database file already exists:\033[32m TRUE")

                def show_data(sort_column=None, reverse_sort=False):
                    try:
                        # Connect to the database
                        conn = sqlite3.connect("typing_stats.db")
                        # Fetch data from the table
                        df = pd.read_sql_query("SELECT * FROM typing_stats", conn)
                        # Close the connection
                        conn.close()

                        # Filter data based on search query
                        search_query = search_box.get()
                        if search_query:
                            df = df[
                                df.astype(str)
                                .apply(
                                    lambda x: x.str.contains(
                                        search_query, case=False, regex=False
                                    )
                                )
                                .any(axis=1)
                            ]

                        # Sort data based on sort_column and reverse_sort parameters
                        if sort_column:
                            df = df.sort_values(by=sort_column, ascending=not reverse_sort)

                        # Display the data in a table
                        tree.delete(*tree.get_children())
                        if len(df) == 0:
                            tree.insert("","end",text="No results found",values=("No results","No results","No results","No results","No results","No results","No results","No results"))
                        else:
                            tree["column"] = list(df.columns)
                            tree["show"] = "headings"
                            for column in tree["columns"]:
                                if column == "#0":
                                    tree.column(column, width=0, stretch=False)
                                elif column == "date":
                                    tree.column(column, width=100, anchor="center")
                                else:
                                    tree.column(column, width=100, anchor="center")
                                tree.heading(column,text=column,command=lambda c=column: show_data(sort_column=c, reverse_sort=not reverse_sort))
                        
                            df_rows = df.to_numpy().tolist()
                            for row in df_rows:
                                values = tuple(
                                    [
                                        f"[{search_query}]" in str(value).lower()
                                        and value
                                        or value
                                        for value in row
                                    ]
                                )
                                tree.insert("", "end", values=values)
                                if search_query:
                                    for i, value in enumerate(row):
                                        if search_query.lower() in str(value).lower():
                                            tree.item(
                                                tree.get_children()[
                                                    len(tree.get_children()) - 1
                                                ],
                                                tags=("highlight",),
                                            )
                                            tree.tag_configure(
                                                "highlight", background="yellow"
                                            )
                                            break
                            tree.tag_configure("highlight", background="yellow")
                    except sqlite3.Error as e:
                        print(f"\033[33m ---->>       Error connecting to database: {e}")

                # Create the main window
                global root
                root = Tk()
                root.title("Paragraph Challenge: Stats Viewer")
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
                root.minsize(788, 680)
                root.maxsize(788, 680)
                # theme
                style = ThemedStyle(root)
                style.set_theme("breeze")
                root.attributes("-topmost", True)
                # Create a label and search box
                search_label = ttk.Label(root, text="Search by date:")
                search_label.grid(row=0, column=0, padx=10, pady=10)
                search_box = ttk.Entry(root)
                search_box.grid(row=0, column=1, padx=10, pady=10)
                # search button
                search_button = ttk.Button(root, text="Search", command=show_data, style="TButton", width=20)
                search_button.grid(row=0, column=2, padx=10, pady=10)
                # button to quit the program
                quit_button = ttk.Button(root, text="Quit", command=root.destroy, style="TButton", width=20)
                quit_button.grid(row=0, column=3, padx=10, pady=10)
                # treeview to display the data
                tree = ttk.Treeview(root)
                tree.grid(row=1, column=0, padx=10, pady=10, columnspan=4, sticky="NSEW")
                scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
                scrollbar.grid(row=1, column=4, sticky="NS")
                tree.configure(yscrollcommand=scrollbar.set)
                # Configure the row and column weights to make the treeview and scrollbar expand along with the window
                root.columnconfigure(0, weight=1)
                root.columnconfigure(1, weight=1)
                root.columnconfigure(2, weight=1)
                root.columnconfigure(3, weight=1)
                root.rowconfigure(1, weight=1)
                # Display the data in the table
                show_data()
                # Run the main event loop
                root.mainloop()
                    
            global stop_event, timer_thread, count_thread, totaltime, timing, wrongwords, elapsedtimeinminutes, textarea

            stop_event = threading.Event()
            totaltime = 60
            timing = 0
            wrongwords = 0
            elapsedtimeinminutes = 0
            timer_thread = None
            count_thread = None
            
            def start_timer(stop_flag):
                    global timing, totaltime, textarea  # Add textarea to the global scope 
                    backbtn.config(state=DISABLED) 
                    startButton.config(state=DISABLED)
                    historybtn.config(state=DISABLED)
                    textarea.config(state=NORMAL)
                    textarea.focus()

                    timing += 1
                    elapsed_timer_label.config(text=timing)
                    remaining_timer_label.config(text=totaltime - timing)

                    if timing < totaltime:
                        paradef.after(1000, start_timer, stop_flag)
                    else:
                        textarea.config(state=DISABLED)
                        resetButton.config(state=NORMAL)
                        historybtn.config(state=NORMAL)
                        backbtn.config(state=NORMAL)


            def count(stop_flag):  # Remove the textarea parameter
                while stop_flag[0]:
                    global wrongwords, timing, totaltime, elapsedtimeinminutes, textarea  # Add textarea to the global scope
                    while timing != totaltime:
                        try:
                            entered_paragraph = textarea.get(1.0, END).split()
                        except Exception as Er_para:
                            print(Er_para)
                        totalwords = len(entered_paragraph)

                    totalwords_count_label.config(text=totalwords)
                    para_word_list = label_paragraph["text"].split()

                    for pair in list(zip(para_word_list, entered_paragraph)):
                        if pair[0] != pair[1]:
                            wrongwords += 1

                    wrongwords_count_label.config(text=wrongwords)

                    elapsedtimeinminutes = timing / 60
                    wpm = (totalwords - wrongwords) / elapsedtimeinminutes
                    wpm_count_label.config(text=wpm)
                    gross_wpm = totalwords / elapsedtimeinminutes
                    if gross_wpm != 0:
                        accuracy = wpm / gross_wpm * 100
                    else:
                        accuracy = 0
                    accuracy = round(accuracy)
                    accuracy_percent_label.config(text=str(accuracy) + "%")
                    msg_labrl.configure(text="Your result is ready. Use the reset button to reset.")
                    resetButton.config(state=NORMAL)
                    textarea.config(state=DISABLED)
                    
                    db_file = "typing_stats.db"

                    if not os.path.exists(db_file):
                        conn = sqlite3.connect(db_file)
                        conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                        conn.close()

                    try:
                        conn = sqlite3.connect(db_file)

                        # Check if the table already exists
                        cursor = conn.cursor()
                        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='typing_stats'")
                        table_exists = cursor.fetchone()

                        if not table_exists:
                            conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

                        accuracy = 0.95  # Example values for accuracy, wpm, gross_wpm, totalwords, and wrongwords
                        wpm = 60
                        gross_wpm = 65
                        totalwords = 100
                        wrongwords = 5

                        conn.execute("INSERT INTO typing_stats (ACCURACY, WPM, GROSS_WPM, TOTAL_WORDS, WRONG_WORDS) VALUES (?, ?, ?, ?, ?)",
                                    (accuracy, wpm, gross_wpm, totalwords, wrongwords))

                        # Commit changes and close the connection
                        conn.commit()
                        conn.close()
                        print("     >>  Data Written.")
                    except sqlite3.Error as e:
                        print("     >>  An error occurred:", e)
                    break  

            def start():
                msg_labrl.configure(text="")
                stop_flag = [True]  # Create a stop flag
                
                start_threads(stop_flag, textarea)  # Pass the textarea variable to start_threads


            def start_threads(stop_flag, textarea):  # Add textarea as a parameter
                try:
                    global timer_thread, count_thread
                    timer_thread = threading.Thread(target=start_timer, args=(stop_flag,))
                    count_thread = threading.Thread(target=count, args=(stop_flag,))
                    timer_thread.start()
                    count_thread.start()
                except Exception as e:
                    print("An error occurred:", e)


            def stop_threads(stop_flag):
                try:
                    stop_flag[0] = False
                    stop_event.set()
                    destroy_images(para_main_img, para_footer_img, para_back_img, para_history_img, para_result_img, para_mid_img,
                                para_graph_main_img, result_frame_img, textarea_img)
                    paradef.destroy()
                    print(" -->> \033[35mPARAGRAPH PAGE: \033[36mReturned To Home Successfully")
                    home_page_sec()
                except Exception as e:
                    print("An error occurred:", e)


            def reset():
                global timing, elapsedtimeinminutes, wrongwords
                timing = elapsedtimeinminutes = wrongwords = 0
                startButton.config(state=NORMAL)
                resetButton.config(state=DISABLED)
                textarea.config(state=NORMAL)
                textarea.delete(1.0, END)
                textarea.config(state=DISABLED)
                historybtn.config(state=NORMAL)
                msg_labrl.configure(text="Click start and type the above text here:")
                elapsed_timer_label.config(text="0")
                remaining_timer_label.config(text="0")
                wpm_count_label.config(text="...", fg="#282828")
                accuracy_percent_label.config(text="...", fg="#282828")
                totalwords_count_label.config(text="...", fg="#282828")
                wrongwords_count_label.config(text="...", fg="#282828")
            
            def destroy_images(*images):
                for image in images:
                    try:
                        if image:
                            count = len(images)
                            print(" -->> \033[30mNumber of images:", count)
                            image.__del__()
                        else:
                            del image
                    except Exception as e:
                        print(f" -->> \033[37mCache: \033[31mError Occurred: \033[35mPARAGRAPH PAGE", e)
                        
                print(" -->> \033[32mCache Successfully Cleared: \033[33mPARAGRAPH PAGE")
            
            image_files = ["paramain_lowrel.png","parafooter_lowrel.png", "paraback_lowrel.png", "parahistory_lowrel.png","pararesult_lowrel.png", "paramid_lowrel.png","paragraphmain_lowrel.png","resultframe_lowrel.png","textarea_low.png", "button_start.png", "button_reset.png"]
            
            image_variables = []
            try:
                for file in image_files:
                    with open(file, "rb") as f:
                        image_variables.append(PhotoImage(data=f.read()))

                if len(image_variables) == 11:
                    para_main_img = image_variables[0]
                    para_footer_img = image_variables[1]
                    para_back_img = image_variables[2]
                    para_history_img = image_variables[3]
                    para_result_img = image_variables[4]
                    para_mid_img = image_variables[5]
                    para_graph_main_img = image_variables[6]
                    result_frame_img = image_variables[7]
                    textarea_img = image_variables[8] 
                    para_button_start_img = image_variables[9]
                    para_button_reset_img = image_variables[10]
                    
                else:
                    # Handle the case where the number of images doesn't match the expected number
                    # You can raise an exception or handle the error in an appropriate way
                    raise ValueError("The number of images does not match the expected count.")

            except IOError as e:
                # Handle the case where there is an IO error while reading the image files
                print(f"IO error occurred while reading image files: {str(e)}")

            except Exception as e:
                # Handle any other unexpected exceptions
                print(f"An error occurred: {str(e)}")

            parabg="#eeeae7"
            paradef = Frame(hdroot_sec, bg=bgcolor, width=1800, height=900, background=parabg)
            paradef.pack()
            
            para_main = Frame(hdroot_sec, width=1200, height=620, background=parabg)
            para_main.place(x=40,y=40)
            w0 = Label(para_main, image=para_main_img, border=0, background=parabg)
            w0.pack()
                
            para_footer = Frame(para_main, width=420, height=200, background="#FFF")
            para_footer.place(x=40,y=40)
            w1 = Label(para_footer, image=para_footer_img, border=0, background="#FFF")
            w1.pack()
            
            historybtn = Button(para_footer)
            historybtn.configure(image=para_history_img, background="#eeeae7", activebackground="#eeeae7", command=para_history_panel, border=0)
            historybtn.place(x=280, y=80)
            
            backbtn = Button(para_footer)
            backbtn.configure(image=para_back_img, background="#eeeae7", activebackground="#eeeae7", command=lambda: stop_threads(stop_flag), border=0)
            backbtn.place(x=70, y=80)
            
            para_result = Frame(para_main, width=420, height=280, background="#FFF")
            para_result.place(x=40,y=300)
            w0a = Label(para_result, image=para_result_img, border=0, background="#fff")
            w0a.pack()
            
            para_result_header = Label(para_result,text="Result",font=("Tahoma", 24, "bold"),fg="#000", bg="#eeeae7")
            para_result_header.place(x=43, y=30)

            
            accuracy_label = Label(para_result,text="Accuracy",font=("Tahoma", 12, "bold"),fg="#000",border=0, background="#eeeae7")
            accuracy_label.place(x=45, y=100)
            accuracy_percent_label = Label(para_result,text="...",font=("Tahoma", 12),fg="#282828",border=0, background="#eeeae7")
            accuracy_percent_label.place(x=275, y=100)

            wpm_label = Label(para_result,text="WPM",font=("Tahoma", 12, "bold"),fg="#000",border=0, background="#eeeae7")
            wpm_label.place(x=45, y=140)
            wpm_count_label = Label(para_result,text="...",font=("Tahoma", 12),fg="#282828",border=0, background="#eeeae7")
            wpm_count_label.place(x=275, y=140)

            totalwords_label = Label(para_result,text="Total Words",font=("Tahoma", 12, "bold"),fg="#000",border=0, background="#eeeae7")
            totalwords_label.place(x=45, y=190)
            totalwords_count_label = Label(para_result,text="...",font=("Tahoma", 12),fg="#282828",border=0, background="#eeeae7")
            totalwords_count_label.place(x=275, y=190)

            wrongwords_label = Label(para_result,text="Wrong Words",font=("Tahoma", 12, "bold"),fg="#000",border=0, background="#eeeae7")
            wrongwords_label.place(x=45, y=230)
            wrongwords_count_label = Label(para_result,text="...",font=("Tahoma", 12),fg="#282828",border=0, background="#eeeae7")
            wrongwords_count_label.place(x=275, y=230)
            
            para_mid = Frame(para_main, width=660, height=540, background="#eef8da")
            para_mid.place(x=500,y=40)
            w1a = Label(para_mid, image=para_mid_img, border=0, background="#fff")
            w1a.pack()

            
            paragraph_list = [
                "In recent years, technology has rapidly advanced, changing the way we live our lives. With the rise of smartphones, social media, and streaming services, we have access to more information and entertainment than ever before.",
                "However, with these advancements come new challenges. Many people struggle with addiction to technology, spending hours on their phones or computers each day. This can lead to a lack of real-life social connections and a decrease in mental well-being.",
                "In addition to the effects on individuals, technology also has a significant impact on society as a whole. Social media can be a powerful tool for spreading information and organizing movements, but it can also be used to spread misinformation and hate speech.",
                "Exercise is essential for maintaining physical and mental well-being. Regular exercise can improve cardiovascular health, boost immunity, and increase endorphins, which can reduce stress and improve mood. Exercise also helps to prevent chronic diseases such as diabetes, heart disease, and obesity. It is important to incorporate physical activity into daily life, even if its just a short walk or bike ride.",
                "Meditation is a practice that has been around for centuries and has numerous health benefits. Regular meditation can reduce stress and anxiety, increase focus and concentration, and improve sleep. It can also help to lower blood pressure and reduce symptoms of depression. Meditation can be practiced in various ways, including mindfulness, breathwork, and visualization",
                "Social media has become a ubiquitous part of modern life, and its impact is complex. While it can connect people and promote social causes, it can also contribute to anxiety, depression, and cyberbullying. Social media can also be a platform for misinformation and can lead to addictive behavior. Its important to use social media mindfully and with awareness of its potential impact on mental health.",
                "Getting adequate sleep is crucial for physical and mental health. Sleep deprivation can lead to decreased cognitive function, memory impairment, and an increased risk of accidents. Sleep also plays a vital role in immune function, cardiovascular health, and hormone regulation. Its important to prioritize sleep hygiene, including setting a regular sleep schedule, avoiding screens before bed, and creating a relaxing sleep environment.",
                "The Power of Gratitude: Gratitude is a simple yet powerful practice that can promote well-being and increase happiness. Research shows that practicing gratitude can reduce stress, improve relationships, and increase feelings of satisfaction with life. Gratitude can be practiced in various ways, including journaling, expressing thanks to others, and cultivating a sense of appreciation for the present moment.",
                "Proper nutrition is essential for maintaining overall health and well-being. Eating a balanced diet rich in fruits, vegetables, whole grains, and lean protein can reduce the risk of chronic diseases such as heart disease and diabetes. Its important to limit processed foods, sugary drinks, and excess saturated and trans fats. Proper hydration is also critical for maintaining health and preventing dehydration.",
                "Mental health is just as important as physical health, and its essential to prioritize self-care and seek help when needed. Mental health issues such as depression, anxiety, and stress can affect daily life and overall well-being. Its important to practice self-care activities such as exercise, meditation, and social connection, and to seek professional help when needed.",
                "Climate change is a pressing issue with significant social, environmental, and economic consequences. It can lead to extreme weather events, rising sea levels, and loss of biodiversity. Climate change can also contribute to food and water scarcity and increased public health risks. Its essential to take action to reduce greenhouse gas emissions, increase renewable energy sources, and advocate for policies that prioritize sustainability and climate justice.",
                "Education is a fundamental human right that can transform lives and communities. Access to quality education can lead to improved health outcomes, increased economic opportunities, and greater civic engagement. Education can also promote critical thinking and social awareness, which can lead to positive social change. Its important to advocate for equitable access to education and to prioritize educational opportunities for marginalized communities.",
                "The Impact of Technology: Technology has transformed nearly every aspect of modern life, from communication to work to entertainment. While technology can provide numerous benefits, it",
                "Another issue facing our society today is climate change. As the planet continues to warm, we are seeing more extreme weather events, rising sea levels, and loss of biodiversity. Its crucial that we take action now to reduce our carbon footprint and transition to sustainable energy sources.",
                "One way to combat climate change is through renewable energy, such as wind and solar power. While these technologies have come a long way in recent years, there are still challenges to overcome, such as storage and distribution.",
                "Education is also a key factor in creating a more sustainable future. By teaching children about the environment and the impact of human actions, we can inspire the next generation to make positive changes.",
                'Have you ever heard of the concept of "dad jokes"? Well, I recently decided to try my hand at it and told my wife a joke. I said, "Why did the tomato turn red? Because it saw the salad dressing!" I was expecting her to roll her eyes or at least give me a pity laugh, but instead, she just looked at me confused and said, "I dont get it." I was shocked. I mean, its a classic dad joke! How could she not get it? So, I explained it to her, and after a long pause, she finally let out a little chuckle. I dont know if my dad joke skills are really that bad, or if my wife just has no sense of humor, but either way, I will keep trying. Who knows, maybe one day I will actually get a real laugh out of her!',
                'The hacker deftly typed commands into the virtual console, navigating through layers of firewalls and encryption. The systems defenses were sophisticated, but the hacker was equally skilled. As the virtual environment responded to his commands, he could feel himself getting closer to his objective. Finally, he broke through the final layer of protection and gained access to the systems core. But just as he was about to extract the data he needed, a warning message appeared on the screen: "Intrusion detected. Initiating self-destruct. Panic set in as the hacker tried to stop the countdown, but it was too late. The screen went blank as the virtual environment disintegrated around him.',
            ]
            random.shuffle(paragraph_list)
            
            
            para_graph_main = Frame(para_mid, width=620, height=230, background="#eef8da")
            para_graph_main.place(x=20,y=20)
            w01 = Label(para_graph_main, image=para_graph_main_img, border=0, background="#eef8da")
            w01.pack()
            
            report_frame = Frame(para_graph_main, width=200, height=200, background="#eef8da")
            report_frame.place(x=400,y=15)
            f0 = Label(report_frame, image=result_frame_img, border=0, background="#fff")
            f0.pack()

            para_up_header = Label(report_frame,text="Report",font=("Tahoma", 20, "bold"),fg="#007bff", bg="#eef8da")
            para_up_header.place(x=18, y=20)

            elapsed_time_label = Label(report_frame,text="Elapsed Time:",font=("Tahoma", 11, "bold"),fg="#000",border=0, bg="#eef8da")
            elapsed_time_label.place(x=20, y=85)
            elapsed_timer_label = Label(report_frame, text="0", font=("Tahoma", 11), fg="lightblue", border=0, bg="#eef8da")
            elapsed_timer_label.place(x=160, y=85)

            remaining_time_label = Label(report_frame,text="Remaining Time:",font=("Tahoma", 11, "bold"),fg="#000",border=0, bg="#eef8da")
            remaining_time_label.place(x=20, y=125)
            remaining_timer_label = Label(report_frame, text="60", font=("Tahoma", 11), fg="lightgreen", border=0, bg="#eef8da")
            remaining_timer_label.place(x=160, y=125)
            
            para_graph = Frame(para_graph_main, width=320, height=210, background="#FFF")
            para_graph.place(x=20,y=10)
            
            
            label_paragraph = Label(para_graph,text=paragraph_list[0],wraplength=370,justify=LEFT,font=("arial", 10, "bold"),bd=0,bg="#fff",)
            label_paragraph.pack()
            
            para_entry = Frame(para_mid, width=620, height=230, background="#eef8da")
            para_entry.place(x=20,y=290)
            w02 = Label(para_entry, image=para_graph_main_img, border=0, background="#eef8da")
            w02.pack()
            
            textarea_frame = Frame(para_entry, bg="#eeeae7", width= 370, height=170)
            textarea_frame.place(x=15, y=40)
            te = Label(textarea_frame, image=textarea_img, border=0, background="#FFF")
            te.pack()

            msg_labrl = Label(para_entry)
            msg_labrl.configure(text="Click start and type the above text here:",relief="flat",background="#FFF",foreground="green",border=0,)
            msg_labrl.place(x=15, y=15)

            textarea = Text(textarea_frame,font=("arial", 9, "bold"),width=49,height=9,bd=4,relief=FLAT,wrap="word",bg="#eeeae7",state=DISABLED) 
            textarea.place(x=9,y=14)
            
            start_frame = Frame(para_entry, width=200, height=200, background="#eef8da")
            start_frame.place(x=400,y=15)
            f0a = Label(start_frame, image=result_frame_img, border=0, background="#fff")
            f0a.pack()
    
            startButton = Button(start_frame) 
            startButton.configure(image=para_button_start_img, background="#eef8da", activebackground="#eef8da", command=start, border=0, state=NORMAL)
            startButton.place(x=20, y=45)

            resetButton = Button(start_frame)
            resetButton.configure(image=para_button_reset_img, background="#eef8da", activebackground="#eef8da", state=DISABLED, command=reset,border=0)
            resetButton.place(x=20, y=105)
            
            paradef.bind("<Destroy>", lambda event: stop_threads(stop_flag))
            textarea.focus_set()
            paradef.mainloop()
        
        def home_page_sec():
            #if screen_widthhd > 1366:
                #hdroot.call("tk", "scaling", 1.2)
            print("\033[37m -->> Home Page\033[0m")
            default = Frame(hdroot_sec,bg=bgcolor, width=1280, height=700)
            default.pack()

            def load_images(image_files):
                images = {}
                try:
                    for file in image_files:
                        with Image.open(file) as img:
                            images[file] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                    return None
                return images
            
            image_files = ["cross_lowrel.png","hd_home_bg_lowrel.png","hd_side_home_bg_lowrel.png","hd_home_footer_lowrel.png","mid_up_lowrel.png","web_lowrel.png","about_lowrel.png","update_lowrel.png","text_lowrel.png","header_lowrel.png","button_word_lowrel.png","button_paragraph_lowrel.png"]
            images = load_images(image_files)
            
            def open_word_page():
                nonlocal images
                try:
                    for image in images.values():
                        if image:
                            count = len(images)
                            print(" -->> \033[30mNumber of images:", count)
                            image.__del__()
                        else:
                            del image
                    images = {}
                    print(" -->> \033[32mCache Successfully Cleared: \033[33mHOME-TO-WORD PAGE")
                    default.destroy()
                    word_page_sec()
                
                except Exception as e:
                    print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                    
            def open_para_page():
                nonlocal images
                try:
                    for image in images.values():
                        if image:
                            count = len(images)
                            print(" -->> \033[30mNumber of images:", count)
                            image.__del__()
                        else:
                            del image
                    images = {}
                    print(" -->> \033[32mCache Successfully Cleared: \033[33mHOME-TO-PARAGRAPH PAGE")
                    default.destroy()
                    para_page_sec()
                except Exception as e:
                    print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                            
            print("\033[37m -->> Home Page\033[0m")
            
            home_fr = Frame(default, width=600, height=620)
            home_fr.config(bg="#000")
            home_fr.place(x=40, y=40)
            la = Label(home_fr, image=images["hd_home_bg_lowrel.png"], border=0, background=bgcolor)
            la.pack()
            
            header = Label(home_fr, image=images["header_lowrel.png"], background="#66a0f8", border=0)
            header.place(x=40, y=40)
            
            chos = Label(home_fr, text="SKILL IMPROVER", border=0, background="#fff", fg="#000")
            chos.configure(font=("Calibri (Body)", 28, "bold"))
            chos.place(x=130, y=60)
            
            home_mid = Frame(home_fr, width=520, height=460)
            home_mid.place(x=40, y=140)
            label = Label(home_mid, image=images["text_lowrel.png"], border=0, background="#66a0f8")
            label.pack()
            
            home_up = Frame(default, width=555, height=360)
            home_up.config(bg="#000")
            home_up.place(x=685, y=40)
            lb = Label(home_up, image=images["hd_side_home_bg_lowrel.png"], border=0, background=bgcolor)
            lb.pack()
            
            exit_btn = Button(home_up, image=images["cross_lowrel.png"], background="#FFF", activebackground="#FFF", command=on_exit_sec, border=0)
            exit_btn.place(x=500, y=8)
            
            home_up_mid = Frame(home_up, width=475, height=320)
            home_up_mid.config(bg="#EEE")
            home_up_mid.place(x=40, y=60)
            ld = Label(home_up_mid, image=images["mid_up_lowrel.png"], border=0, background="#FFF")
            ld.pack()
            
            chos = Label(home_up_mid, text="Challenges", border=0, background="#eeeae7", fg="#000")
            chos.configure(font=("Calibri (Body)", 22, "bold"))
            chos.place(x=40, y=30)

            choss = Label(home_up_mid, text="Choose a Challenge Type", border=0, background="#eeeae7", fg="#282C34")
            choss.configure(font=("Calibri (Body)", 12, "bold"))
            choss.place(x=40, y=80)
            
            wordbtn = Button(home_up_mid, image=images["button_word_lowrel.png"], background="#eee", activebackground="#eee", command=open_word_page, border=0)
            wordbtn.place(x=60, y=180)

            parabtn = Button(home_up_mid, image=images["button_paragraph_lowrel.png"], background="#eee", activebackground="#eee", command=open_para_page, border=0)
            parabtn.place(x=280, y=180)

            
            home_footer = Frame(default, width=555, height=200)
            home_footer.config(bg="#000")
            home_footer.place(x=685, y=460)
            lc = Label(home_footer, image=images["hd_home_footer_lowrel.png"], border=0, background=bgcolor)
            lc.pack()
            
            Webbtn = Button(home_footer, image=images["web_lowrel.png"], background="#FFF", activebackground="#FFF", command=open_webiste_sec, border=0)
            Webbtn.place(x=55, y=76)

            Aboutbtn = Button(home_footer, image=images["about_lowrel.png"], background="#FFF", activebackground="#FFF", command=about_app_sec, border=0)
            Aboutbtn.place(x=250, y=76)

            updatebtn = Button(home_footer, image=images["update_lowrel.png"], background="#FFF", activebackground="#FFF", command=app_updator_sec, border=0)
            updatebtn.place(x=440, y=76)
            
            hdroot_sec.bind("<B1-Motion>", move_app_sec)
            hdroot_sec.protocol("WM_DELETE_WINDOW", on_exit_sec)
            hdroot_sec.mainloop()

        
        home_page_sec()
        
    def splash_funcsec():
        try:
            gif = Image.open("skill_gif.gif")
        except FileNotFoundError:
            messagebox.showerror("File Missing", "The file skill_gif.gif was not found.")
            splash.destroy()
            return
        
        def animate(frame):
            if gif_label.winfo_exists():
                gif_label.config(image=frames[frame])
                splash.after(50, animate, (frame + 1) % len(frames))
            if frame == len(frames) - 1:
                gifframe.destroy()
                
                close = Label(splash, text="", bg="#FFF", font=("Leelawadee UI", 20), bd=182)
                print("\033[35m -->> Greeting Screen\033[0m")
                if current_hour < 12:
                    close.config(text="Welcome, Good morning", fg="#1E90FF", font=("Leelawadee UI", 20, "bold"))
                elif 12 <= current_hour < 18:
                    close.config(text="Welcome, Good afternoon", fg="#000", font=("Leelawadee UI", 20, "bold"))
                else:
                    close.config(text="Welcome, Good Evening", fg="#FFF", bg="#000", font=("Leelawadee UI", 20, "bold"))
                close.pack()
                
                def close_splash():
                    gif = None
                    if gif:
                        gif.__del__()
                    else:
                        del gif
                    splash.destroy()
                    contion_second()
                close.after(3800, close_splash)

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
        # Start the main event loop
        splash.mainloop()
            
    if screen_height < 700:
        splash.withdraw()
        messagebox.showerror("Display Error", "Unsupported display resolution for application")
        splash.destroy()
        
    elif screen_width > 1460:
        print("1400")
        def contion_first():
            ## Main GUI
            global hdroot
            hdroot = Tk()
            hdroot.title("Skill Improver")
            bgcolor="#f3eadd"
            hdroot.config(bg=bgcolor)
            hdroot.overrideredirect(True)
            hdroot.iconbitmap("skill.ico")
            hdroot.resizable(False, False)
                    
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
            screen_widthhd = hdroot.winfo_screenwidth()
            stop_flag = [True]
                    
            if screen_width == 1600:
                hdroot.geometry("1800x900+10+10")
            else:
                hdroot.geometry("1800x900+60+40")
                    
            def on_exit():
                rr = messagebox.askyesno("Exit", "Are you sure you want to exit?")
                if rr:
                    hdroot.title("Closing")
                    print("\033[31m// Application Closed!!\033[0m")
                    hdroot.after(2000, on_operation_complete)
                else:
                    pass
                    
            def on_operation_complete():
                try:
                    print("\033[31m// Exist: TK\033[0m")
                    hdroot.destroy()
                except TclError as e:
                    if str(e) == "\033[31m// can't invoke \"destroy\" command: application has been destroyed":
                                # Window is already closed or destroyed, no further action needed
                        pass
                    else:
                        # Handle other possible errors gracefully
                        print("\033[31m// An error occurred while destroying the tkinter window:", e)
                        # Perform any necessary cleanup or error handling here
                except Exception as e:
                    # Handle any other unexpected exceptions
                    print("\033[31m// An unexpected error occurred:", e)
                    # Perform appropriate error handling or logging here
                finally:
                    print("\033[31m// Exist: 0\033[0m")
                    os._exit(0)
                    
            def move_app(e):
                hdroot.geometry(f"+{e.x_root}+{e.y_root}")

            def open_webiste():
                try:
                    print("\033[32m ---->> Redirected to Browser\033[0m")
                    webbrowser.open("https://sarwanboi.github.io/Skill-Improver.github.io")
                except webbrowser.Error:
                    messagebox.showerror("Error","Could not open the web page. Please check your internet connection and try again.",)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            def about_app():
                about_tk = Toplevel(hdroot)
                about_tk.config(bg=bgcolor)
                about_tk.geometry("460x400")
                about_tk.title("About")
                about_tk.iconbitmap("skill.ico")
                about_tk.resizable(False, False)
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
                
                half_frame = Frame(about_tk, width=440, height=120, bg="#000")
                half_frame.place(x=0, y=0)
                ld = Label(half_frame, text="SKILL IMPROVER", border=0, background="#000", fg="#FFF", font=("Calibri (Body)", 24, "bold"))
                ld.place(relx=0.5, rely=0.5, anchor="center")

                labels_data = [
                    ("UI:", 26, 160),
                    ("2.8", 280, 160),
                    ("Version:", 26, 220),
                    ("3.6 (Production)", 280, 220),
                    ("Released Date:", 26, 280),
                    ("November 30, 2023", 280, 280),
                    ("Developer:", 26, 340),
                    ("Sarwan Yadav", 280, 340)
                ]

                for i, (text, x, y) in enumerate(labels_data):
                    label = Label(about_tk, text=text, border=0, background=bgcolor, fg="#010101", font=("Calibri (Body)", 14, "bold"))
                    label.place(x=x, y=y)
                    if i % 2 == 1:
                        label = Label(about_tk, text=text, border=0, background=bgcolor, fg="#000", font=("Calibri (Body)", 14, "bold"))
                        label.place(x=x, y=y)
                print("\033[34m ---->> About Application\033[0m")
                about_tk.mainloop()
                    
            def app_updator():
                print("\033[33m ---->> Started Updator\033[0m")
                                
                droot = Tk()
                droot.title("Stay Updated - Skill Improver")
                droot.iconbitmap("skill.ico")
                droot.overrideredirect(True)
                droot.geometry("400x350+750+280")
                droot.resizable(False, False)
                droot.attributes("-topmost", True)
                droot.config(bg="#f1f1f1")
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
                
                def move_updator(e):
                    droot.geometry(f"+{e.x_root}+{e.y_root}")
                                
                # Frame 0
                update_half_frame = Frame(droot, width=400, height=150, background="#1E90FF")    
                update_half_frame.place(x=0, y=0)
                head = Label(update_half_frame, text="STAY UPDATED", borderwidth=0, relief="flat")
                head.configure(foreground="#FCFCFC", background="#1E90FF", font=("Calibri (Body)", 22, "bold"), anchor="center")
                head.place(relx=0.5, rely=0.5, anchor="center")
                cl_btn = Button(update_half_frame, command=droot.destroy)
                cl_btn.configure(fg="#000", bg="#FFF", text="X", border=0, width=4)
                cl_btn.place(x=356,y=10)
                
                # Frame 1
                update_info = Frame(droot, width=400, height=120, background="#f1f1f1")    
                update_info.place(x=0, y=150)
                labeln = Label(master=update_info, text="Press the button to download the latest version", background="#F1F1F1")
                labeln.place(relx=0.5, rely=0.5, anchor="center")
                            
                # Frame 2
                update_half = Frame(droot, width=400, height=80, background="#f1f1f1")    
                update_half.place(x=0, y=270)
                
                def updator_engine():
                    print("\033[36m     >> Application Ready For Update\033[0m")
                                    
                    local_version = "3.6.0.0"
                    print("\033[36m     >> Current Application Version:\033[33m", local_version)
                    
                    def is_uptodated():
                        update_btn.configure(text="", state=DISABLED, cursor="arrow", foreground="#eee", background="#eee")
                        header = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Referer": "https://www.google.com/"
                        }
                        response = requests.get(version_url, headers=header)
                        latest_version = response.text.strip()

                        if latest_version > local_version:
                            print("\033[36m >> Available Application Version:\033[33m", latest_version)

                            def ask_continue():
                                droot.attributes("-topmost", False)
                                msg_box = messagebox.askquestion("Update?", "Are you want to download the latest version?", icon="info")
                                if msg_box == "yes":
                                    exe_url = "https://sarwanboi.github.io/Skill-Improver.github.io/redic/download/Skill_Improver%20-%20Setup.exe"
                                    headers = {
                                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                                    }

                                    try:
                                        def run_download():
                                            droot.lift()
                                            print("\033[35m >> Thread: Threading - Start Download\033[0m")
                                            def install():
                                                droot.destroy()
                                                hdroot.destroy()
                                                os.startfile("Skill_Improver - Setup.exe")
                                                subprocess.run(["taskkill", "/f", "/im", "python.exe"], shell=False)

                                            def complete():
                                                droot.lift()
                                                print(" >> \033[30mOpening the installer... ")
                                                labeln.configure(text="Please wait while opening the installer...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                                droot.lift()
                                                labeln.after(3800, install)

                                            def download(url):
                                                filename = "Skill_Improver - Setup.exe"
                                                headers = {
                                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                                                }
                                                labeln.configure(text="Downloading...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                                print(" >> \033[37mDownloading...")
                                                response = requests.get(url, headers=headers)
                                                with open(filename, "wb") as f:
                                                    f.write(response.content)
                                                os.chmod(filename, 0o644)
                                                droot.lift()
                                                labeln.configure(text="Download Completed", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                                print(" >> \033[33mDownload Completed")
                                                droot.wm_attributes("-topmost", True)
                                                labeln.after(2000, complete)
                                                                            
                                            response = requests.head(exe_url, headers=headers, timeout=30)
                                            response.raise_for_status()

                                            if response.status_code == 301:
                                                new_url = response.headers["Location"]
                                                print(" >> \033[32mRedirection detected. \033[33mNew URL:\033[35m", new_url, "\033[34mStatus:\033[33m", response)
                                                droot.lift()
                                                lsr1 = ("Calibri (Body)", 10, "bold")
                                                labeln.configure(text="Starting download...", foreground="#1E90FF", font=lsr1,)
                                                print(" >> \033[36mStarting download...")
                                                droot.wm_attributes("-topmost", True)
                                                labeln.after(2000, lambda: threading.Thread(target=download, args=(new_url,)).start())
                                            else:
                                                print(" >> \033[31mNo redirection. \033[33mUsing Old Url:\033[36m", exe_url,"\n      \033[34mStatus:\033[33m", response)
                                                droot.lift()
                                                lsr1 = ("Calibri (Body)", 10, "bold")
                                                labeln.configure(text="Starting download...", foreground="lightblue", font=lsr1,)
                                                print(" >> \033[36mStarting download...")
                                                droot.wm_attributes("-topmost", True)
                                                labeln.after(2000, lambda: threading.Thread(target=download, args=(exe_url,)).start())
                                                                            
                                        droot.lift()
                                        lsr1 = ("Calibri (Body)", 10, "bold")
                                        labeln.configure(text="Starting download...", foreground="#1E90FF", font=lsr1,)
                                        print(" >> \033[36mStarting download...")
                                        droot.wm_attributes("-topmost", True)
                                        labeln.after(2000, run_download)
                                                                        
                                    except RequestException as e:
                                        if hasattr(e, 'response') and e.response.status_code == 404:
                                            print(" >> \033[33mIssue: \033[31mFile not found")
                                            messagebox.showerror("Error", "We were unable to locate the requested file. Please make sure the file still exists and is accessible, and then try again.")
                                        else:
                                            print("\033[31m >> Error: {}".format(e))

                                else:
                                    messagebox.showinfo("Return", "You will now return to the application screen")
                                    droot.lift()
                                    labeln.configure(text="Please wait while closing the updator...", foreground="#1E90FF", font=("Calibri (Body)", 12, "bold"))
                                    labeln.after(1400, droot.destroy)
                                                    
                            labeln.configure(text="The latest release version \nof the software is now available...", fg="#000")
                            labeln.place(relx=0.5, rely=0.8, anchor="center")
                            labeln.after(2000, ask_continue)
                                                            
                        else:
                            update_half_frame.config(bg="#FCFCFC")
                            update_info.config(bg="#ac86ff")
                            update_half.config(bg="#ac86ff")
                            update_btn.config(bg="#ac86ff")
                            cl_btn.config(bg="#F1F1F1")
                            head.config(fg="#ac86ff", bg="#FCFCFC", text="Congratulations!")
                            labeln.config(fg="#FFF", text="Your software is up-to-date.\n No New Updates Available.", bg="#ac86ff", font=("Calibri (Body)", 16, "bold"))
                            labeln.place(relx=0.5, rely=0.8, anchor="center")
                            print("\033[37m >> No new update available.\033[36m The latest version is already installed.")
                            
                    version_url = "https://sarwanboi.github.io/Skill-Improver.github.io/redic/download/version.txt"
                    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
                    
                    try:
                        response = requests.head(version_url, headers=header)
                        print("\033[37m     >> Connection Status:\033[32m   Positive\033[0m")
                        response.raise_for_status()
                        is_uptodated()
                    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
                        droot.withdraw()
                        messagebox.showerror("Connection Error", "Sorry, we're having trouble connecting to the internet. Please check your connection and try again.")
                        print("\033[35m     >> Connection Status:\033[31m   Negative\033[0m")
                
                # Function to check if the local version is up-to-date
                def thread_st():
                    print("\033[35m     >> Thread:  Threading Requests\033[0m")
                    threading.Thread(target=updator_engine).start()

                update_btn = Button(update_half,border=0,font=("Calibri (Body)", 14, "bold"), text="Update", fg="#FFF", bg="#1E90FF", width=15,command=thread_st)
                update_btn.place(relx=0.5, rely=0.5, anchor="center")

                droot.bind("<B1-Motion>", move_updator)
                droot.mainloop()
                    
            def word_page():
                wordbg = "#ac86ff"
                print("\033[37m -->> Word Page\033[0m")
                worddef = Frame(hdroot, width=1800, height=900, background=wordbg)
                worddef.pack()
                
                def history_panel():
                    global history_tk, data
                    data = None

                    def read_file():
                        global data
                        with open("history.txt", "r", encoding="utf-8") as file:
                            data = re.split(r"-{8,}", file.read().strip())
                            
                    def highlight_matches(text_widget, search_string):
                        if not search_string.strip():
                            return
                        text_widget.tag_remove("highlight", "1.0", "end")
                        start = "1.0"
                        while True:
                            start = text_widget.search(search_string, start, "end")
                            if not start:
                                break
                            end = f"{start}+{len(search_string)}c"
                            text_widget.tag_add("highlight", start, end)
                            start = end

                    def search_records():
                        query = search_entry.get().strip()
                        if not query:
                            results_text.delete("1.0", "end")
                            results_text.insert("end", "Please enter a query to search")
                            return
                        results_text.delete("1.0", "end")
                        results = [record for record in data if query in record]
                        if results:
                            insert_text_and_highlight_matches(results_text, results, query)
                        else:
                            results_text.insert("end", "No results found")

                    def search_by_date():
                        query = date_entry.get().strip()
                        if not query:
                            results_text.delete("1.0", "end")
                            results_text.insert("end", "Please enter a query to search")
                            return
                        results_text.delete("1.0", "end")
                        results = [
                            record
                            for record in data
                            if re.search(rf"Date ->> {query}", record)
                        ]
                        if results:
                            insert_text_and_highlight_matches(results_text, results, query)
                            highlight_matches(results_text, rf"Date ->> {query}")
                        else:
                            results_text.insert("end", "No results found")

                    def insert_text_and_highlight_matches(
                        result_text, results, search_string
                    ):
                        result_text.insert("end", "\n\n".join(results))
                        highlight_matches(result_text, search_string)

                    history_tk = ttkthemes.ThemedTk()

                    history_tk.get_themes()
                    history_tk.set_theme("breeze")
                    history_tk.title("Word Challenge- History Panel")
                    history_tk.resizable(0, 0)
                    history_tk.config(bg="#F2F2F2")
                    history_tk.iconbitmap("skill.ico")
                    history_tk.geometry("1000x520")
                    v_s = ttk.Scrollbar(history_tk)
                    ctypes.windll.shcore.SetProcessDpiAwareness(1)
                    history_tk.attributes("-topmost", True)
                    v_s.pack(side=RIGHT, fill=Y)
                    h_s = ttk.Scrollbar(history_tk, orient=HORIZONTAL)
                    h_s.pack(side=BOTTOM, fill=X)
                    results_frame = Frame(history_tk, bg="#FFF")
                    results_frame.place(x=4, y=100)
                    f = "'Tahoma',36,'bold'"
                    results_label = ttk.Label(history_tk,text="Your Score Records Are Stored Here",font=f,background="#F2F2F2",border=8,foreground="#000")
                    results_label.place(x=40, y=32)

                    search_frame = Frame(history_tk, bg="#FCFCFC", width=456, height=92)
                    search_frame.place(x=530, y=4)

                    search_label = ttk.Label(search_frame,text="Search:",font="Tahoma,20,bold",background="#FCFCFC")
                    search_label.place(x=10, y=16)
                    search_entry = ttk.Entry(search_frame)
                    search_entry.place(x=190, y=10)

                    search_button = ttk.Button(search_frame, text="Search", command=search_records)
                    search_button.place(x=350, y=11)

                    date_label = ttk.Label(search_frame,text="by date (DD/MM/YYYY):",font=("Tahoma", 11),border=0,background="#FCFCFC")
                    date_label.place(x=10, y=64)

                    date_entry = ttk.Entry(search_frame)
                    date_entry.place(x=190, y=58)

                    date_button = ttk.Button(search_frame, text="Search", command=search_by_date)
                    date_button.place(x=350, y=58)
                    results_text = Text(results_frame,width=134,height=25,yscrollcommand=v_s.set,xscrollcommand=h_s.set,bd="0",bg="#fff")
                    results_text.pack(side=LEFT, fill=BOTH, expand=True, padx=18)
                    results_text.tag_configure("highlight", background="yellow")

                    v_s.config(command=results_text.yview)
                    h_s.config(command=results_text.xview)

                    read_file()
                    results_text.insert(END, "".join(data))
                    history_tk.mainloop()
                    
                
                word_footer_img = word_top_img = word_fr_img = word_main_img = back_img = history_img = None

                def destroy_images(*images):
                    for image in images:
                        try:
                            if image:
                                count = len(images)
                                print(" -->> \033[30mNumber of images:", count)
                                image.__del__()
                            else:
                                del image
                        except Exception as e:
                            print(f" -->> \033[37mCache: \033[31mError Occurred: \033[35mWORD PAGE", e)
                            
                    print(" -->> \033[32mCache Successfully Cleared: \033[33mWORD PAGE")
                    
                def returnhome():
                    try:
                        destroy_images(word_footer_img, word_top_img, word_fr_img, word_main_img, back_img, history_img, wordtext_img, entry_name_img)
                        worddef.destroy()
                        print(" -->> \033[35mWORD PAGE: \033[36mReturned To Home Successfully")
                        home_page()
                    except Exception as e:
                        print(f" -->> \033[31mAn error occurred while returning to the home page: \033[37m{str(e)}")

                    
                image_files = ["wordfooter.png", "wordtop.png", "wordresult.png", "wordmain.png", "home_button.png", "history.png", "wordtext.png", "entrybox.png"]
                image_variables = []

                for file in image_files:
                    try:
                        with open(file, "rb") as f:
                            image_variables.append(PhotoImage(data=f.read()))
                    except FileNotFoundError as e:
                        print(f"Error: File {file} not found.")
                    except IOError as e:
                        print(f"Error reading file {file}: {e}")
                try:
                    word_footer_img, word_top_img, word_fr_img, word_main_img, back_img, history_img, wordtext_img, entry_name_img = image_variables
                except ValueError as e:
                    print("Error: Incorrect number of images provided.")
                
                words = ['ability','artist','able','about','above','accept','according','account','across','act','action','activity','actually','add','address','administration','admit','adult','affect','after','again','against','age','agency','agent','ago','agree','agreement','ahead','air','all','allow','almost','alone','along','already','also','although','always','American','among','amount','analysis','and','animal','another','answer','any','anyone','anything','appear','apply','approach','area','argue','arm','around','arrive','art','article','artist','as','ask','assume','at','attack','attention','attorney','audience','author','authority','available','avoid','away','baby','back','bad','bag','ball','bank','bar','base','be','beat','beautiful','because','become','bed','before','begin','behavior','behind','believe','benefit','best','better','between','beyond','big','bill','billion','bit','black','blood','blue','board','body','book','born','both','box','boy','break','bring','brother','budget','build','building','business','but','buy','by','call','camera','campaign','can','cancer','candidate','capital','car','card','care','career','carry','case','catch','cause','cell','center','central','century','certain','certainly','chair','challenge','chance','change','character','charge','check','child','choice','choose','church','citizen','city','civil','claim','class','clear','clearly','close','coach','cold','collection','college','color','come','commercial','common','community','company','compare','computer','concern','condition','conference','Congress','consider','consumer','contain','continue','control','cost','could','country','couple','course','court','cover','create','crime','cultural','culture','cup','current','customer','cut','dark','data','daughter','day','dead','deal','death','debate','decade','decide','decision','deep','defense','degree','Democrat','democratic','describe','design','despite','detail','determine','develop','development','die','difference','different','difficult','dinner','direction','director','discover','discuss','discussion','disease','do','doctor','dog','door','down','draw','dream','drive','drop','drug','during','each','early','east','easy','eat','economic','economy','edge','education','effect','effort','eight','either','election','else','employee','end','energy','enjoy','enough','enter','entire','environment','environmental','especially','establish','even','evening','event','ever','every','everybody','everyone','everything','evidence','exactly','example','executive','exist','expect','experience','expert','explain','eye','face','fact','factor','fail','fall','family','far','fast','father','fear','federal','feel','feeling','few','field','fight','figure','fill','film','final','finally','financial','find','fine','finger','finish','fire','firm','first','fish','five','floor','fly','focus','follow','food','foot','for','force','foreign','forget','form','former','forward','four','free','friend','from','front','full','fund','future','game','garden','gas','general','generation','get','girl','give','glass','go','goal','good','government','great','green','ground','group','grow','growth','guess','gun','guy','hair','half','hand','hang','happen','happy','hard','have','he','head','health','hear','heart','heat','heavy','help','her','here','herself','high','him','himself','his','history','hit','hold','home','hope','hospital','hot','hotel','hour','house','how','however','huge','human','hundred','husband','idea','identify','if','image','imagine','impact','important','improve','in','include','including','increase','indeed','indicate','individual','industry','information','inside','instead','institution','interest','interesting','international','interview','into','investment','involve','issue','it','item','its','itself','job','join','just','keep','key','kid','kill','kind','kitchen','know','knowledge','land','language','large','last','late','later','laugh','law','lawyer','lay','lead','leader','learn','least','leave','left','leg','legal','less','let','letter','level','lie','life','light','like','likely','line','list','listen','little','live','local','long','look','lose','loss','lot','love','low','machine','magazine','main','maintain','major','majority','make','man','manage','management','manager','many','market','marriage','material','matter','may','maybe','me','mean','measure','media','medical','meet','meeting','member','memory','mention','message','method','middle','might','military','million','mind','minute','miss','mission','model','modern','moment','money','month','more','morning','most','mother','mouth','move','movement','movie','much','music','must','myself','name','nation','national','natural','nature','near','nearly','necessary','need','network','never','new','news','newspaper','next','nice','night','no','none','nor','north','not','note','nothing','notice','now','number','occur','off','offer','office','officer','official','often','oil','old','on','once','one','only','onto','open','operation','opportunity','option','or','order','organization','other','our','out','outside','over','own','owner','page','pain','Painting','paper','parent','part','participant','particular','particularly','partner','party','pass','past','patient','pattern','pay','peace','people','per','perform','performance','perhaps','period','person','personal','phone','political','politics','poor','popular','population','position','positive','possible','power','quite','race','radio','raise','range','rate','rather','reach','read','ready','real','reality','realize','really','reason','receive','recent','recently','recognize','record','red','reduce','reflect','region','relate','relationship','religious','remain','remember','remove','report','represent','Republican','require','research','resource','respond','response','responsibility','run','safe','same','save','say','scene','school','science','scientist','score','sea','season','seat','second','section','security','see','seek','seem','sell','send','senior','sense','series','serious','serve','service','set','seven','several','shake','share','she','shoot','short','shot','should','shoulder','show','side','sign','significant','similar','simple','simply','since','sing','single','sister','sit','site','situation','six','size','skill','skin','small','smile','so','social','society','soldier','some','somebody','someone','something','sometimes','speech','spend','sport','spring','staff','stage','stand','standard','star','start','state','statement','station','stay','step','still','stock','stop','store','story','strategy','street','strong','structure','student','study','stuff','style','subject','success','successful','such','suddenly','suffer','suggest','summer','support','sure','surface','system','table','take','talk','task','tax','teach','teacher','team','technology','television','tell','ten','tend','term','test','than','thank','thing','think','third','this','those','though','thought','thousand','threat','three','through','throughout','throw','thus','time','to','today','together','tonight','too','top','total','tough','toward','town','trade','traditional','training','travel','treat','treatment','tree','trial','trip','trouble','true','truth','try','turn','TV','two','type','under','understand','unit','until','up','upon','us','use','usually','value','various','very','victim','view','violence','visit','voice','vote','wait','weapon','wear','week','weight','well','west','western','what','whatever','when','where','whether','whose','why','wide','wife','will','win','wind','window','wish','with','within','without','woman','wonder','word','work','worker','world','worry','would','write','writer','wrong','yard','yeah','year','yes','yet','you','young','your','yourself']
                global score, miss, current_word, total_words, mistakes, wrong_words, timer
                
                def time_io():
                    global timer, score, miss, total_words, mistakes, wrong_words
                    if timer > 30:
                        pass
                    else:
                        timerlabelcount.configure(fg="orange")
                    if timer > 11:
                        pass
                    else:
                        timerlabelcount.configure(fg="red")
                    if timer > 0:
                        timer -= 1
                        timerlabelcount.configure(text=timer)
                        Accuracy_Result.configure(fg="#282C34")
                        word_per_m_Result.configure(fg="#282C34")
                        Hit_Result.configure(fg="#282C34")
                        Miss_Result.configure(fg="#282C34")
                        Tscore_Result.configure(fg="#282C34")
                        timerlabelcount.after(1000, time_io)
                    else:
                        accuracy = (
                            (total_words - mistakes) / total_words * 100
                            if total_words > 0
                            else 0
                        )
                        wpm = int(score / 0.5)
                        resul = score - miss
                        if score == resul:
                            startlabel.configure(text="Well Done Buddy", fg="#60ee6a", font=("Calibri (Body)", 17, "bold"))
                        else:
                            startlabel.configure(text="You Can Try Better", fg="lightgrey",font=("Calibri (Body)", 15, "bold"))

                        fscore = score - miss
                        faccuracy = f"{accuracy:.2f}"
                        Accuracy_Result.configure(text="{}%".format(faccuracy), fg="blue")
                        word_per_m_Result.configure(text=wpm, fg="blue")
                        Hit_Result.configure(text=score, fg="#60ee6a")
                        Miss_Result.configure(text=miss, fg="#60ee6a")
                        Tscore_Result.configure(text=fscore, fg="#60ee6a")

                        
                        #print(f"\033[36m ---->>       //    Accuracy: {accuracy:.2f}% |    WPM: {wpm}\n\033[34m              // Wrong Words: {wrong_words}\n\033[33m              //   Hit = {score} |   Miss = {miss} | Total Score = {fscore}")
                        
                        TimeVar = time.strftime("%I:%M:%S %p")
                        full_date = time.localtime()
                        day = str(full_date.tm_mday)
                        month = str(full_date.tm_mon)
                        year = str(full_date.tm_year)
                        date = ("Date ->> "+ day+ "/" + month + "/" + year + ", " + "Time - " + TimeVar)
                        try:
                            with open("history.txt", "a") as files:
                                files.write(
                                    """\n--------        --------        --------        --------        ---------        ---------\n\n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Result ->> Accuracy: {} | WPM: {} |  Hit = {} | Miss = {} | Total Score = {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Wrong Words: {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n""".format(
                                        date,faccuracy,wpm,score,miss,fscore,", ".join(wrong_words),
                                    )
                                )
                                print("\033[36m ---->>       File Writtened")
                        except FileNotFoundError:
                            try:
                                with open("history.txt", "w") as files:
                                    files.write(
                                        """\n--------        --------        --------        --------        ---------        ---------\n\n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Result ->> Accuracy: {} | WPM: {} |  Hit = {} | Miss = {} | Total Score = {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n    * Wrong Words: {} \n---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ----  ---- ---- ---- ----- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- --\n""".format(
                                            date,faccuracy,wpm,score,miss,fscore,", ".join(wrong_words),
                                        )
                                    )
                                print("\033[36m ---->>       File Created and Written")
                            except Exception as e:
                                print("\033[35m     >> File error:", e)
                        except Exception as e:
                            print("\033[35m     >> File error:", e)

                        
                        rr = messagebox.askretrycancel("Notification", "Wanna Play Again!!!!")
                        if rr == True:
                            score = 0
                            miss = 0
                            timer = 60
                            total_words = 0
                            mistakes = 0
                            wrong_words = []
                            timerlabelcount.configure(text=timer, fg="#60ee6a")
                            wordlabel.configure(text=words[0])
                            scorelabelcount.configure(text=score)
                            startlabel.configure(text="Start Typing", fg="#ccc")
                            Accuracy_Result.config(text="...", fg="#ccc")
                            word_per_m_Result.config(text="...", fg="#ccc")
                            Hit_Result.config(text="...", fg="#ccc")
                            Miss_Result.config(text="...", fg="#ccc")
                            Tscore_Result.config(text="...", fg="#ccc")
                            wordentry.delete(0, END)
                        else:
                            startlabel.configure(text="Closing",fg="lightgrey",font=("Calibri (Body)", 16, "bold") )
                            startlabel.after(2800, returnhome)
                            
                def startgame(event):
                    global score, miss, current_word, total_words, mistakes, wrong_words
                    try:
                        if timer == 60:
                            time_io()
                        if wordentry.get() == current_word:
                            score += 1
                            scorelabelcount.configure(text=score)
                        else:
                            miss += 1
                            mistakes += 1
                            wrong_words.append(current_word)
                        total_words += 1
                        random.shuffle(words)
                        current_word = words[0]
                        wordlabel.configure(text=current_word)
                        wordentry.delete(0, END)
                   
                    except IndexError:
                        # Handle the case when the words list is empty or index out of range
                        current_word = ""
                        wordlabel.configure(text="No words available")
                        wordentry.delete(0, END)
                     
                    startlabel.configure(text="Give Your Best")
                    Accuracy_Result.config(text="...")
                    word_per_m_Result.config(text="...")
                    Hit_Result.config(text="...")
                    Miss_Result.config(text="...")
                    Tscore_Result.config(text="...")
                
                score = 0
                miss = 0
                timer = 60
                count = 0

                current_word = ""
                score = 0
                mistakes = 0
                wpm = 0
                total_words = 0
                wrong_words = []

                word_footer = Frame(worddef, width=640, height=240)
                word_footer.config(bg="#fff")
                word_footer.place(x=60, y=40)
                p0 = Label(word_footer, image=word_footer_img, border=0, background=wordbg)
                p0.pack()

                backbtn = Button(word_footer)
                backbtn.configure(image=back_img, background="#FFF", activebackground="#FFF", command=returnhome, border=0)
                backbtn.place(x=140, y=80)
                historybtn = Button(word_footer)
                historybtn.configure(image=history_img, background="#FFF", activebackground="#FFF", command=history_panel, border=0)
                historybtn.place(x=400, y=80)

                word_fr = Frame(worddef, width=640, height=540)
                word_fr.config(bg="#fff")
                word_fr.place(x=60, y=320)
                pa = Label(word_fr, image=word_fr_img, border=0, background=wordbg)
                pa.pack()

                word_main = Frame(worddef, width=940, height=820)
                word_main.config(bg="#FFF")
                word_main.place(x=820, y=40)
                pb = Label(word_main, image=word_main_img, border=0, background=wordbg)
                pb.pack()

                word_top = Frame(worddef, width=820, height=320)
                word_top.config(bg="#FFF")
                word_top.place(x=880, y=80)
                p1 = Label(word_top, image=word_top_img, border=0, background="#FFF")
                p1.pack()
                
                reporthead = Label(word_top,text="Report",font=("Calibri (Body)", 38, "bold"),fg="#000",bg="#eeeae7",border=0,)
                reporthead.place(x=40, y=20)
                scorelabel = Label(word_top,text="Your Score:",font=("Calibri (Body)", 18, "bold"),fg="#282C34",bg="#eeeae7",border=0,)
                scorelabel.place(x=40,y=140)
                scorelabelcount = Label(word_top,text=score,font=("Calibri (Body)", 18, "bold"),fg="#66a0f8",bg="#eeeae7")
                scorelabelcount.place(x=200,y=140)
                timerlabel = Label(word_top,text="Time Left:",font=("Calibri (Body)", 18, "bold"),fg="#282C34",bg="#eeeae7")
                timerlabel.place(x=39,y=200)
                timerlabelcount = Label(word_top,text=timer,font=("Calibri (Body)", 18, "bold"),fg="#60ee6a",bg="#eeeae7")
                timerlabelcount.place(x=200,y=200)
                msg = Label(word_top,text="Message: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#eeeae7")
                msg.place(x=40,y=260)
                startlabel = Label(word_top,text="Start Typing",font=("Calibri (Body)", 18, "bold"),bg="#eeeae7",fg="#ccc",)
                startlabel.place(x=200,y=260)
                
                wordframe = Frame(word_top, width=390, height=320)
                wordframe.config(bg="#FFF")
                wordframe.place(x=410, y=20)
                pwt = Label(wordframe, image=wordtext_img, border=0, background="#eeeae7")
                pwt.pack()
                
                wordhead = Label(wordframe,text="Write This Word",font=("Calibri (Body)", 28, "bold"),foreground="#282C34",background="#FFF")
                wordhead.place(x=20, y=50)
                wordheads = Label(wordframe,text="In Entry Box",font=("Calibri (Body)", 22, "bold"),foreground="#282C34",background="#FFF")
                wordheads.place(x=20, y=90)
                wordlabel = Label(wordframe,text=words[0],font=("Calibri (Body)", 26, "bold"),foreground="grey",background="#FFF")
                wordlabel.place(x=20, y=180)
                
                resultframe = Frame(word_fr, width=560, height=500)
                resultframe.config(bg="#FFF")
                resultframe.place(x=40, y=30)
                
                resultheading = Label(resultframe,text="Result",font=("Calibri (Body)", 38, "bold"),fg="#007bff",bg="#FFF",border=0)
                resultheading.place(x=40, y=10)

                Accuracy_Label = Label(resultframe,text="Accuracy: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#fff")
                Accuracy_Result = Label(resultframe,text="0",font=("Calibri (Body)", 18, "bold"),foreground="#ccc",background="#fff")
                word_per_m_Label = Label(resultframe,text="WPM: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#fff")
                word_per_m_Result = Label(resultframe,text="0",font=("Calibri (Body)", 18, "bold"),foreground="#ccc",background="#fff")

                Accuracy_Label.place(x=35, y=105)
                Accuracy_Result.place(x=260, y=105)
                word_per_m_Label.place(x=35, y=165)
                word_per_m_Result.place(x=260, y=165)

                Hit_Label = Label(resultframe,text="Hit: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#fff")
                Hit_Result = Label(resultframe,text="0",font=("Calibri (Body)", 18, "bold"),foreground="#ccc",background="#fff")
                Miss_Label = Label(resultframe,text="Miss: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#fff")
                Miss_Result = Label(resultframe,text="0",font=("Calibri (Body)", 18, "bold"),foreground="#ccc",background="#fff")
                Tscore_Label = Label(resultframe,text="Total: ",font=("Calibri (Body)", 18, "bold"),foreground="#282C34",background="#fff")
                Tscore_Result = Label(resultframe,text="0",font=("Calibri (Body)", 18, "bold"),foreground="#ccc",background="#fff")

                Hit_Label.place(x=35, y=265)
                Hit_Result.place(x=260, y=265)
                Miss_Label.place(x=35, y=335)
                Miss_Result.place(x=260, y=335)
                Tscore_Label.place(x=34, y=405)
                Tscore_Result.place(x=260, y=405)

                # Word Entry Box
                entry_frame = Frame(word_main, bg="#eeeae7")
                entry_frame.place(x=180, y=640)

                entry_image = Label(entry_frame, image=entry_name_img, border=0)
                entry_image.config(bg="#FFF")
                wordentry = Entry(word_main, width=18, border=0, font=("bold", 40),justify='center')
                wordentry.config(bg="#eeeae7", fg="#000")
                entry_image.grid()
                wordentry.place(x=199, y=676)

                wordentry.focus_set()
                wordentry.bind("<Return>", startgame)
                worddef.mainloop()

            def para_page():
                print("\033[37m -->> Paragraph Page\033[0m")
                parabg="#9d7ee1"
                paradef = Frame(hdroot, bg=bgcolor, width=1800, height=900, background=parabg)
                paradef.pack()
                
                def para_history_panel():
                    print("\033[35m ---->>       Paragraph Challenge: Stats Viewer")
                    # Check if the database file exists
                    if not os.path.exists("typing_stats.db"):
                        # Create the database file and table
                        print("\033[33m ---->>       Checking if the database file exists...")
                        print("\033[31m ---->>       No database file exists:\033[32m TRUE")
                        print("\033[32m ---->>       Connecting to sqlite3 for databse creation.")
                        conn = sqlite3.connect("typing_stats.db")
                        conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                        print("\033[36m ---->>       DATABASE CREATED SUCCESSFULLY")
                        print("\033[36m ---->>       TABLE CREATED SUCCESFULLY INTO DATBASE")
                        conn.close()
                        print("\033[31m ---->>       Connection Closed Successfulyy")
                    #else:
                        #print("\033[31m ---->>       database file already exists:\033[32m TRUE")

                    def show_data(sort_column=None, reverse_sort=False):
                        try:
                            # Connect to the database
                            conn = sqlite3.connect("typing_stats.db")
                            # Fetch data from the table
                            df = pd.read_sql_query("SELECT * FROM typing_stats", conn)
                            # Close the connection
                            conn.close()

                            # Filter data based on search query
                            search_query = search_box.get()
                            if search_query:
                                df = df[
                                    df.astype(str)
                                    .apply(
                                        lambda x: x.str.contains(
                                            search_query, case=False, regex=False
                                        )
                                    )
                                    .any(axis=1)
                                ]

                            # Sort data based on sort_column and reverse_sort parameters
                            if sort_column:
                                df = df.sort_values(by=sort_column, ascending=not reverse_sort)

                            # Display the data in a table
                            tree.delete(*tree.get_children())
                            if len(df) == 0:
                                tree.insert("","end",text="No results found",values=("No results","No results","No results","No results","No results","No results","No results","No results"))
                            else:
                                tree["column"] = list(df.columns)
                                tree["show"] = "headings"
                                for column in tree["columns"]:
                                    if column == "#0":
                                        tree.column(column, width=0, stretch=False)
                                    elif column == "date":
                                        tree.column(column, width=100, anchor="center")
                                    else:
                                        tree.column(column, width=100, anchor="center")
                                    tree.heading(column,text=column,command=lambda c=column: show_data(sort_column=c, reverse_sort=not reverse_sort))
                            
                                df_rows = df.to_numpy().tolist()
                                for row in df_rows:
                                    values = tuple(
                                        [
                                            f"[{search_query}]" in str(value).lower()
                                            and value
                                            or value
                                            for value in row
                                        ]
                                    )
                                    tree.insert("", "end", values=values)
                                    if search_query:
                                        for i, value in enumerate(row):
                                            if search_query.lower() in str(value).lower():
                                                tree.item(
                                                    tree.get_children()[
                                                        len(tree.get_children()) - 1
                                                    ],
                                                    tags=("highlight",),
                                                )
                                                tree.tag_configure(
                                                    "highlight", background="yellow"
                                                )
                                                break
                                tree.tag_configure("highlight", background="yellow")
                        except sqlite3.Error as e:
                            print(f"\033[33m ---->>       Error connecting to database: {e}")

                    # Create the main window
                    global root
                    root = Tk()
                    root.title("Paragraph Challenge: Stats Viewer")
                    ctypes.windll.shcore.SetProcessDpiAwareness(1)
                    root.minsize(788, 680)
                    root.maxsize(788, 680)
                    # theme
                    style = ThemedStyle(root)
                    style.set_theme("breeze")
                    root.attributes("-topmost", True)
                    # Create a label and search box
                    search_label = ttk.Label(root, text="Search by date:")
                    search_label.grid(row=0, column=0, padx=10, pady=10)
                    search_box = ttk.Entry(root)
                    search_box.grid(row=0, column=1, padx=10, pady=10)
                    # search button
                    search_button = ttk.Button(root, text="Search", command=show_data, style="TButton", width=20)
                    search_button.grid(row=0, column=2, padx=10, pady=10)
                    # button to quit the program
                    quit_button = ttk.Button(root, text="Quit", command=root.destroy, style="TButton", width=20)
                    quit_button.grid(row=0, column=3, padx=10, pady=10)
                    # treeview to display the data
                    tree = ttk.Treeview(root)
                    tree.grid(row=1, column=0, padx=10, pady=10, columnspan=4, sticky="NSEW")
                    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
                    scrollbar.grid(row=1, column=4, sticky="NS")
                    tree.configure(yscrollcommand=scrollbar.set)
                    # Configure the row and column weights to make the treeview and scrollbar expand along with the window
                    root.columnconfigure(0, weight=1)
                    root.columnconfigure(1, weight=1)
                    root.columnconfigure(2, weight=1)
                    root.columnconfigure(3, weight=1)
                    root.rowconfigure(1, weight=1)
                    # Display the data in the table
                    show_data()
                    # Run the main event loop
                    root.mainloop()
                
                def destroy_images(*images):
                    for image in images:
                        try:
                            if image:
                                count = len(images)
                                print(" -->> \033[30mNumber of images:", count)
                                image.__del__()
                            else:
                                del image
                        except Exception as e:
                            print(f" -->> \033[37mCache: \033[31mError Occurred: \033[35mPARAGRAPH PAGE", e)
                            
                    print(" -->> \033[32mCache Successfully Cleared: \033[33mPARAGRAPH PAGE")
                
                image_files = ["paramain.png","parafooter.png", "paraback.png", "parahistory.png","pararesult.png", "paramid.png","paragraphmain.png","resultframe.png","textarea.png"]
                
                image_variables = []
                try:
                    for file in image_files:
                        with open(file, "rb") as f:
                            image_variables.append(PhotoImage(data=f.read()))

                    if len(image_variables) == 9:
                        para_main_img = image_variables[0]
                        para_footer_img = image_variables[1]
                        para_back_img = image_variables[2]
                        para_history_img = image_variables[3]
                        para_result_img = image_variables[4]
                        para_mid_img = image_variables[5]
                        para_graph_main_img = image_variables[6]
                        result_frame_img = image_variables[7]
                        textarea_img = image_variables[8]
                    else:
                        # Handle the case where the number of images doesn't match the expected number
                        # You can raise an exception or handle the error in an appropriate way
                        raise ValueError("The number of images does not match the expected count.")

                except IOError as e:
                    # Handle the case where there is an IO error while reading the image files
                    print(f"IO error occurred while reading image files: {str(e)}")

                except Exception as e:
                    # Handle any other unexpected exceptions
                    print(f"An error occurred: {str(e)}")

                
                para_main = Frame(hdroot, width=1680, height=780, background=parabg)
                para_main.place(x=60,y=60)
                w0 = Label(para_main, image=para_main_img, border=0, background=parabg)
                w0.pack()
                    
                para_footer = Frame(para_main, width=520, height=240, background="#FFF")
                para_footer.place(x=60,y=60)
                w1 = Label(para_footer, image=para_footer_img, border=0, background="#FFF")
                w1.pack()
                
                historybtn = Button(para_footer)
                historybtn.configure(image=para_history_img, background="#eeeae7", activebackground="#eeeae7", command=para_history_panel, border=0)
                historybtn.place(x=358, y=80)
                
                para_result = Frame(para_main, width=520, height=380, background="#FFF")
                para_result.place(x=60,y=360)
                w0a = Label(para_result, image=para_result_img, border=0, background="#fff")
                w0a.pack()
                
                para_result_header = Label(para_result,text="Result",font=("Tahoma", 34, "bold"),fg="#000", bg="#eeeae7")
                para_result_header.place(x=43, y=40)

                
                accuracy_label = Label(para_result,text="Accuracy",font=("Tahoma", 16, "bold"),fg="#000",border=0, background="#eeeae7")
                accuracy_label.place(x=45, y=120)
                accuracy_percent_label = Label(para_result,text="...",font=("Tahoma", 16),fg="#282828",border=0, background="#eeeae7")
                accuracy_percent_label.place(x=275, y=120)

                wpm_label = Label(para_result,text="WPM",font=("Tahoma", 16, "bold"),fg="#000",border=0, background="#eeeae7")
                wpm_label.place(x=45, y=180)
                wpm_count_label = Label(para_result,text="...",font=("Tahoma", 16),fg="#282828",border=0, background="#eeeae7")
                wpm_count_label.place(x=275, y=180)

                totalwords_label = Label(para_result,text="Total Words",font=("Tahoma", 16, "bold"),fg="#000",border=0, background="#eeeae7")
                totalwords_label.place(x=45, y=240)
                totalwords_count_label = Label(para_result,text="...",font=("Tahoma", 16),fg="#282828",border=0, background="#eeeae7")
                totalwords_count_label.place(x=275, y=240)

                wrongwords_label = Label(para_result,text="Wrong Words",font=("Tahoma", 16, "bold"),fg="#000",border=0, background="#eeeae7")
                wrongwords_label.place(x=45, y=300)
                wrongwords_count_label = Label(para_result,text="...",font=("Tahoma", 16),fg="#282828",border=0, background="#eeeae7")
                wrongwords_count_label.place(x=275, y=300)
                
                para_mid = Frame(para_main, width=980, height=680, background="#CCC")
                para_mid.place(x=640,y=60)
                w1a = Label(para_mid, image=para_mid_img, border=0, background="#fff")
                w1a.pack()
                
                global stop_event, timer_thread, count_thread, totaltime, timing, wrongwords, elapsedtimeinminutes, textarea

                stop_event = threading.Event()
                totaltime = 60
                timing = 0
                wrongwords = 0
                elapsedtimeinminutes = 0
                timer_thread = None
                count_thread = None

                def start_timer(stop_flag):
                    global timing, totaltime, textarea  # Add textarea to the global scope
                    startButton.config(state=DISABLED)
                    historybtn.config(state=DISABLED)
                    textarea.config(state=NORMAL)
                    textarea.focus()

                    timing += 1
                    elapsed_timer_label.config(text=timing)
                    remaining_timer_label.config(text=totaltime - timing)

                    if timing < totaltime:
                        paradef.after(1000, start_timer, stop_flag)
                    else:
                        textarea.config(state=DISABLED)
                        resetButton.config(state=NORMAL)
                        historybtn.config(state=NORMAL)


                def count(stop_flag):  # Remove the textarea parameter
                    while stop_flag[0]:
                        global wrongwords, timing, totaltime, elapsedtimeinminutes, textarea  # Add textarea to the global scope
                        while timing != totaltime:
                            try:
                                entered_paragraph = textarea.get(1.0, END).split()
                            except Exception as Er_para:
                                print(Er_para)
                            totalwords = len(entered_paragraph)

                        totalwords_count_label.config(text=totalwords)
                        para_word_list = label_paragraph["text"].split()

                        for pair in list(zip(para_word_list, entered_paragraph)):
                            if pair[0] != pair[1]:
                                wrongwords += 1

                        wrongwords_count_label.config(text=wrongwords)

                        elapsedtimeinminutes = timing / 60
                        wpm = (totalwords - wrongwords) / elapsedtimeinminutes
                        wpm_count_label.config(text=wpm)
                        gross_wpm = totalwords / elapsedtimeinminutes
                        if gross_wpm != 0:
                            accuracy = wpm / gross_wpm * 100
                        else:
                            accuracy = 0
                        accuracy = round(accuracy)
                        accuracy_percent_label.config(text=str(accuracy) + "%")
                        msg_labrl.configure(text="Your result is ready. Use the reset button to reset.")
                        resetButton.state(["active"])
                        textarea.config(state=DISABLED)
                        
                        db_file = "typing_stats.db"

                        if not os.path.exists(db_file):
                            conn = sqlite3.connect(db_file)
                            conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                            conn.close()

                        try:
                            conn = sqlite3.connect(db_file)

                            # Check if the table already exists
                            cursor = conn.cursor()
                            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='typing_stats'")
                            table_exists = cursor.fetchone()

                            if not table_exists:
                                conn.execute("""CREATE TABLE typing_stats (ACCURACY REAL, WPM REAL, GROSS_WPM REAL, TOTAL_WORDS INTEGER, WRONG_WORDS INTEGER, TIMESTAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

                            accuracy = 0.95  # Example values for accuracy, wpm, gross_wpm, totalwords, and wrongwords
                            wpm = 60
                            gross_wpm = 65
                            totalwords = 100
                            wrongwords = 5

                            conn.execute("INSERT INTO typing_stats (ACCURACY, WPM, GROSS_WPM, TOTAL_WORDS, WRONG_WORDS) VALUES (?, ?, ?, ?, ?)",
                                        (accuracy, wpm, gross_wpm, totalwords, wrongwords))

                            # Commit changes and close the connection
                            conn.commit()
                            conn.close()
                            print("     >>  Data Written.")
                        except sqlite3.Error as e:
                            print("     >>  An error occurred:", e)
                        
                        break  

                def start():
                    msg_labrl.configure(text="")
                    stop_flag = [True]  # Create a stop flag
                    
                    start_threads(stop_flag, textarea)  # Pass the textarea variable to start_threads


                def start_threads(stop_flag, textarea):  # Add textarea as a parameter
                    try:
                        global timer_thread, count_thread
                        timer_thread = threading.Thread(target=start_timer, args=(stop_flag,))
                        count_thread = threading.Thread(target=count, args=(stop_flag,))
                        timer_thread.start()
                        count_thread.start()
                    except Exception as e:
                        print("An error occurred:", e)


                def stop_threads(stop_flag):
                    try:
                        stop_flag[0] = False
                        stop_event.set()
                        destroy_images(para_main_img, para_footer_img, para_back_img, para_history_img, para_result_img, para_mid_img,
                                    para_graph_main_img, result_frame_img, textarea_img)
                        paradef.destroy()
                        print(" -->> \033[35mPARAGRAPH PAGE: \033[36mReturned To Home Successfully")
                        home_page()
                    except Exception as e:
                        print("An error occurred:", e)


                def reset():
                    global timing, elapsedtimeinminutes, wrongwords
                    timing = elapsedtimeinminutes = wrongwords = 0
                    startButton.config(state=NORMAL)
                    resetButton.config(state=DISABLED)
                    textarea.config(state=NORMAL)
                    textarea.delete(1.0, END)
                    textarea.config(state=DISABLED)
                    historybtn.config(state=NORMAL)
                    msg_labrl.configure(text="Click start and type the above text here:")
                    elapsed_timer_label.config(text="0")
                    remaining_timer_label.config(text="0")
                    wpm_count_label.config(text="...", fg="#282828")
                    accuracy_percent_label.config(text="...", fg="#282828")
                    totalwords_count_label.config(text="...", fg="#282828")
                    wrongwords_count_label.config(text="...", fg="#282828")
                
                
                paragraph_list = [
                    "In recent years, technology has rapidly advanced, changing the way we live our lives. With the rise of smartphones, social media, and streaming services, we have access to more information and entertainment than ever before.",
                    "However, with these advancements come new challenges. Many people struggle with addiction to technology, spending hours on their phones or computers each day. This can lead to a lack of real-life social connections and a decrease in mental well-being.",
                    "In addition to the effects on individuals, technology also has a significant impact on society as a whole. Social media can be a powerful tool for spreading information and organizing movements, but it can also be used to spread misinformation and hate speech.",
                    "Exercise is essential for maintaining physical and mental well-being. Regular exercise can improve cardiovascular health, boost immunity, and increase endorphins, which can reduce stress and improve mood. Exercise also helps to prevent chronic diseases such as diabetes, heart disease, and obesity. It is important to incorporate physical activity into daily life, even if its just a short walk or bike ride.",
                    "Meditation is a practice that has been around for centuries and has numerous health benefits. Regular meditation can reduce stress and anxiety, increase focus and concentration, and improve sleep. It can also help to lower blood pressure and reduce symptoms of depression. Meditation can be practiced in various ways, including mindfulness, breathwork, and visualization",
                    "Social media has become a ubiquitous part of modern life, and its impact is complex. While it can connect people and promote social causes, it can also contribute to anxiety, depression, and cyberbullying. Social media can also be a platform for misinformation and can lead to addictive behavior. Its important to use social media mindfully and with awareness of its potential impact on mental health.",
                    "Getting adequate sleep is crucial for physical and mental health. Sleep deprivation can lead to decreased cognitive function, memory impairment, and an increased risk of accidents. Sleep also plays a vital role in immune function, cardiovascular health, and hormone regulation. Its important to prioritize sleep hygiene, including setting a regular sleep schedule, avoiding screens before bed, and creating a relaxing sleep environment.",
                    "The Power of Gratitude: Gratitude is a simple yet powerful practice that can promote well-being and increase happiness. Research shows that practicing gratitude can reduce stress, improve relationships, and increase feelings of satisfaction with life. Gratitude can be practiced in various ways, including journaling, expressing thanks to others, and cultivating a sense of appreciation for the present moment.",
                    "Proper nutrition is essential for maintaining overall health and well-being. Eating a balanced diet rich in fruits, vegetables, whole grains, and lean protein can reduce the risk of chronic diseases such as heart disease and diabetes. Its important to limit processed foods, sugary drinks, and excess saturated and trans fats. Proper hydration is also critical for maintaining health and preventing dehydration.",
                    "Mental health is just as important as physical health, and its essential to prioritize self-care and seek help when needed. Mental health issues such as depression, anxiety, and stress can affect daily life and overall well-being. Its important to practice self-care activities such as exercise, meditation, and social connection, and to seek professional help when needed.",
                    "Climate change is a pressing issue with significant social, environmental, and economic consequences. It can lead to extreme weather events, rising sea levels, and loss of biodiversity. Climate change can also contribute to food and water scarcity and increased public health risks. Its essential to take action to reduce greenhouse gas emissions, increase renewable energy sources, and advocate for policies that prioritize sustainability and climate justice.",
                    "Education is a fundamental human right that can transform lives and communities. Access to quality education can lead to improved health outcomes, increased economic opportunities, and greater civic engagement. Education can also promote critical thinking and social awareness, which can lead to positive social change. Its important to advocate for equitable access to education and to prioritize educational opportunities for marginalized communities.",
                    "The Impact of Technology: Technology has transformed nearly every aspect of modern life, from communication to work to entertainment. While technology can provide numerous benefits, it",
                    "Another issue facing our society today is climate change. As the planet continues to warm, we are seeing more extreme weather events, rising sea levels, and loss of biodiversity. Its crucial that we take action now to reduce our carbon footprint and transition to sustainable energy sources.",
                    "One way to combat climate change is through renewable energy, such as wind and solar power. While these technologies have come a long way in recent years, there are still challenges to overcome, such as storage and distribution.",
                    "Education is also a key factor in creating a more sustainable future. By teaching children about the environment and the impact of human actions, we can inspire the next generation to make positive changes.",
                    'Have you ever heard of the concept of "dad jokes"? Well, I recently decided to try my hand at it and told my wife a joke. I said, "Why did the tomato turn red? Because it saw the salad dressing!" I was expecting her to roll her eyes or at least give me a pity laugh, but instead, she just looked at me confused and said, "I dont get it." I was shocked. I mean, its a classic dad joke! How could she not get it? So, I explained it to her, and after a long pause, she finally let out a little chuckle. I dont know if my dad joke skills are really that bad, or if my wife just has no sense of humor, but either way, I will keep trying. Who knows, maybe one day I will actually get a real laugh out of her!',
                    'The hacker deftly typed commands into the virtual console, navigating through layers of firewalls and encryption. The systems defenses were sophisticated, but the hacker was equally skilled. As the virtual environment responded to his commands, he could feel himself getting closer to his objective. Finally, he broke through the final layer of protection and gained access to the systems core. But just as he was about to extract the data he needed, a warning message appeared on the screen: "Intrusion detected. Initiating self-destruct. Panic set in as the hacker tried to stop the countdown, but it was too late. The screen went blank as the virtual environment disintegrated around him.',
                ]
                random.shuffle(paragraph_list)
                
                backbtn = Button(para_footer)
                backbtn.configure(image=para_back_img, background="#eeeae7", activebackground="#eeeae7", command=lambda: stop_threads(stop_flag), border=0)
                backbtn.place(x=98, y=80)
                
                para_graph_main = Frame(para_mid, width=900, height=300, background="#eef8da")
                para_graph_main.place(x=40,y=20)
                w01 = Label(para_graph_main, image=para_graph_main_img, border=0, background="#eef8da")
                w01.pack()
                
                report_frame = Frame(para_graph_main, width=280, height=260, background="#eef8da")
                report_frame.place(x=600,y=20)
                f0 = Label(report_frame, image=result_frame_img, border=0, background="#fff")
                f0.pack()

                para_up_header = Label(report_frame,text="Report",font=("Tahoma", 26, "bold"),fg="#007bff", bg="#eef8da")
                para_up_header.place(x=18, y=20)

                elapsed_time_label = Label(report_frame,text="Elapsed Time:",font=("Tahoma", 14, "bold"),fg="#000",border=0, bg="#eef8da")
                elapsed_time_label.place(x=20, y=100)
                elapsed_timer_label = Label(report_frame, text="0", font=("Tahoma", 18), fg="lightblue", border=0, bg="#eef8da")
                elapsed_timer_label.place(x=200, y=100)

                remaining_time_label = Label(report_frame,text="Remaining Time:",font=("Tahoma", 14, "bold"),fg="#000",border=0, bg="#eef8da")
                remaining_time_label.place(x=20, y=160)
                remaining_timer_label = Label(report_frame, text="60", font=("Tahoma", 18), fg="lightgreen", border=0, bg="#eef8da")
                remaining_timer_label.place(x=200, y=160)
                
                para_graph = Frame(para_graph_main, width=580, height=220, background="#eef8da")
                para_graph.place(x=20,y=20)
                
                
                label_paragraph = Label(para_graph,text=paragraph_list[0],wraplength=580,justify=LEFT,font=("arial", 14, "bold"),bd=0,bg="#fff",)
                label_paragraph.pack()
                
                para_entry = Frame(para_mid, width=900, height=280, background="#eef8da")
                para_entry.place(x=40,y=350)
                w02 = Label(para_entry, image=para_graph_main_img, border=0, background="#eef8da")
                w02.pack()
                
                textarea_frame = Frame(para_entry, bg="#FFF", width=565, height=230)
                textarea_frame.place(x=20, y=50)
                te = Label(textarea_frame, image=textarea_img, border=0, background="#FFF")
                te.pack()

                msg_labrl = Label(para_entry)
                msg_labrl.configure(text="Click start and type the above text here:",relief="flat",background="#FFF",foreground="green",border=0,)
                msg_labrl.place(x=20, y=20)

                textarea = Text(textarea_frame,font=("arial", 14, "bold"),width=49,height=9,bd=4,relief=FLAT,wrap="word",bg="#EEE",state=DISABLED) 
                textarea.place(x=9,y=10)
                
                start_frame = Frame(para_entry, width=280, height=260, background="#eef8da")
                start_frame.place(x=600,y=20)
                f0a = Label(start_frame, image=result_frame_img, border=0, background="#fff")
                f0a.pack()
                
                custom_font = font.Font(family='Segoe UI', size=22) 
                style = ttk.Style()
                style.configure('Custom.TButton', font=custom_font)
                startButton = ttk.Button(start_frame, text="Start",style=('Custom.TButton'),command=start, width=10)
                startButton.state(["active"])
                startButton.place(x=60, y=65)

                resetButton = ttk.Button(start_frame, text="Reset",style=('Custom.TButton'),width=10, state=DISABLED, command=reset)
                resetButton.place(x=60, y=145)
                
                paradef.bind("<Destroy>", lambda event: stop_threads(stop_flag))
                textarea.focus_set()
                paradef.mainloop()

            def home_page():
                
                def load_images(image_files):
                    images = {}
                    try:
                        for file in image_files:
                            with Image.open(file) as img:
                                images[file] = ImageTk.PhotoImage(img)
                    except Exception as e:
                        print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                        return None
                    return images
                        
                def open_word_page():
                    nonlocal images
                    try:
                        for image in images.values():
                            if image:
                                count = len(images)
                                print(" -->> \033[30mNumber of images:", count)
                                image.__del__()
                            else:
                                del image
                        images = {}
                        print(" -->> \033[32mCache Successfully Cleared: \033[33mHOME-TO-WORD PAGE")
                        default.destroy()
                        word_page()
                    
                    except Exception as e:
                        print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                        
                def open_para_page():
                    nonlocal images
                    try:
                        for image in images.values():
                            if image:
                                count = len(images)
                                print(" -->> \033[30mNumber of images:", count)
                                image.__del__()
                            else:
                                del image
                        images = {}
                        print(" -->> \033[32mCache Successfully Cleared: \033[33mHOME-TO-PARAGRAPH PAGE")
                        default.destroy()
                        para_page()
                    except Exception as e:
                        print(" -->> \033[37mCache: \033[31mError Occurred:", str(e))
                                
                print("\033[37m -->> Home Page\033[0m")
                   
                default = Frame(hdroot, bg=bgcolor, width=1800, height=900)
                default.pack()

                image_files = ["cross.png", "hd_home_bg.png", "text.png", "hd_home_footer.png", "hd_side_home_bg.png", "mid_up.png",
                            "button_word.png", "button_paragraph.png", "button_skill-improver.png", "web.png", "about.png",
                            "update.png"]
                images = load_images(image_files)

                home_fr = Frame(default, width=800, height=820, bg=bgcolor)
                home_fr.place(x=40, y=40)

                la = Label(home_fr, image=images["hd_home_bg.png"], border=0, background=bgcolor)
                la.pack()

                header = Label(home_fr, image=images["button_skill-improver.png"], background="#66a0f8", border=0)
                header.place(x=40, y=80)

                chos = Label(home_fr, text="SKILL IMPROVER", border=0, background="#fff", fg="#000")
                chos.configure(font=("Calibri (Body)", 34, "bold"))
                chos.place(x=215, y=105)

                home_mid = Frame(home_fr, width=720, height=560)
                home_mid.place(x=40, y=220)
                label = Label(home_mid, image=images["text.png"], border=0, background="#66a0f8")
                label.pack()

                home_up = Frame(default, width=865, height=540, bg=bgcolor)
                home_up.place(x=885, y=40)

                lb = Label(home_up, image=images["hd_side_home_bg.png"], border=0, background=bgcolor)
                lb.pack()

                exit_btn = Button(home_up, image=images["cross.png"], background="#FFF", activebackground="#FFF", command=on_exit, border=0)
                exit_btn.place(x=784, y=14)

                home_up_mid = Frame(home_up, width=700, height=400, bg="#EEE")
                home_up_mid.place(x=80, y=100)

                ld = Label(home_up_mid, image=images["mid_up.png"], border=0, background="#FFF")
                ld.pack()

                chos = Label(home_up_mid, text="Challenges", border=0, background="#eeeae7", fg="#000")
                chos.configure(font=("Calibri (Body)", 36, "bold"))
                chos.place(x=60, y=50)

                choss = Label(home_up_mid, text="Choose a Challenge Type", border=0, background="#eeeae7", fg="#282C34")
                choss.configure(font=("Calibri (Body)", 22, "bold"))
                choss.place(x=60, y=130)

                wordbtn = Button(home_up_mid, image=images["button_word.png"], background="#eee", activebackground="#eee", command=open_word_page, border=0)
                wordbtn.place(x=60, y=280)

                parabtn = Button(home_up_mid, image=images["button_paragraph.png"], background="#eee", activebackground="#eee", command=open_para_page, border=0)
                parabtn.place(x=380, y=280)

                home_footer = Frame(default, width=865, height=240, bg=bgcolor)
                home_footer.place(x=885, y=620)

                lc = Label(home_footer, image=images["hd_home_footer.png"], border=0, background=bgcolor)
                lc.pack()

                Webbtn = Button(home_footer, image=images["web.png"], background="#FFF", activebackground="#FFF", command=open_webiste, border=0)
                Webbtn.place(x=100, y=100)

                Aboutbtn = Button(home_footer, image=images["about.png"], background="#FFF", activebackground="#FFF", command=about_app, border=0)
                Aboutbtn.place(x=400, y=100)

                updatebtn = Button(home_footer, image=images["update.png"], background="#FFF", activebackground="#FFF", command=app_updator, border=0)
                updatebtn.place(x=700, y=100)

                hdroot.bind("<B1-Motion>", move_app)
                hdroot.protocol("WM_DELETE_WINDOW", on_exit)
                hdroot.mainloop()
            
            home_page()
        
        def splash_func():
            try:
                gif = Image.open("skill_gif.gif")
            except FileNotFoundError:
                messagebox.showerror("File Missing", "The file skill_gif.gif was not found.")
                splash.destroy()
                return
                    
            def animate(frame):
                if gif_label.winfo_exists():
                    gif_label.config(image=frames[frame])
                    splash.after(50, animate, (frame + 1) % len(frames))
                if frame == len(frames) - 1:
                    gifframe.destroy()
                    x = (screen_width - 250) // 2
                    y = (screen_height - 180) // 2
                    splash.geometry(f"+{x}+{y}")
                    close = Label(splash, text="", bg="#FFF", font=("Leelawadee UI", 20), bd=160)
                    print("\033[35m -->> Greeting Screen\033[0m")
                    if current_hour < 12:
                        close.config(text="Welcome, Good morning", fg="#1E90FF", font=("Leelawadee UI", 22, "bold"))
                    elif 12 <= current_hour < 18:
                        close.config(text="Welcome, Good afternoon", fg="#000", font=("Leelawadee UI", 22, "bold"))
                    else:
                        close.config(text="Welcome, Good Evening", fg="#FFF", bg="#000", font=("Leelawadee UI", 22, "bold"))
                    close.pack()
                            
                    def close_splash():
                        gif = None
                        if gif:
                            gif.__del__()
                        else:
                            del gif
                        splash.destroy()
                        contion_first()
                    close.after(3800, close_splash)

            def show_splash():
                print("\033[33m -->> Splash Screen\033[0m")
                # Create a list of PhotoImage objects to store the frames of the GIF
                global frames, gif_label, gifframe
                frames = []
                for frame in range(gif.n_frames):
                    gif.seek(frame)
                    resized_image = gif.resize((600, 600))
                    frames.append(ImageTk.PhotoImage(resized_image))
                # Create a frame and a label to display the GIF
                gifframe = Frame(splash)
                gifframe.pack()
                gif_label = Label(gifframe, image=frames[0], bg="#ccc")
                gif_label.pack()
                # Start the animation
                animate(0)
                
            x = (screen_width - 250) // 2
            y = (screen_height - 600) // 2
            splash.geometry(f"+{x}+{y}")
            current_hour = int(datetime.now().strftime("%H"))
            
            show_splash()
            # Start the main event loop
            print("\033[36m Condition: \033[33m01\033[0m") 
            splash.mainloop()
        
        splash_func()
        
    elif screen_width >= 1360:
        print("1360")
        splash_funcsec()  
        
    elif screen_width >= 1280:
        if screen_height == 960:
            print("1280*960")
            splash_funcsec()  
        elif screen_height == 800:
            print("1280*800")
            splash_funcsec()  
        elif screen_height == 768:
            print("1280*768")
            splash_funcsec()  
        elif screen_height == 720:
            print("1280*720")
            splash_funcsec()  
    else:
        splash.withdraw()
        messagebox.showerror("Display Error", "Unsupported display resolution for application")
        splash.destroy()   

check_screen()