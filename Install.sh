sudo apt update && sudo apt full-upgrade --assume-yes
echo "\ndtparam=i2c_vc=on" > /boot/config.txt
sudo raspi-config nonint do_i2c 0
