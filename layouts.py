
from libqtile import layout

def init_layout_theme():
    return {"margin":8,
            "border_width":2,
            "border_focus": "#ff00ff",
            "border_normal": "#f4c2c2"
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=8, border_width=2, border_focus="#ff00ff", border_normal="#f4c2c2"),
    layout.MonadWide(margin=8, border_width=2, border_focus="#ff00ff", border_normal="#f4c2c2"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color = '#141414',
        active_bg = '#0000ff',
        inactive_bg = '#1e90ff',
        padding_y =5,
        section_top =10,
        panel_width = 280),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme)
]


