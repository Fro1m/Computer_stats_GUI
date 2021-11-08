import tkinter as tk
import socket
import uuid
import requests
import urllib.request
import pycountry
from subprocess import check_output
import win32gui
import win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

dg = check_output((
    "powershell -NoLogo -NoProfile -NonInteractive -ExecutionPolicy bypass -Command ""& {"
    "Get-NetRoute –DestinationPrefix '0.0.0.0/0' | Select-Object -First 1 | "
    "Get-NetIPConfiguration "
    "}"""
)).decode().strip()
with open('readme.txt', 'w') as f:
    f.write(dg)
f = open('readme.txt')
lines = f.readlines()
dg_line = (lines[12])
def1 = []
for i in range(23, 33):
    def1.append(dg_line[i])
final_default_gateway = ''.join(def1)


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


def get(ip):
    endpoint = f'https://ipinfo.io/{ip}/json'
    response = requests.get(endpoint, verify=True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['country']


def show_mac(text):
    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, text)
    mac_entry.delete(0, 2)
    return


def exit_code():
    window.destroy()


def show_ip(text):
    ip_entry.delete(0, tk.END)
    ip_entry.insert(0, text)
    return


def show_country(text):
    result.delete(0, tk.END)
    result.insert(0, text)
    return


def do_you(text):
    result.delete(0, tk.END)
    result.insert(0, text)
    return


def show_default_gateway(text):
    result.delete(0, tk.END)
    result.insert(0, text)


def show_comp_name(text):
    result.delete(0, tk.END)
    result.insert(0, text)


external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
my_country = get(external_ip)
c = pycountry.countries.get(alpha_2=my_country)


window = tk.Tk()
window.geometry('310x270')
window.resizable(width=False, height=False)

top_left_frame = tk.Frame(master=window,
                          relief=tk.SUNKEN,
                          borderwidth=2,
                          bg="white",
                          )

top_right_frame = tk.Frame(master=window,
                           relief=tk.SUNKEN,
                           borderwidth=2,
                           bg="white",
                           )

bottom_frame = tk.Frame(master=window,
                        relief=tk.SUNKEN,
                        borderwidth=2,
                        bg="white",
                        )

ip_button = tk.Button(master=top_left_frame,
                      text="Check your IP",
                      command=lambda:show_ip(ip_address)
                      )

mac_button = tk.Button(master=top_right_frame,
                       text="Check your MAC",
                       command=lambda:show_mac(hex(uuid.getnode()))
                       )

copyright_label = tk.Label(text="© This program belongs to Fro1m")

ip_entry = tk.Entry(master=top_left_frame,)
mac_entry = tk.Entry(master=top_right_frame)
check_label = tk.Label(master=bottom_frame,
                       text="You can also check your:\n",
                       bg="white",
                       fg="black",)
but = tk.IntVar()

check_c_name = tk.Radiobutton(master=bottom_frame,
                              text="Computer name",
                              variable=but,
                              value=1,
                              command=lambda: show_comp_name(hostname)
                              )
check_dg = tk.Radiobutton(master=bottom_frame,
                          text="default gateway",
                          variable=but,
                          value=2,
                          command=lambda: show_default_gateway(final_default_gateway)
                          )
check_country = tk.Radiobutton(master=bottom_frame,
                               text="current country",
                               variable=but,
                               value=3,
                               command=lambda: show_country(c.name)
                               )
check_lucky = tk.Radiobutton(master=bottom_frame,
                             text="Are you lucky?",
                             variable=but,
                             value=4,
                             command=lambda: do_you("Are you?")
                             )

result = tk.Entry(master=bottom_frame)

exit_button = tk.Button(text="Click to exit",
                        command=exit_code)

top_left_frame.place(x=10, y=5)
top_right_frame.place(x=160, y=5)
bottom_frame.place(x=16, y=90)
ip_button.pack(padx=5, pady=5)
mac_button.pack(padx=5, pady=5)
ip_entry.pack(padx=5, pady=5)
mac_entry.pack(padx=5, pady=5)
check_label.grid(row=0, column=1)
check_c_name.grid(row=1, column=1)
check_dg.grid(row=2, column=1)
check_country.grid(row=3, column=1)
check_lucky.grid(row=4, column=1)
result.grid(row=2, column=2, padx=5)
copyright_label.place(x=3, y=238)
exit_button.place(x=220, y=238)


window.mainloop()