
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, ScratchPad, DropDown
from defaults import myTerm, myFM

scratchpad = ScratchPad(
    'scratchpad', [
        DropDown('term', myTerm, width=0.8,
                         height=0.7, x=0.1, y=0.1, opacity=1, on_focus_lost_hide = False),
        DropDown('fm', myFM, width=0.4,
                 height=0.5, x=0.3, y=0.1, opacity=0.5),

    ]
)


