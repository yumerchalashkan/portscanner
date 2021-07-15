# Portscanner
A minimal library that scans ports and finds open ports
## Usage
There are two different usage, code and console.
### Usage in code
<i><b>scan_port()</b></i> method is used to scan only one port. If the port to be scanned is closed, it returns an empty array. Otherwise, it returns an array with a port number in it.
```python
from portscanner import *

p = PortScanner("109.232.216.33")

result = p.scan_port(80) #for open port
print(result) #output: [80]

result = p.scan_port(81) #for closed port
print(result) #output: []
```

<i><b>scan_range()</b></i> method is used to scan that a certain range. Returns open ports in an array if a specified range of ports are open.
```python
from portscanner import *

p = PortScanner("109.232.216.33")

result = p.scan_range(1,1000)
print(result) #output: [25, 21, 80, 53, 110, 143, 443, 465]
```

<i><b>scan_all()</b></i> method is used to scan that all open ports. Returns open ports in an array if a specified range of ports are open. This method may take about 10 seconds to finish.
```python
from portscanner import *

p = PortScanner("109.232.216.33")

result = p.scan_all() #output: [21, 25, 53, 80, 110, 143, 465, 443, 587, 993, 995, 2078, 2095, 2077, 2083, 2087, 2086, 2096, 2082, 33410]
print(result)
```
### Usage in console
For linux
```c
./nscan.py 80                //to scan only one port.
./nscan.py -range 1 1000     //to scan the range 1 and 1000
./nscan.py -all       //to scan all open ports
```
For windows
```c
python nscan.py 80                 //to scan only one port.
python nscan.py -range 1 10000     //to scan the range 1 and 1000
python nscan.py -all               //to scan all open ports
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
