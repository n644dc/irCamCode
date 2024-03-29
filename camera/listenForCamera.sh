#! /bin/sh

### BEGIN INIT INFO
# Provides:          cameraListener.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system

case "$1" in
  start)
    echo "STARTING CAMERA LISTENER"
	sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/usb
    sudo /usr/local/bin/cameraListener.py &
    ;;
  stop)
    echo "STOPPING CAMERA LISTENER"
    sudo pkill -f /usr/local/bin/cameraListener.py
    ;;
  *)
    echo "Usage: /etc/init.d/listenForCamera.sh {start|stop}"
    exit 1
    ;;
esac

exit 0