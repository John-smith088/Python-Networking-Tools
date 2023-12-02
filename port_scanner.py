import nmap, sys

def scan_open_ports(scanner):
    if (len(sys.argv) < 3):
        ip = input("Enter the ip address: ")
        portrange = input("Enter the port range: ")
    else:
        ip = sys.argv[1]
        portrange = sys.argv[2]
    
    scanResults = ""
    try:
        scanner.scan(ip, portrange)
    except:
        print("Error scanning IP with designated port range")

    for host in scanner.all_hosts():
        hostName = scanner[host].hostname()
        if (hostName):
            scanResults += f"Host : {host} ({scanner[host].hostname()})\n"
        else:
            scanResults += f"Host : {host} ({'Could not resolve hostname'})\n"
        scanResults += f"State : {scanner[host].state()}\n"
        for protocol in scanner[host].all_protocols():
            scanResults += "\n---------\n\n"
            scanResults += f"Protocol : {protocol}\n"

            portList = scanner[host][protocol].keys()
            for port in portList:
                scanResults += f"port : {port}\tstate : {scanner[host][protocol][port]['state']}\n"
                
    save_to_file(scanResults)
    return scanResults

def save_to_file(scanResults):
    #when done ask if they want results printed to sent to file
    while (True):
        try:
            saveToFile = input("Save scan results to file(Y/N): ").lower()
        except AttributeError:
            saveToFile = input("Invalid input.\nSave scan results to file(Y/N): ")
        while (saveToFile != 'y' and saveToFile != 'n'):
            saveToFile = input("Invalid input.\nSave scan results to file(Y/N): ")
        break

    if (saveToFile == 'y'):
        fileName = input("Enter the filename to save scan results to: ")
        with open(fileName, "w") as resultsFile:
            resultsFile.write(scanResults)
        print(f"Results saved to {fileName + '.txt'}!\n")
    return

def get_tool_choice():
    toolChoices = '''Networking tool choices:
    0) exit
    1) port scanner
    '''
    print(toolChoices)
    toolChoice = input("What tool would you like to run: ")
    while not((toolChoice.isdigit()) and (0 <= int(toolChoice) <= 1)):
        toolChoice = input("Invalid choice, try again: ")
    toolChoice = int(toolChoice)
    return toolChoice

def main():
    nmapPath = r"C:\Program Files (x86)\Nmap"
    nmapPath2 = "C:\\Program Files (x86)\\Nmap\\"
    nmapPath3 = "C:\\Program Files (x86)\\Nmap\\nmap.exe"

    #initialize
    #print(f"Scotts {sys.argv[0]}!\n")
    nmScanner = nmap.PortScanner(nmap_search_path=(nmapPath, nmapPath2, nmapPath3))

    running = True #set the program to running
    while (running):
        toolChoice = get_tool_choice()
        if (toolChoice == 0):
            running = False
        if (toolChoice == 1):
            scanResults = scan_open_ports(nmScanner)
            print(f"{scanResults}\n")
    return

if __name__ == '__main__':
    main()