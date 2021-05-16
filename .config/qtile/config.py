# -*- coding: utf-8 -*-
from typing import List  # noqa: F401

# mouse_callbacks
from libqtile import qtile

#----- Built-in Extensions: WindowList
from libqtile.extension import WindowList

import os, subprocess
from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import (
    CurrentLayoutIcon,
    Sep,
    GroupBox,
    TextBox,
    Prompt,
    WindowName,
    Systray,
    Net,
    Volume,
    Clock,
    KeyboardLayout,
    WindowCount,
#    CapsNumLockIndicator,
#    Chord,
    QuickExit,
    )

mod = "mod4"
terminal = guess_terminal()

groups = [
    Group("WEB", layout='monadtall', matches=[Match(wm_class=["chromium"])]),
    Group("RED", layout='monadwide',),
    Group("DEV", layout='matrix', matches=[Match(wm_class=["nemo"])]),
    Group("ZOO", layout='zoomy',),
    Group("MAX", layout='max', matches=[Match(wm_class=["etl"])]),
]

#----- Play around Groups
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

#----- Key Bindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="move active window >> left",),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="move active window >> right",),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="move active window >> down",),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="move active window >> up",),
    
    # Change window size/ratio
    Key([mod], "i", lazy.layout.grow(),
        desc="expand window size/ratio",),
    Key([mod], "m", lazy.layout.shrink(),
        desc="shrink/decrease window size/ratio",),
    Key([mod], "n", lazy.layout.normalize(),
        desc="normalize stack size/ratio",),
    Key([mod], "o", lazy.layout.maximize(),
        desc="maximize active window size/ratio : stack",),
    Key([mod], "c", lazy.layout.reset(),
        desc="reset all windows",),
    Key([mod, "shift"], "space", lazy.layout.flip(),
        desc="flip stack layout",),

    # Float active window or reset to the correct order
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle Floating"),

    # Applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "p", lazy.spawn("dmenu_run -i"), desc="dmenu"),
    Key([mod, "shift"], "w", lazy.spawn("chromium"),
        desc="Launch Chromium Browser"),

    Key([mod, "shift"], "Return", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # List open windows in dmenu 
    Key([mod], "u", lazy.run_extension(WindowList(
        item_format="{id}: {window} >>> {group}",)),
        desc="Give vertical list of all open windows in dmenu. Switch to selected",
        ),
]

#----- GLOBAL COLORZ, Yep ColorZ!
colorz = ("#000000", #[0] Dark Panel BG
          "#2ABB9B", #[1] Green : Border Line >> Active Tab >> Group
          "#FFa400", #[2] Yellow: Inactive Group Names
          "#F22613", #[3] Red   : Active Group Names
          "#19B5FE", #[4] Blue  : Selected Group
          "#ff0000", #[5] light Red : Focused Window Border
          "#5aff00", #[6] Green : Normal Window Border
          )

layout_monad = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 2,
    "margin": 2,
    "single_border_width": 2,
    "single_margin": 2,
    }

layout_flo = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 2,
    "fullscreen_border_width": 2,
    }

layout_zoomy = {
    "columnwidth": 200,
    "margin": 2,
    }

layout_matrix = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 2,
    "margin": 2,
    }

layouts = [
    layout.MonadTall(**layout_monad,ratio=0.6),
    layout.MonadWide(**layout_monad),
    layout.Matrix(**layout_matrix),
    layout.Zoomy(**layout_zoomy),
    layout.Max(),
    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

#----- Widget Settings
widget_defaults = dict(
    font='San Francisco Display',
    fontsize=14,
    padding=3,
    background=colorz[0], #Panel Background
    )

#----- Random Global Variables
#----- Custom Icon Path for CurrentlayoutIcon Widget
wd_icon = [os.path.expanduser("~/.config/qtile/icons")]

# Default File Manager
def open_fm():
    qtile.cmd_spawn('nemo')

w_sep = {
    "background": colorz[0],
    "foreground": colorz[2],
    "linewidth":8,
    "size_percent":60,
    }

w_gbox = {
    "active": colorz[3],
    "block_highlight_text_color": colorz[4],
    "borderwidth": 2,
    "inactive": colorz[2],
    "this_current_screen_border": colorz[1],
    "this_screen_border": colorz[2],
    }

w_prompt = {
    "cursor_color": colorz[3],
    "padding": 5,
    "prompt": "Start:   ",
    }

w_net = {
    "format": "{down} ↓↑ {up}",
    "interface": "wlx7cdd90399231",
    }

w_vol = {
    "fmt": "🎧 {}",
    }

w_clock = {
    "format": "%d-%m-%Y %a %I:%M %p",
}

w_key_l = {
    "configured_keyboards": ['us','de','iq ku_ara', 'ar'],
    "display_map": {"us":"EN",
                    "iq ku_ara":"KU",
                    "de":"DE",
                    "ar":"AR"},
}

screens = [
    Screen(
        top=bar.Bar(
            [
                CurrentLayoutIcon(custom_icon_paths=wd_icon),
                Sep(**w_sep),
                GroupBox(**w_gbox,),
                TextBox(text="🐸", fontsize="16", padding=5,),
                WindowCount(),
                Prompt(**w_prompt),
                WindowName(foreground=colorz[1]),
                TextBox(text="📂", fontsize="16", padding=5, mouse_callbacks={'Button1': open_fm},),
                Systray(icon_size=20),
                TextBox(text="[", foreground=colorz[2], fontsize=18,),
                Net(**w_net,),
                TextBox(text="]", foreground=colorz[2], fontsize=18,),
                TextBox(text= "[", foreground= colorz[4], fontsize= 18,),
                Volume(**w_vol),
                TextBox(text= "]", foreground= colorz[4], fontsize= 18,),
                TextBox(text= "[", foreground= colorz[3], fontsize= 18,),
                Clock(**w_clock),
                TextBox(text= "]", foreground= colorz[3], fontsize= 18,),
                TextBox(text= "[", foreground= colorz[1], fontsize= 18,),
                KeyboardLayout(**w_key_l),
                TextBox(text= "]", foreground= colorz[1], fontsize= 18,),

            ],
            24,
            opacity=0.90,
        ),
    ),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None #HSK
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(**layout_flo, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
