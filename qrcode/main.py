# wifi Qrcode
# pip install qrcode
import qrcode
# wifi name
wifi_name = 'wifi_name'
# wifi password
wifi_password = 'wifi_password'
# wifi type
wifi_type = 'WPA'
# wifi qrcode
wifi_qrcode = qrcode.make('WIFI:T:' + wifi_type + ';S:' + wifi_name + ';P:' + wifi_password + ';;')
# save wifi qrcode
wifi_qrcode.save('wifi_qrcode.png')
