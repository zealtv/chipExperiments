This is where I'll dump my chip experimentations.  -- currently looking into osc communication using pure data as well as serial communication with arduino.  Will likely have a crack at getting openframeworks running also.

```
set up openFrameworks see: https://github.com/zealtv/ofInstallChip
install python GPIO library: https://github.com/xtacocorex/CHIP_IO

install puredata:
sudo apt-get install puredata pd-zexy pd-osc pd-comport pd-hid

add folowing lines to /etc/security/limits.conf
@audio - rtprio 99
@audio - memlock unlimited

get xbox 360 usb guitar hero controller running:
sudo apt-get install xboxdrv
cp org.seul.Xboxdrv.conf /etc/dbus-1/system.d/
sudo reboot
sudo xboxdrv -D --detach --silent 
```


