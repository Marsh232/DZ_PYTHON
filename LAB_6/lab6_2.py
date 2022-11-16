import csv
import glob
import re

def write_dhcp_snooping_to_csv(filenames, output):
    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
    with open(output, "w") as dest:
        writ_output = csv.writer(dest)
        writ_output.writerow(["switch", "mac", "ip", "vlan", "interface"])
        for file_name in filenames:
            sw = re.search("([^/]+)_dhcp_snooping.txt", file_name).group(1)
            with open(file_name) as f:
                for line in f:
                    hz = re.search(regex, line)
                    if hz:
                        writ_output.writerow((sw,) + hz.groups())


if __name__=='__main__':
    names_files = glob.glob("*_dhcp_snooping.txt")
    write_dhcp_snooping_to_csv(names_files, "output.csv")