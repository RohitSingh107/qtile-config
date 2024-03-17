import subprocess
import os


home = os.path.expanduser("~")

processes = [
    "lxsession",
    "nm-applet",
    "numlockx on",
    "blueman-applet",
    f"picom --config {home}/.config/picom/picom-blur.conf",
    "dunst",
    "feh --bg-fill /usr/share/wallpapers/garuda-wallpapers/Abstract.jpg",
    # "cbatticon",
]


def run(process: str):
    com = process.split()
    try:
        subprocess.check_call(["pgrep", com[0]])
    except subprocess.CalledProcessError:
        subprocess.Popen(com)


def run_all_processes():
    for process in processes:
        run(process)
