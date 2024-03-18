
import os
from libqtile import qtile

home = os.path.expanduser('~')
wayland = False

if qtile.core.name == "x11":
    myTerm = "kitty"
elif qtile.core.name == "wayland":
    # myTerm = "foot"
    myTerm = "kitty"
    wayland = True

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
# myTerm = "alacritty" # My terminal of choice
myFM = "nautilus"
myBrowser = "firefox-nightly"
colorscheme = "default"

systemMonitor = "missioncenter"

wallpaper = '/usr/share/wallpapers/garuda-wallpapers/Abstract.jpg'


