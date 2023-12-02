import port_scanner as portScanner
def main():
    running = True #set the program to running
    while (running):
        toolChoice = portScanner.get_tool_choice()
        if (toolChoice == 0):
            running = False
        if (toolChoice == 1):
            scanResults = portScanner.scan_open_ports()
            print(f"{scanResults}\n")
    return

if __name__ == '__main__':
    main()