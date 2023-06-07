import socket
#list of ports
#ports = [20, 21, 23, 53, 80, 110, 119, 123, 143, 161, 194, 443]
class port_scanner:
    # program information
    def __init__(self):
        print('********************************************************')
        print("**", "This program is port scanner to find the open port", "**")
        print('********************************************************')
        print("Please, Select your option: ")
        print("1) Enter the website or the IP for target")
        print("2) Add port in port list")
        print("3) show existing port")
        print("4) exit the program")
        self.target()
    #the program options
    def target(self):
        while True:
            try:
                target = int(input("Please, Enter your option: "))
                if target == 1:
                    print("port scanner for website or ip ")
                    self.port_scan()
                elif target == 2:
                    print("Add New port on list")
                    self.add_port()
                elif target == 3:
                    print("The existing port")
                    self.exsisting_port()
                elif target == 4:
                    break
                else:
                    print("choose between 1 , 2 , 3 or 4")
            except Exception:
                print("You Enter not valid option")
    # Port scanner option
    def port_scan(self):
        t = input("Enter target IP or website: ")
        end = int(input("Enter the end port you want scan: "))
        speed = float(input("Enter The scan speed by second: "))
        for p in range(1,end):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(speed)
            r = s.connect_ex((t,p))
            if r == 0:
                service = socket.getservbyport(p)
                print("The port {} is open --> {}".format(p,service))
    #add port in program to scan the target
    def add_port(self):
        item = int(input("Enter The port number: "))
        ports.append(item)
        print(ports)
    # show the ports in program
    def exsisting_port(self):
        print(ports)
#Run the class
port = port_scanner()