import subprocess

interface = input("interface >")

new_mac = input('new MAC (00:XX:XX:XX:XX:XX)>')

print('[+] Changing mac address for ' + interface + ' to ' + new_mac)

print("ifconfig " + interface + " down")
subprocess.call("ifconfig " + interface + " down", shell=True)

print("ifconfig " + interface + " hw ether " + new_mac)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)

print("ifconfig " + interface + " up")
subprocess.call("ifconfig " + interface + " up", shell=True)

