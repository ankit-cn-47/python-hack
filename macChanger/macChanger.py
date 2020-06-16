import subprocess
import optparse
import re


def mac_changer(interface, new_mac):
    print('[+] Changing mac address for ' + interface + ' to ' + new_mac)
    # print("ifconfig " + interface + " down")
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # more secure option
    subprocess.call(["ifconfig", interface, "down"])

    # print("ifconfig " + interface + " hw ether " + new_mac)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # more secure option
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # print("ifconfig " + interface + " up")
    # subprocess.call("ifconfig " + interface + " up", shell=True)
    # more secure option
    subprocess.call(["ifconfig", interface, "up"])


# for commandline inputs
def get_args():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface whose mac address required to be changed')
    parser.add_option('-m', '--mac', dest='new_mac', help='The new MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please specify interface, use --help for more info')
    elif not options.new_mac:
        parser.error('[-] Please specify mac address, use --help for more info')
    return options


def get_current_mac_address(interface):
    try:
        ifconfig_result = subprocess.check_output(['ifconfig', interface])
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if ifconfig_result and mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print('[-] Sorry could not find the MAC address')
    except:
        print('[-] Sorry could not find the MAC address')
        exit(1)


# input from user after displaying message
# interface = input("interface >")

# input from user after displaying message
# new_mac = input('new MAC (00:XX:XX:XX:XX:XX)>')

option = get_args()
current_mac = get_current_mac_address(option.interface)
get_current_mac_address(option.interface)
print("Current MAC : " + str(current_mac))

mac_changer(option.interface, option.new_mac)

current_mac = get_current_mac_address(option.interface)
if current_mac == option.new_mac:
    print('[+] MAC address successfully changed to ' + current_mac)
else:
    print('[-] Sorry, MAC address was not changed')
