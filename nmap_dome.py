#coding=utf-8
import nmap
nm = nmap.PortScanner()
nm.scan('121.42.136.115', '22-443')
nm.scaninfo()
nm.command_line()
