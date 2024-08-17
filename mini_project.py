import time
import network
import urequests
def send_sms(ssid, password, recipient, sender,
 message, auth_token, account_sid):
 wlan = network.WLAN(network.STA_IF)
 wlan.active(True)
 wl*an.connect(ssid, password)
 while max_wait > 0:
 if wlan.status() < 0 or wlan.status() >= 3:
 break
 max_wait -= 1
 print('waiting for connection...')
 time.sleep(1)
 # Handle connection error
 if wlan.status() != 3:
 raise RuntimeError('network connection failed')
 else:
 print('connected')
 status = wlan.ifconfig()
 #print('ip = ' + status[0])
 
 headers = {'Content-Type': 'application/x-www-form-urlencoded'}
 data = "To=" + recipient + "&From=" + sender + "&Body=" + message
 print("Attempting to send SMS")
 r = urequests.post("https://api.twilio.com/2010-04-01/Accounts/" +
 account_sid + "/Messages.json",
 data=data,
 auth=(account_sid,auth_token),
 headers=headers)
 if r.status_code >= 300 or r.status_code < 200:
 print("There was an error with your request to send a message. \n" +
 "Response Status: " + str(r.status_code))
 else:
 print("Success")
 print(r.status_code)
 r.close()
import machine
import time
trigger = machine.Pin(2, machine.Pin.OUT)
echo = machine.Pin(3, machine.Pin.IN)
while True:
 trigger.low()
 time.sleep_us(2)
 trigger.high()
 time.sleep_us(10)
 trigger.low()
 
 while echo.value() == 0:
 pass
 pulse_start = time.ticks_us()
 
 while echo.value() == 1:
 pass
 pulse_end = time.ticks_us()
 +
 P*ulse_duration = pulse_end - pulse_start
 distance = pulse_duration / 58
 
 print("Distance:", distance, "cm")
 time.sleep(1)
 if(distance>10):
 send_sms('OPPO Reno6 5G','jana 
kutty','+91/mobilenumber/','+12/twiligo number/','locker was 
opened','twiligo id','twiligo password')