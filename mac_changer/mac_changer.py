# !/user/bin/python3
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change mack address. Example- eth0, wlan0")
    parser.add_option("-m", "--mac", dest="set_mac", help="Set MAC address. sure it will 12 characters")
    return parser.parse_args()


def change_mac(interface, set_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", set_mac])
    subprocess.run(["ifconfig", interface, "up"])

    print("[+] Change MAC address " + interface + " to " + set_mac)


(options, argument) = get_arguments()
interface = options.interface or input("interface > ")
set_mac = options.set_mac or input("set Mac > ")

change_mac(interface, set_mac)
