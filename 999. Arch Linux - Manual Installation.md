
# Manual Installation for Awesome WM

1. `loadKeys la-latin1` **Set the language for the keyboard**
2. `ls /sys/firmware/efi/efivars` **If the system is not UEFI try BIOS**
3. `timedatectl set-ntp true`
4. Partitioning the disk _boot, root and swap_ with `cfdisk`
  - Set the size for the partitions select the **type** and finally **Write** them all.
  - You can see the result with `lsblk`

## Boot
- `mkfs.vfat -F 32 /dev/sda1`
## Root
- `mkfs.ext4 /dev/sda2`
## Swap
- `mkswap /dev/sda3`
- `swapon /dev/sda3`

# 5. Mount the Partitions

## Root
- `mount /dev/sda2 /mnt`
## Boot
- `mkdir /mnt/boot`
- `mount /dev/sda1 /mnt/boot`

# 6. Install utilities

- `pacman -Sy archlinux-keyring && pacman -Su`
- `pacman-key --init` **This is optional**
- `/mnt linux linux-firmware base base-devel networkmanager grub wpa_supplicant`

# 7. Make the fstab and use root into the system

- `genfstab -U /mnt > /mnt/etc/fstab` **You can make a `cat` for see the content**
- `arch-chroot /mnt`
# 8. Making the users and set the passwords

- `passwd`
- `useradd -m archuser` 
- `passwd archuser` 
- `usermod -aG wheel archuser` **Check If the user is in the group with the command `groups archuser`

# 9. Install and set the Sudo/ers files 

- `pacman -S sudo vim nano` 
- `vim /etc/sudoers` **Uncomment the `%Wheel` line who require password for all users**

# 10. Set the localtime and the 

- `timedate list-timezones`
- `ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime`
- `hwclock --systohc`

# 11. Regions

- `vim /etc/locale.gen` and uncomment
	- en US.UTF-8
	- es CO.UTF-8 **This is optional**
- `local-gen`
- `vim /etc/vconsole.conf` **For the loadkeys on the keyboard** 
	- `KEYMAP=la-latin1`

# 12. Install Grub

- `grub-install /dev/sda` 
- `grub-mkconfig -o /boot/grub/grub.cfg`

# 13. Set the Hostname and Loopback

- `echo archlinuxpen300 > /etc/hostname`
- `nano /etc/hosts`

127.0.0.1       localhost
::1                  localhost
127:0.1.1       archlinuxpen300.localhost archlinuxpen300

- `pacman -S neofetch` 

- `exit`
- `reboot now`

---

# 14. First login with normal user

- `sudo systemctl start NetworkManager.service`
- `sudo systemctl enable NetworkManager
- `sudo systemctl start wpa_supplicant.service
- `sudo systemctl enable wpa_supplicant.service

# 15. Install more packages

-  `sudo pacman -S xf86-video-intel intel-ucode
-  `sudo pacman -S mesa mesa-demos 
- `sudo pacman -S xorg xorg-server
- `sudo pacman -S kitty` **Use git kitty like an alternative**
- `git clone https://aur.archlinux.org/paru-bin.git` **Enable AUR**
- `makepkg -si

# 16 . EN4BLE BLACK ARCH REP0SITORY

- `curl -O https://blackarch.org/strap.sh
- `chmod +x strap.sh
- `sudo ./strap.sh
- `sudo pacman -Sy && pacman -S nmap

# 17. Install the lightdm login for the system

- `sudo pacman -S lightdm  lightdm-gtk-greeter
- `vim /etc/lightdm/lightdm.conf
- `greeter-session=lightdm-gtk-greeter
- `sudo systemctl enable lightdm.service
- `lightdm --test-mode --debug` **Testing the service** 

## For Vmware installation

- `sudo pacman -S gtkmm`
- `sudo pacman -S open-vm-tools`
- `sudo pacman -S xf86-video-vmware xf86-input-vmmouse`
- `sudo systemctl vmtoolsd`

---------------------------------------------------------------------------
---------------------------------------------------------------------------
 
if yay/paru present multilib error, it's because in the pacman.conf exist a duplicate of a mirrorlist or a repository

#### Awesome - Windows Manager  
dotfiles[^1][^2][^3]

- `paru -Sy awesome` **proof install the tools one by one**
- `picom-jonaburg-git rofi acpi acpid acpi_call upower lxappearance jq inotify-tools polkit-gnome xdotool xclip gpick ffmpeg blueman pipewire pipewire-pulse pipewire-alsa alsa-utils brightnessctl feh maim mpv mpd mpc mpdris2 python-mutagen ncmpcpp playerctl flameshot polybar
- `systemctl enable mpd.service
- `systemctl start mpd.service

- `sudo apt install xbacklight alsa-utils brightnessctl` ***The brightnessctl works***
- `sudo apt install kmix budgie-network-manager-applet` ***Optional***

### Kitty and ZSH

LINK: https://github.com/xqrr3db4ck/Awesome.git

- `echo $SHELL`
- `sudo su`
- `usermod --shell /usr/bin/zsh`
- `sudo apt install zsh-syntax-highlighting zsh-autosuggestions`

#### PowerLevel10K
##### - Manual installation - 

- `git clone https://github.com/romkatv/powerlevel10k#manual`
- `zsh `

---
[^1]:https://github.com/rxyhn/dotfiles
[^2]:https://github.com/rxyhn/yoru/wiki/Detailed-Setup#dependencies
[^3]:https://www.youtube.com/watch?v=FsnMkicU_Hw