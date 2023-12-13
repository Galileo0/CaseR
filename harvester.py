#The Harvester Module
import os
import json



def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def executeTerminalCommands_os(command):
    os.system(command)

def readResultsFromFile(path,infoType):
    print(path)
    try:
        data = open(path)
        data = json.load(data)
        return data[infoType]
    except:
        print('Error Reading File')
        return []

def scanHarvester(targets,outputPath):
    outputPath = outputPath + 'theharvester/'
    makeDir(outputPath)
    all_hosts = []
    all_ips = []
    for target in targets:
        file = outputPath + target + '_Harvester.json'
        print(file)
        command = 'theHarvester -d ' + target + ' -b all -f ' + file
        print(command)
        finalResult = []
        print('The Harvester -> ',target)
        executeTerminalCommands_os(command)
        print('Load Data To run Time')
        hosts = readResultsFromFile(file,'hosts')
        ips = readResultsFromFile(file,'ips')

        for host in hosts:
            all_hosts.append(host)
        
        for ip in ips:
            all_ips.append(ip)
    
    return all_hosts,all_ips
