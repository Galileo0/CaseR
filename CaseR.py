#imports 
from datetime import datetime
from dotenv import load_dotenv
import os
import nmap_module as nm
import crt_sh as crt
import amass
import harvester as hr

targetName = ''
targetIps = []
targetDomains = []
#Run Time Data
runTimeData = []
crtRunTimeData = []
theHarvesterRunTimeData_hosts = []
theHarvesterRunTimeData_ips = []
#output
outputPath = '/output/'

def makeTargetDir(targetName):
    global outputPath
    dir_path = os.getcwd()
    outputPath = dir_path+outputPath+targetName+'/'
    os.mkdir(outputPath)

def main():
    global targetName
    global targetIps
    global targetDomains
    load_dotenv()

    print('''
        Welcome To CaseR 
            [CyberGuarD]
        Author: Ahmed Zakaria @Galmood
        V:1.0

        ''')

    currentDateTime = datetime.now()
    currentDateTime = currentDateTime.strftime('%d_%m_%Y_%H_%M')
    print('Timestamp -> ', currentDateTime)
    targetName = input('Target Name -> ')
    makeTargetDir(targetName+'_'+currentDateTime)
    #TakeIPs
    tempIps = input('Target Ips Seperated By , -> ')
    tempDomains = input('Target Domains Seperated By , -> ')
    targetIps = tempIps.split(',')
    targetDomains = tempDomains.split(',')
    print('')
    print('----- Target Ips -----')
    for ip in targetIps:
        print(ip)

    print('----- Target Domains -----')
    for domain in targetDomains:
        print(domain)
    
    #Execution
    if(os.environ.get("crt_sh") == 'True'):
        print('--- crt.sh Module ---')
        searchByCrt()
    
    if(os.environ.get("amass") == 'True'):
        print('--- amass Module ---')
        amassScan()

    if(os.environ.get("theHarvester") == 'True'):
        print('--- theHarvester Module ---')
        harvesterScan()

    if(os.environ.get("nmap") == 'True'):
        print('--- Nmap Module ---')
        scanNamp()
    

def scanNmapCustom(targets):
    for traget in targets:
        if(os.environ.get("nmap_ping_scan") == 'True'):
            print('Ping Scan -> ',traget)
            nm.pingScan(traget,outputPath)
        if(os.environ.get("nmap_tcp_scan") == 'True'):
            print('TCP Scan -> ',traget)
            nm.tcpScan(traget,outputPath)
        if(os.environ.get("nmap_udp_scan") == 'True'):
            print('UDP Scan -> ',traget)
            nm.udpScan(traget,outputPath)
        if(os.environ.get("nmap_service_scan") == 'True'):
            print('Service Detection Scan -> ',traget)
            nm.serviceScan(traget,outputPath)
        if(os.environ.get("nmap_vulnNSE_scan") == 'True'):
            print('Vuln NSE Scan -> ',traget)
            nm.vulnNSEScan(traget,outputPath)
        if(os.environ.get("nmap_vulners_scan") == 'True'):
            print('Vulners Scan -> ', traget)
            nm.vulnersScan(traget,outputPath)



def scanNamp():
    global targetIps
    global targetDomains
    global outputPath
    global crtRunTimeData
    global theHarvesterRunTimeData_hosts
    global theHarvesterRunTimeData_ips

    for ip in targetIps:
        if(os.environ.get("nmap_ping_scan") == 'True'):
            print('Ping Scan -> ',ip)
            nm.pingScan(ip,outputPath)
        if(os.environ.get("nmap_tcp_scan") == 'True'):
            print('TCP Scan -> ',ip)
            nm.tcpScan(ip,outputPath)
        if(os.environ.get("nmap_udp_scan") == 'True'):
            print('UDP Scan -> ',ip)
            nm.udpScan(ip,outputPath)
        if(os.environ.get("nmap_service_scan") == 'True'):
            print('Service Detection Scan -> ',ip)
            nm.serviceScan(ip,outputPath)
        if(os.environ.get("nmap_vulnNSE_scan") == 'True'):
            print('Vuln NSE Scan -> ',ip)
            nm.vulnNSEScan(ip,outputPath)
        if(os.environ.get("nmap_vulners_scan") == 'True'):
            print('Vulners Scan -> ', ip)
            nm.vulnersScan(ip,outputPath)
    
    for domain in targetDomains:
        if(os.environ.get("nmap_ping_scan") == 'True'):
            print('Ping Scan -> ',domain)
            nm.pingScan(domain,outputPath)
        if(os.environ.get("nmap_tcp_scan") == 'True'):
            print('TCP Scan -> ',domain)
            nm.tcpScan(domain,outputPath)
        if(os.environ.get("nmap_udp_scan") == 'True'):
            print('UDP Scan -> ',domain)
            nm.udpScan(domain,outputPath)
        if(os.environ.get("nmap_service_scan") == 'True'):
            print('Service Detection Scan -> ',domain)
            nm.serviceScan(domain,outputPath)
        if(os.environ.get("nmap_vulnNSE_scan") == 'True'):
            print('Vuln NSE Scan -> ',domain)
            nm.vulnNSEScan(domain,outputPath)
        if(os.environ.get("nmap_vulners_scan") == 'True'):
            print('Vulners Scan -> ', domain)
            nm.vulnersScan(domain,outputPath)
    
    #harvester & crt Scan 

    if(os.environ.get("nmap_scan_harvester_results") == 'True'):
        print('--- Scan TheHarvester Results ---')
        scanNmapCustom(theHarvesterRunTimeData_ips)
        scanNmapCustom(theHarvesterRunTimeData_hosts)
    
    if(os.environ.get("nmap_scan_crt_results") == 'True'):
        print('--- Scan Crt.sh Results ---')
        scanNmapCustom(crtRunTimeData)


def handelRunTimeData(data):
    global runTimeData
    for x in data:
        runTimeData.append(x)

def searchByCrt():
    global targetIps
    global targetDomains
    global outputPath
    out1 = crt.gueryResults(targetIps,outputPath)
    out2 = crt.gueryResults(targetDomains,outputPath)
    handelRunTimeData(out1)
    handelRunTimeData(out2)

def amassScan():
    global targetIps
    global targetDomains
    global outputPath
    amass.passiveDnsAmass(targetDomains,outputPath)
    amass.ipDiscover(targetDomains,outputPath)
    amass.discoverDomainsWithIp(targetIps,outputPath)
    amass.discoverDomains(targetDomains,outputPath)
    amass.discoverWebpages(targetDomains,outputPath)
    amass.acctiveDnsAmass(targetDomains,outputPath)

def harvesterScan():
    global targetDomains
    global outputPath
    global theHarvesterRunTimeData_hosts 
    global theHarvesterRunTimeData_ips 
    theHarvesterRunTimeData_hosts , theHarvesterRunTimeData_ips = hr.scanHarvester(targetDomains,outputPath)

main()