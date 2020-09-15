import threading
import socket
import time
import sys

class PortScanner:
    __returned_values = []

    def __init__(self,host):
        self.host = host
    
    def scan(self,port_number):
        temp_buffer = []
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            port_status = s.connect_ex((self.host,port_number))
        except ConnectionRefusedError:
            print("No connection could be made because the target machine actively refused it.")
        else:
            if port_status == 0:
                self.__returned_values.append(port_number)
        s.close()
        return self.__returned_values

    def scan_port(self,port_number):
        temp_buffer = []
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            port_status = s.connect_ex((self.host,port_number))
        except ConnectionRefusedError:
            print("No connection could be made because the target machine actively refused it.")
        else:
            if port_status == 0:
                self.__returned_values.append(port_number)
        s.close()
        temp_buffer = self.__returned_values
        self.__returned_values = []
        return temp_buffer
    
    def scan_range(self,first,last):
        temp_buffer = []
        for i in range(first,last):
            t = threading.Thread(target=self.scan,kwargs={'port_number':i})
            t.start()
        temp_buffer = self.__returned_values
        self.__returned_values = []
        return temp_buffer

    #it takes approximately 10 seconds
    def scan_all(self):
        temp_buffer = []
        for i in range(1,65536):
            t = threading.Thread(target=self.scan,kwargs={'port_number':i})
            t.start()
        temp_buffer = self.__returned_values
        self.__returned_values = []
        return temp_buffer

    #just for console usage
    def scan_all_for_console(self):
        temp_buffer = []
        for i in range(1,65536):
            t = threading.Thread(target=self.scan,kwargs={'port_number':i})
            t.start()
            sys.stdout.write("\r(%d/65535) ports scanned" % i)
            sys.stdout.flush()
        print("\n")
        temp_buffer = self.__returned_values
        self.__returned_values = []
        return temp_buffer



