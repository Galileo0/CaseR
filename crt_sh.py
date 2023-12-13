#This module responisble to fetch information from crt.sh site
import requests
import os
import re
site = 'https://crt.sh/?q='




def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)



def gueryResults(targets,outputPath):
    outputPath = outputPath + 'crt_sh/'
    makeDir(outputPath)
    allGatheredData = []
    for target in targets:
        finalResult = []
        res = requests.get(site+target)
        out = re.findall('(?:[a-z0–9](?:[a-z0–9-]{0,61}[a-z0–9])?\.)+[a-z0–9][a-z0–9-]{0,61}[a-z0–9]',str(res.text))
        #Get info related to target
        regex2 = "((.+?\.)?"+target+"(\/[A-Za-z0-9\-\._~:\/\?#\[\]@!$&'\(\)\*\+,;\=]*)?)"
        verifyier = re.compile(regex2)
        for x in out:
            if x not in finalResult:
                if(re.search(verifyier,x)):
                    finalResult.append(x)
                    allGatheredData.append(x)
        print(finalResult)
        fileName = outputPath + target+'_crt.html'
        file = open(fileName,'w')
        file.write(res.text)
        file.close()
        #save_final_domains 
        fileName = outputPath + target+'_crt_extracted_Data.txt'
        file = open(fileName,'w')
        for info in finalResult:
            file.write(info+'\n')
        file.close()
    return allGatheredData
