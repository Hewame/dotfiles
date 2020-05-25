# -*- coding: utf-8 -*-
# Compatable with Qtile version : "0.15.1.dev120+ga07667bf" or later.
# Modified by : Hewa Saleem
#  
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar
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
    )

from typing import List  # noqa: F401

mod = "mod4"


##### Define Groups #####
groups = [
    Group("WEB", layout='monadtall',),
    Group("DEV", layout='monadtall',),
    Group("STK", layout='monadwide',),
    Group("FLO", layout='floating',),
    Group("MAX", layout='max',),  
]

##### Play around Groups #####
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send current window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)


##### GLOBAL COLORS, Yes ColorZ! #####
colorz = ("#00172D", #[0] Maastricht Dark-Blue : Panle BG
          "#2ABB9B", #[1] TURQUOISE Green : Border Line >> Active Tab >> Group
          "#FFA400", #[2] BRIGHT GOLDEN Yellow : Inactive Group Names
          "#F22613", #[3] POMEGRANATE Red : Active Group Names
          "#19B5FE", #[4] DODGER BLUE : Selected Group
          "#5A13F2", #[5] PURPLE : Focused Window Border, W-Clock          
          "#AB05F2", #[6] BRIGHT PURPLE:  Normal Window Border, W-NIC 
          "#2745F2", #[7] BLUE : Widget : Keyboard Layout
          "#C004D9", #[8] DARK PINK : Widget : Volume         
          )


##### Custom Layout Settings #####
layout_mtall = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 4,
    "margin": 2,
    "ratio": 0.6,
    "single_border_width" : 3,
    "single_margin" : 2,
                }

layout_mwide = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 4,
    "margin": 2,
    "single_border_width" : 3,
    "single_margin" : 2,
                }

layout_flo = {
    "border_focus": colorz[5],
    "border_normal": colorz[6],
    "border_width": 4,
    "fullscreen_border_width": 4,
    }
    
##### Layouts #####
layouts = [
    layout.MonadTall(**layout_mtall),
    layout.MonadWide(**layout_mwide),
    layout.Max(),                        
    layout.Floating(**layout_flo),

    ]


##### Key Bindings #####

keys = [
    Key(
        [mod], "Return",
        lazy.spawn("st"),
        desc="Launch simple Terminal"    
    ),
    
    Key(
        [mod, "shift"], "w",
        lazy.spawn("chromium"),
        desc="Launch Chromium Browser"    
    ),    
    
    Key(
        [mod, "shift"], "g",
        lazy.spawn("gedit"),
        desc="Launch Gnome Text Editor"    
    ),

    Key(
        [mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc="Exapand window (MTall), increase..."    
    ),    

    Key(   
        [mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Shrink window (MTall), decrease..."    
    ),      
    
    Key(   
        [mod], "k",
        lazy.layout.down(),
        desc="Switch between windows in current stack pane"    
    ),      

    Key(   
        [mod], "j",
        lazy.layout.up(),
        desc="Switch between windows in current stack pane"    
    ),      

    Key(   
        [mod], "n",
        lazy.layout.normalize(),
        desc="Normalize window size ratios"    
    ),  

    Key(   
        [mod, "shift"], "h",
        lazy.layout.swap_left(),
        desc="Move active window to left "    
    ), 

    Key(   
        [mod, "shift"], "l",
        lazy.layout.swap_right(),
        desc="Move active window to right "    
    ), 

    Key(   
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move active window to down"    
    ), 

    Key(   
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move active window to up"    
    ),             
    
    Key(   
        [mod, "shift"], "space",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc="Switch which side main pane occupies (MTall)"    
    ),  
    
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between different layouts"    
    ),

    Key(
        [mod], "w",
        lazy.window.kill(),
        desc="Kill active window"    
    ),

    Key(
        [mod, "control"], "r",
        lazy.restart(),
        desc="Restart/Reload Qtile"    
    ),
    
    Key(
        [mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"    
    ),
    
    Key(
        [mod], "r",
        lazy.spawncmd(),
        desc="Built-in Launcher"    
    ),

    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc="Toogle Floating"    
    ),

    Key(
        [mod, "shift"], "m",
        lazy.window.toggle_fullscreen(),
        desc="Toogle Fullscreen"    
    ),


]



##### Random Global Variables #####
# Custom Icon Paths for CurrentLayoutIcon Widget
wd_icon = [os.path.expanduser("~/.config/qtile/icons")]


##### Custom Widget Settings ######
widget_defaults = dict(
    font='Ubuntu',
    fontsize=14,
    padding=3,
    background=colorz[0], #Panel BG
)
extension_defaults = widget_defaults.copy()


##### Theme Settings for Widgets #####
# Widget Seperator
w_sep = {
    "background": colorz[0],
    "foreground": colorz[2],
    "linewidth":9,
    "size_percent":70,
    }
# Full Size Widget Seperator
f_w_sep = {
    "background": colorz[0],
    "foreground": colorz[0],
    "linewidth":2,
    "size_percent":100,
    }

        
# Widget GroupBox, This is not AGroupBox
w_gbox = {
    "active": colorz[3],
    "block_highlight_text_color": colorz[4],
    "borderwidth": 2,
    "inactive": colorz[2],
    "this_current_screen_border": colorz[1],
    "this_screen_border": colorz[2],
    }    


# Launcher
w_prompt = {
    "cursor_color": colorz[3],
    "padding": 5,
    "prompt": "Start:   ",
    }
    

# NIC : Network Interfaces    
w_net = {
    "background": colorz[6],
    "format": "{down} ↓↑ {up}",
    "interface": "wlx7cdd90399231",
    }

# Volume Widget
w_vol = {
    "background": colorz[8],
    "fmt": "🎧 {}",
    }
    
# Clock
w_clock = {
    "background": colorz[5],
    "format": "%d-%m-%Y %a %I:%M %p",
    }

# Keyboard layouts
w_key_l = {
    "background": colorz[7],
    "configured_keyboards": ['us','iq ku_ara','de','ar'],
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
                TextBox(text="🤗",
                    fontsize="20",
                    padding=5,),
                Prompt(**w_prompt,),
                WindowName(foreground=colorz[1]),

                Systray(),
                Sep(**f_w_sep),
                Net(**w_net),
                Sep(**f_w_sep),
                Volume(**w_vol),
                Sep(**f_w_sep),   
                Clock(**w_clock),
                Sep(**f_w_sep),
                KeyboardLayout(**w_key_l),
                Sep(**f_w_sep),
               
            ],
            30,
            opacity=0.95,
        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#http://docs.qtile.org/en/latest/manual/config/index.html
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(**layout_flo, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])

auto_fullscreen = False
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
