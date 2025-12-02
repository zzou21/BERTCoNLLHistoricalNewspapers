# This file creates one standardized testing file forCS 372. It creates one JSON by merging all TXT newspaper content from cleaned newspapers. I've already run this code before submitting the project, and you can find the merged JSON at "newspaperCleanedContent.json"
'''Code written by me'''

import os, json

def turnTXTFilesIntoJSON(folderOfTXT, JSONPath):
    dictOfValidTXTs = {}
    for oneTXT in os.listdir(folderOfTXT):
        singleTXTFilePath = os.path.join(folderOfTXT, oneTXT)
        if singleTXTFilePath.endswith(".txt"):
            with open(singleTXTFilePath, "r") as txtFileContent:
                txtFileContentString = txtFileContent.read()
                if not txtFileContentString.startswith("Error generating text"):
                    txtFileContentString = txtFileContentString.replace("\n", "")
                    dictOfValidTXTs[os.path.basename(singleTXTFilePath)] = txtFileContentString
    
    with open(JSONPath, "w") as jsonFileContent:
        json.dump(dictOfValidTXTs, jsonFileContent, indent=4)
    
if __name__ == "__main__":
    # The directory of TXT files 
    folderOfTXT = "/Users/Jerry/Desktop/LAoilNewspaperTXTOutputCleaned"

    # Where the final storage JSON will be stored
    jsonPath = "/Users/Jerry/Desktop/CS376/FinalProject/storageJSON.json"

    turnTXTFilesIntoJSON(folderOfTXT, jsonPath)