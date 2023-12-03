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
splash.iconbitmap("TypeBlitz_Icon.ico")
splash.resizable(False, False)
splash.attributes("-topmost", True)

# Get the screen resolution
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

def check_screen_default():
    print("Checking Screen")

    def scheme_first():

        global wordTK
        wordTK = Tk()
        bgcolor="#6e83b7"
        wordTK.config(bg=bgcolor)
        wordTK.title("TypeBlitz")
        wordTK.overrideredirect(True)
        wordTK.iconbitmap("TypeBlitz_Icon.ico")
        wordTK.resizable(False, False)
        
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        screen_widthhd =  wordTK.winfo_screenwidth()
        screen_heighthd =  wordTK.winfo_screenheight()
        
        if screen_width == 1366:
            wordTK.geometry("1280x700+30+26")
        elif screen_width == 1360:
            wordTK.geometry("1280x700+18+18")
        elif screen_width == 1280 and screen_heighthd == 960:
            wordTK.geometry("1280x700+0+60")
        elif screen_width == 1280 and screen_heighthd == 800:
            wordTK.geometry("1280x700+0+10")
        elif screen_width == 1280 and screen_heighthd >= 700:
            wordTK.geometry("1280x700+0+0")
        else:
            wordTK.geometry("1280x700+0+0")
        
        def move_app_sec(e):
            wordTK.geometry(f"+{e.x_root}+{e.y_root}")
        
        def open_web():
            try:
                print("\033[32m ---->> Redirected to Browser\033[0m")
                webbrowser.open("https://sarwanboi.github.io/Skill-Improver.github.io")
            except webbrowser.Error as web_error:
                messagebox.showerror("Web Browser Error", f"Could not open the web page: {web_error}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
                        
        def about_app():
            about_tk = Toplevel( wordTK)
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
                ("1.0", 200, 80),
                ("Version:", 26, 120),
                ("1.2 (Beta)", 200, 120),  # Indicate that version 3.6 is the production version
                ("Released Date:", 26, 160),
                ("December 04, 2023", 200, 160),
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
        
        def app_updator():
            print("\033[33m ---->> Started Updator\033[0m")
                        
            droot = Tk()
            droot.title("Stay Updated - Skill Improver")
            droot.iconbitmap("TypeBlitz_Icon.ico")
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
                
                local_version = "1.2.0.0"          
                print("\033[36m     >> Current Application Version:\033[33m", local_version)
                
                def is_uptodated():
                    update_btn.configure(text="", state=DISABLED, cursor="arrow", foreground="#eee", background="#eee")
                    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36","Accept-Language": "en-US,en;q=0.9","Referer": "https://www.google.com/"}
                    response = requests.get(version_url, headers=header)
                    latest_version = response.text.strip()

                    if latest_version > local_version:
                        print("\033[36m >> Available Application Version:\033[33m", latest_version)

                        def ask_continue():
                            droot.attributes("-topmost", False)
                            msg_box = messagebox.askquestion("Update?", "Are you want to download the latest version?", icon="info")
                            if msg_box == "yes":
                                exe_url = ""
                                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

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
        
        def word_page():
            default.destroy()
            print("\033[37m -->> Word Page\033[0m")
            wordbg = "#66a0f8"
            worddef = Frame(wordTK, width=1800, height=900, background=wordbg)
            worddef.pack()
                        
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
                    home_page()
                except Exception as e:
                    print(f" -->> \033[31mAn error occurred while returning to the home page: \033[37m{str(e)}")

            image_files = ["homie.png", "histor.png", "wordtext.png", "wordtop.png", "wordfooter.png", "wordmain.png", "wordresult.png","textarea.png"]
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

                def insert_text_and_highlight_matches(result_text, results, search_string):
                    result_text.insert("end", "\n\n".join(results))
                    highlight_matches(result_text, search_string)

                history_tk = ttkthemes.ThemedTk()

                history_tk.get_themes()
                history_tk.set_theme("breeze")
                history_tk.title("Word Challenge- History Panel")
                history_tk.resizable(0, 0)
                history_tk.config(bg="#F2F2F2")
                history_tk.iconbitmap("TypeBlitz_Icon.ico")
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
        
        def home_page():
            def exitway():
                def finalexit():
                    try:
                        print("\033[31m// Exist: TK\033[0m")
                        wordTK.destroy()
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
                        
                rr = messagebox.askyesno("Exit", "Are you sure you want to exit?")
                if rr:
                    wordTK.title("Closing")
                    print("\033[31m// Application Closed!!\033[0m")
                    wordTK.after(2000,finalexit)
                else:
                    pass
                
            print("\033[37m -->> Home Page\033[0m")
            global default
            default = Frame( wordTK,bg=bgcolor, width=1280, height=700)
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
            
            la = Label( wordTK, image=images["TypeBlitz2.png"], border=0, background=bgcolor)
            la.place(x=100, y=100)
            
            option = Frame( wordTK, width=500, height=500)
            option.place(x=700, y=100)
            lb = Label(option, image=images["TypeBlitz_side.png"], border=0, background=bgcolor)
            lb.pack()   
            closebtn = Button(option, image=images["exit.png"], background="#466089", activebackground="#466089", command= exitway, border=0)
            closebtn.place(x=440, y=10)
            
            option_in_a = Frame(option, width=350, height=210, bg="#466089")
            option_in_a.place(x=75, y=65)
            lc = Label(option_in_a, image=images["TypeBlitz_side_in_a.png"], border=0, background="#466089")
            lc.pack()   
            header = Label(option_in_a, text="Type Test", font=("Helvetica", 17, "bold"), bg="#FFF", fg="#000")
            header.place(x=20, y=24) 
            sub_header = Label(option_in_a, text="Select a Type of Test:", font=("Helvetica", 13), bg="#FFF", fg="#75a7e5")
            sub_header.place(x=26, y=70)
            wordbtn = Button(option_in_a, image=images["button_word.png"], background="#FFF", activebackground="#FFF", border=0, command=word_page)
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
            updatebtn = Button(option_in_b, image=images["update.png"], background="#FFF", activebackground="#FFF", border=0, command=app_updator)
            updatebtn.place(x=260, y=35)
            
            default.bind("<B1-Motion>", move_app_sec)
            default.mainloop()
            
            # ***************************************************************************************************************************************************  #
            
        home_page()
        
        wordTK.bind("<B1-Motion>", move_app_sec)
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
        message = f"""\n Your display resolution is {screen_width}x{screen_height}. 
        \n Additionally, the optimal viewing resolution for this application is 1360x768.
        \n The upcoming update will also provide support for {screen_width}x{screen_height}."""
        messagebox.showinfo("Display Error", message)
        splash_screen()
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
