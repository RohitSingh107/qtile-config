import os
import socket
from libqtile import bar, widget, qtile



myTerm = "alacritty" # My terminal of choice
def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#ff5555", "#ff5555"], # color 3
            ["#f4c2c2", "#f4c2c2"], # color 4
            ["#ffffff", "#ffffff"], # color 5
            ["#ffd47e", "#ffd47e"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#000000", "#000000"], # color 8
            ["#c40234", "#c40234"], # color 9
            ["#6790eb", "#6790eb"], # color 10
            ["#ff00ff", "#ff00ff"], #11
            ["#4c566a", "#4c566a"], #12 
            ["#282c34", "#282c34"], #13
            ["#212121", "#212121"], #14
            ["#e75480", "#e75480"], #15 
            ["#2aa899", "#2aa899"], #16 
            ["#abb2bf", "#abb2bf"],# color 17
            ["#81a1c1", "#81a1c1"], #18 
            ["#56b6c2", "#56b6c2"], #19 
            ["#b48ead", "#b48ead"], #20 
            ["#e06c75", "#e06c75"], #21
            ["#ff79c6", "#ff79c6"], #22
            ["#ffb86c", "#ffb86c"]] #23

colors = init_colors()
def base(fg='text', bg='dark'):
    return {'foreground': colors[14],'background': colors[15]}




def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                 widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[15],
                        background = colors[15]
                        ),              #
               widget.Image(
                       filename = "~/.config/qtile/icons/garuda-red.png",
                       iconsize = 9,
                       background = colors[15],
                       mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn('jgmenu_run')}
                       ),
               widget.GroupBox(

            **base(bg=""),
            font='UbuntuMono Nerd Font',

                    fontsize = 15,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,

            active=colors[5],
            inactive=colors[6],
            rounded= True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[16],
            this_current_screen_border=colors[20],
            this_screen_border=colors[17],
            other_current_screen_border=colors[13],
            other_screen_border=colors[17],
            disable_drag=True


                   
                        ),
                widget.TaskList(
                    highlight_method = 'border', # or block
                    icon_size=20,
                    max_title_width=150,
                    rounded=True,
                    padding_x=0,
                    padding_y=0,
                    margin_y=0,
                    fontsize=17,
                    border=colors[7],
                    foreground=colors[9],
                    margin=2,
                    txt_floating='🗗',
                    txt_minimized='>_ ',
                    borderwidth = 1,
                    background=colors[20],
                    #unfocused_border = 'border'
                ),

               widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[5],
                       background = colors[3],
                       padding = 0,
                       scale = 0.7
                       ),

               widget.CurrentLayout(
                      font = "Noto Sans Bold",
                      fontsize = 16,
                      foreground = colors[5],
                      background = colors[3]
                        ),


                widget.Net(
                         font="Noto Sans",
                         fontsize=16,
                        # Here enter your network name
                         interface=["wlp6s0"],
                         format = '{down} ↓↑ {up}',
                         foreground=colors[5],
                         background=colors[19],
                         padding = 0,
                         ),

                widget.CPU(
                        font="Noto Sans",
                        #format = '{MemUsed}M/{MemTotal}M',
                        update_interval = 1,
                        fontsize = 16,
                        foreground = colors[5],
                        background = colors[22],
                        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),

               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
                        update_interval = 1,
                        fontsize = 16,
                        measure_mem = 'M',
                        foreground = colors[5],
                        background = colors[16],
                        mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                       ),

               widget.Clock(
                        foreground = colors[9],
                        background = colors[23],
                        fontsize = 16,
                        format="%Y-%m-%d %H:%M"
                        ),

               widget.Systray(
                       background=colors[10],
                       icon_size=20,
                       padding = 4
                       ),
              ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


main_bar = bar.Bar(widgets=init_widgets_screen1(), size=25, opacity=0.85, background= "000000")

main_bar2 = bar.Bar(widgets=init_widgets_screen2(), size=25, opacity=0.85, background= "000000")
