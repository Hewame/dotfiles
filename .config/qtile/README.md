# Qtile
> This demo instructed on a minimal Debian 10 installation.
> No GUI, Desktop Environment and GUI based Xsession manager at all.

#### Installing requirements

```console
~$ sudo apt install xorg python3-dbus python-gobject python3-pip git alsa-utils fonts-noto-color-emoji
~$ sudo apt install libxcb-render0-dev libffi-dev libcairo2 libpangocairo-1.0-0 libxcb-cursor0 
~$ pip3 install xcffib
~$ pip3 install psutil
~$ pip3 install --no-cache-dir cairocffi
```
#### Installing Qtile, running on Python3

With the dependencies in place, run the following commands to
install latest Qtile from source.

```console
~$ git clone git://github.com/qtile/qtile.git
~$ cd qtile
~$ pip3 install .
```

#### Add Qtile to your system PATH
```console
~$ echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
~$ source ~/.bashrc
```

#### Execute Qtile after starting Xsession
```console
~$ vim ~/.xinitrc
#!/bin/sh

nitrogen --restore &
qtile
```

#### Start Xsession
```console
~$ startx
```

#### Debugging
```console
~$ more ~/.local/share/qtile/qtile.log
~$ qtile -l
```
---

#### Virtualbox Users (Optional)

If you would like to get the Full size screen follow this
[instruction](https://forums.virtualbox.org/viewtopic.php?t=15679 "Install Linux Guest Additions") or run the following commands:

```console
~$ sudo apt install dkms build-essential linux-headers-$(uname -r)
~$ sudo mount /dev/sr0 /media/cdrom ; cd /media/cdrom
~$ sudo sh ./VBoxLinuxAdditions.run
```










