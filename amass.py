#This module for using amass
# Passive Mode | Active Mode | Discover Ips
import os


def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def executeTerminalCommands_os(command):
    os.system(command)

def passiveDnsAmass(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('Amass Passive -> ',target)
        file = outputPath + target + '_Passive_Dns_enum.txt'
        command = 'amass enum -passive -norecursive  -d ' + target + ' -o ' + file
        executeTerminalCommands_os(command)

def acctiveDnsAmass(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('Amass Active Dns -> ',target)
        file = outputPath + target + '_Active_Dns_enum.txt'
        command = 'amass enum -active -d ' + target + ' -o ' + file
        executeTerminalCommands_os(command)

def ipDiscover(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('IP Discovery -> ',target)
        file = outputPath + target + '_IP_enum.txt'
        command = 'amass intel -ip -d ' + target + ' -o ' + file
        executeTerminalCommands_os(command)


#for Ips
def discoverDomainsWithIp(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('Discover domain names -> ',target)
        file = outputPath + target + '_Domain_enum.txt'
        command = 'amass intel -whois -addr ' + target + ' -o ' + file
        executeTerminalCommands_os(command)

#for Domains
def discoverDomains(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('Discover domain names -> ',target)
        file = outputPath + target + '_Domain_enum_d.txt'
        command = 'amass enum -d ' + target + ' -o ' + file
        executeTerminalCommands_os(command)


def discoverWebpages(targets,outputPath):
    outputPath = outputPath + 'amass/'
    makeDir(outputPath)
    for target in targets:
        print('Discover web pages -> ',target)
        file = outputPath + target + '_assets.txt'
        command = 'amass intel -include  ' + target + ' -whois  -active' +' -o ' + file
        executeTerminalCommands_os(command)

