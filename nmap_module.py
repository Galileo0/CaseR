import subprocess
import os
#Global Information



#def executeTerminalCommands(command):
#    exe = subprocess.run(command,capture_output=True)
#    output = str(exe.communicate())
#    print(output)

def executeTerminalCommands_os(command):
    os.system(command)

def pingScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_pingScan.xml'
    command_temp = 'nmap -sP '+target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_pingScan.xml -o '+ outputPath+target+'_pingScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)


def tcpScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_tcpScan.xml'
    command_temp = 'nmap -sT '+target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_tcpScan.xml -o '+ outputPath+target+'_tcpScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)


def udpScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_udpScan.xml'
    command_temp = 'nmap -sU '+target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_udpScan.xml -o '+ outputPath+target+'_udpScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)


def serviceScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_serviceScan.xml'
    command_temp = 'nmap -sV '+target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_serviceScan.xml -o '+ outputPath+target+'_serviceScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)


def vulnNSEScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_VulnNSEScan.xml'
    command_temp = 'nmap -sV  --script vuln ' +target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_VulnNSEScan.xml -o '+ outputPath+target+'_VulnNSEScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)


def vulnersScan(target,outputPath):
    outputFile = '-oX ' +outputPath+target+'_VulnNSEScan.xml'
    command_temp = 'nmap -sV  --script vulners '+target+ ' '
    command = command_temp+' '+outputFile
    convertToHtmlReportCommand = 'xsltproc ' + outputPath+target+'_VulnersScan.xml -o '+ outputPath+target+'_VulnersScan.html'
    executeTerminalCommands_os(command)
    executeTerminalCommands_os(convertToHtmlReportCommand)
