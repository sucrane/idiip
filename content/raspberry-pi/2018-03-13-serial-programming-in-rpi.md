Title: Serial Programming in Raspberry Pi
Date: 2018-03-13

Raspberry Pi uses serial port for console tty. In order to use this serial port to communicate with Mac machine, we will temporarily disable getty service:

```
$ sudo systemctl stop serial-getty@ttyS0.service
$ sudo chmod 666 /dev/ttyS0
```

Then the application can use `/dev/ttyS0` to communicate with other device using serial cable.