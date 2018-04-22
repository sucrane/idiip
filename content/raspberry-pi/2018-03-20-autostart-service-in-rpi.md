Title: Autostart Service in Raspberry Pi
Date: 2018-03-20

If our application needs to autostart as a service in Raspberry Pi, we will write a simple `systemd` service file.
```
[Unit]
Description=Example Application
After=bluetooth.service
Requires=bluetooth.service

[Service]
PermissionsStartOnly=true
Type=simple
User=pi
Group=pi
ExecStartPre=/bin/mkdir -p /var/log/example_app
ExecStartPre=/bin/chown pi:pi /var/log/example_app
ExecStart=/home/pi/bin/example-app
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

The key point here is that our application needs Bluetooth service before it can run. So we put
```
After=bluetooth.service
Requires=bluetooth.service
```

in the `[Unit]` section.

Copy the above file to `/lib/systemd/system/`, and do the following:
```
$ sudo chmod 644 /lib/systemd/system/example-app.service
$ sudo systemctl enable example-app.service
$ sudo reboot
```

Besides, you can manually start/stop the service.
```
$ sudo systemctl start smartblock.service
$ sudo systemctl stop smartblock.service
```