import subprocess
# for commandline inputs
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='Interface whose mac address required to be changed')
parser.add_option('-m', '--mac', dest='new_mac', help='The new MAC address')
(options, arguments) = parser.parse_args()

# input from user after displaying message
# interface = input("interface >")
interface = options.interface

# input from user after displaying message
# new_mac = input('new MAC (00:XX:XX:XX:XX:XX)>')
new_mac = options.new_mac

print('[+] Changing mac address for ' + interface + ' to ' + new_mac)

print("ifconfig " + interface + " down")
# subprocess.call("ifconfig " + interface + " down", shell=True)
# more secure option
subprocess.call(["ifconfig", interface, "down"])

print("ifconfig " + interface + " hw ether " + new_mac)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# more secure option
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

print("ifconfig " + interface + " up")
# subprocess.call("ifconfig " + interface + " up", shell=True)
# more secure option
subprocess.call(["ifconfig", interface, "up"])

