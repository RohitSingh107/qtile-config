import os
import socket
from libqtile import bar, widget, qtile
from defaults import myTerm


colorschemes = {
    "default": [["#ff5555", "#ff5555"],  # 0
                ["#ffffff", "#ffffff"],  # 1
                ["#ffd47e", "#ffd47e"],  # 2
                ["#62FF00", "#62FF00"],  # 3
                ["#c40234", "#c40234"],  # 4
                ["#6790eb", "#6790eb"],  # 5
                ["#282c34", "#282c34"],  # 6
                ["#212121", "#212121"],  # 7
                ["#e75480", "#e75480"],  # 8
                ["#2aa899", "#2aa899"],  # 9
                ["#abb2bf", "#abb2bf"],  # 10
                ["#56b6c2", "#56b6c2"],  # 11
                ["#b48ead", "#b48ead"],  # 12
                ["#ff79c6", "#ff79c6"],  # 13
                ["#e06c75", "#e06c75"],  # 14
                ["#ffb86c", "#ffb86c"]]  # 15
}

def init_colors(colorscheme="default"):
    return colorschemes[colorscheme]


colors = init_colors()


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

        widget.Sep(
            linewidth=1,
            padding=10,
            foreground=colors[8],
            background=colors[8]
        ),              #
        widget.Image(
            filename="~/.config/qtile/icons/garuda-red.png",
            iconsize=9,
            background=colors[8],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('jgmenu_run')}
        ),
        widget.GroupBox(

            foreground=colors[7],
            background=colors[8],

            font='UbuntuMono Nerd Font',

            fontsize=15,
            margin_y=3,
            margin_x=2,
            padding_y=5,
            padding_x=4,
            borderwidth=3,

            active=colors[1],
            inactive=colors[2],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors[9],
            this_current_screen_border=colors[12],
            this_screen_border=colors[10],
            other_current_screen_border=colors[6],
            other_screen_border=colors[10],
            disable_drag=True



        ),
        widget.TaskList(
            highlight_method='border',  # or block
            icon_size=20,
            max_title_width=150,
            rounded=True,
            padding_x=0,
            padding_y=0,
            margin_y=0,
            fontsize=17,
            border=colors[3],
            foreground=colors[4],
            margin=2,
            txt_floating='🗗',
            txt_minimized='>_ ',
            borderwidth=1,
            background=colors[12],
            #unfocused_border = 'border'
        ),

        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[1],
            background=colors[0],
            padding=0,
            scale=0.7
        ),

        widget.CurrentLayout(
            font="Noto Sans Bold",
            fontsize=16,
            foreground=colors[1],
            background=colors[0]
        ),


        widget.Net(
            font="Noto Sans",
            fontsize=16,
            # Here enter your network name
            interface=["wlp6s0"],
            format='{down} ↓↑ {up}',
            foreground=colors[1],
            background=colors[11],
            padding=0,
        ),

        widget.CPU(
            font="Noto Sans",
            #format = '{MemUsed}M/{MemTotal}M',
            update_interval=1,
            fontsize=16,
            foreground=colors[1],
            background=colors[13],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        ),

        widget.Memory(
            font="Noto Sans",
            format='{MemUsed: .0f}M/{MemTotal: .0f}M',
            update_interval=1,
            fontsize=16,
            measure_mem='M',
            foreground=colors[1],
            background=colors[9],
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        ),

        widget.Clock(
            foreground=colors[4],
            background=colors[15],
            fontsize=16,
            format="%Y-%m-%d %H:%M"
        ),

        widget.Systray(
            background=colors[5],
            icon_size=20,
            padding=4
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


main_bar = bar.Bar(widgets=init_widgets_screen1(), size=25,
                   opacity=0.85, background="000000")

main_bar2 = bar.Bar(widgets=init_widgets_screen2(), size=25,
                    opacity=0.85, background="000000")
