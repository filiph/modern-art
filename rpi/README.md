# Run on Raspberry Pi

Instructions below work with https://www.raspberrypi.org/forums/viewtopic.php?f=41&t=43285

## Build framebuffer overlay:

The framebuffer overlay definition file for Sainsmart 18:
https://raw.githubusercontent.com/notro/fbdbi/master/dts/overlays/rpi/sainsmart18X-overlay.dts

Here are the steps

https://github.com/notro/fbtft/wiki/FBTFT-RPI-overlays

    wget -c https://raw.githubusercontent.com/RobertCNelson/tools/master/pkgs/dtc.sh
    chmod +x dtc.sh
    ./dtc.sh

Compile dtb and put it directly into it's destination:
  
    sudo dtc -@ -I dts -O dtb -o /boot/overlays/foo-overlay.dtb foo-overlay.dts

Load the overlay by adding this to /boot/config.txt:

    dtoverlay=foo

Then reboot to load the overlay.

