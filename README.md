This is where I'll dump my chip experimentations.  -- currently looking into osc communication using pure data as well as serial communication with arduino.  Will likely have a crack at getting openframeworks running also.


#### approximate set up:
```
cd /etc/systemd/system/
sudo nano tightvncserver.service
Paste the following text into the editor:

[Unit]
Description=TightVNC remote desktop server
After=sshd.service

[Service]
Type=forking
ExecStart=/usr/bin/tightvncserver :1
User=chip

[Install]
WantedBy=multi-user.target

Exit the editor, saving the file.
sudo chown root:root tightvncserver.service
sudo chmod 755 tightvncserver.service
sudo systemctl enable tightvncserver.service

chip@chip:~$ sudo tightvncserver -geometry 800x600
systemctl start tightvncserver.service

chip@chip:~$ systemctl status tightvncserver.service
● tightvncserver.service - TightVNC remote desktop server
   Loaded: loaded (/etc/systemd/system/tightvncserver.service; disabled)
   Active: active (running) since Sat 2016-11-12 08:51:13 UTC; 34s ago
  Process: 958 ExecStart=/usr/bin/tightvncserver :1 (code=exited, status=0/SUCCESS)
   CGroup: /system.slice/tightvncserver.service
           ├─966 Xtightvnc :1 -desktop X -auth /home/chip/.Xauth...
           └─976 /usr/bin/openbox --startup /usr/lib/arm-linux-g...
chip@chip:~$


sudo apt-get install puredata pd-zexy pd-osd etc   
// or
vnc in
(from client) xtightvncviewer 192.168.1.110:1
install pd via synaptic

if synaptic won't run, run from  menu - system - root terminal
```
