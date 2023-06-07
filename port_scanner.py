import socket
class port_scanner:
    # program information
    def __init__(self):
        print('********************************************************')
        print("**", "This program is port scanner to find the open port", "**")
        print('********************************************************')
        print("Please, Select your option: ")
        print("1) Enter the website or the IP for target")
        print("2) Exit The program")
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
                    break
                else:
                    print("choose between 1 or 2")
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

#Run the class
port = port_scanner()
