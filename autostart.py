import subprocess
from defaults import home, wayland, wallpaper



processes = [
    "lxsession",
    "nm-applet",
    "numlockx on",
    "blueman-applet",
    f"picom --config {home}/.config/picom/picom-blur.conf",
    "dunst",
    f"swaybg --image {wallpaper}" if wayland else f"feh --bg-fill {wallpaper}",
    "cbatticon",
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
