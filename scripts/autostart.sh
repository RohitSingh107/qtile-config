#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}



#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
blueman-applet &
#flameshot &
#picom --config $HOME/.config/picom/picom.conf &
# picom --config .config/picom/picom-blur.conf &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
# feh --randomize --bg-fill /usr/share/wallpapers/garuda-wallpapers/*
feh --bg-fill /usr/share/wallpapers/garuda-wallpapers/Abstract.jpg
#starting user applications at boot time
run volumeicon &
run cbatticon &

#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
