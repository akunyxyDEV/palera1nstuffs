import time;import paramiko;import customtkinter as tk;from paramiko import SSHClient;from customtkinter import *;
from tk import *
client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

tk.set_appearance_mode('dark')
tk.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry("300x450")
root.title("KDAP")
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)
frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60,side=LEFT,fill="both", expand=True)
warning = CTkLabel(master=frame,text="Palera1n Debugger")
warning.pack(padx=10,pady=10)
ip = tk.CTkEntry(master=frame,placeholder_text="IP Here")
ip.pack(pady=10,padx=10)
def connect():
    client.connect(ip.get(),22,"root","alpine")
def run(x):
    stdin, stdout, stderr = client.exec_command(x, get_pty=True)
    for line in iter(stdout.readline, ""):
        print(line, end="")
def installwget():
    answer = 'Y'
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("apt install wget")
    ssh_stdin.write(answer + '\n')
    ssh_stdin.flush()
    ssh_stdin.write("y" + '\n')
    ssh_stdin.flush()
    time.sleep(1)
    ssh_stdout.read()
def straprepo():
    run(x="wget 'https://static.palera.in/straprepo.deb'")
    run(x="dpkg -i straprepo.deb")
def clean():
    run("rm straprepo.deb")
    run("rm cydia.deb")
def installcydia():
    run("wget 'https://static.palera.in/cydia.deb'")
    run("dpkg -i cydia.deb")
def uninstallcydia():
    run("dpkg -P cydia")
def uninstallstraprepo():
    run("dpkg -P palecursus")
connecttoip = CTkButton(master=frame,text="Connect",command=connect)
connecttoip.pack(pady=5,padx=10)
wget = CTkButton(master=frame,text="Install WGET (needed)",command=installwget)
wget.pack(pady=5,padx=10)
strap = CTkButton(master=frame,text="Install Strap Repo",command=straprepo)
strap.pack(pady=5,padx=10)
cydia = CTkButton(master=frame,text="Install Cydia (BROKEN)",command=installcydia)
cydia.pack(pady=5,padx=10)
cydia = CTkButton(master=frame,text="Uninstall Cydia",command=uninstallcydia)
cydia.pack(pady=5,padx=10)
cydia = CTkButton(master=frame,text="Uninstall StrapRepo",command=uninstallstraprepo)
cydia.pack(pady=5,padx=10)
palera1n = CTkButton(master=frame,text="Download Palera1n IPA",state="disabled")
palera1n.pack(pady=5,padx=10)
cydia = CTkButton(master=frame,text="Clean Files",command=clean)
cydia.pack(pady=5,padx=10)
root.mainloop()