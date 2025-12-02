'''This file contains calls to Duke's API to perform data cleaning.
- "apiCall" function: borrowed the function frameowkr from CS 101 Fall 2025 Assignment 5; I modified details (such as data types, method parameters, etc.) to fit the need of my use case.
- "obtainFilePathUncleaned" funcrion: written completely by me.
- "createCleanedFilesInFolder" function: written completely by me with Claude Sonnet 3.5 in debugging.
- "returnListOfFilesProcessed" function: written by me.
- Main function block: by me'''

import urllib.request, json, os, time
from pathlib import Path

def apiCall(text, api_key):
    """
    Given a string containing one English word, your MyGPTBuilder API key, and (optionally)
    a list of previously-generated hints for the given word, return a new hint obtained
    by querying Duke's free Mistral model.

    :param text:
    :param api_key:
    """

    # Using in-context learning and few-shot prompting to provide better results.
    try:
        url = 'https://litellm.oit.duke.edu/v1/chat/completions'
        payload = {
            'model': 'Mistral on-site', # Could use "Mistral on-site" or "gpt-5-chat"
            'messages': [ {
                'role': 'user',
                'content': f"""You are an OCR text cleaning specialist. Your task is to fix OCR errors in historical newspaper text.

Rules:
- Fix only OCR errors and spelling mistakes
- Do not add or remove words
- Preserve formatting
- Output ONLY the corrected text with NO preamble, explanations, or meta-commentary

For two examples, when you have an OCR-ed text:
"Mondal, Nouenber 1911: Loc Angeles",

You should clean it to be:
"Monday, November 1911: Los Angeles"

Or, when you have an OCR-ed text:
"Robcr walked*& lovards th north",

You should clean it to be:
"Robert walked towards the north".

The input text is:
{text}

Corrected text: """ }
            ],
            "temperature": 0.2
        }

        payload = json.dumps(payload).encode('utf-8')
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + api_key
        }
        
        req = urllib.request.Request(url, data=payload, headers=headers, method='POST')

        print("Calling API")
        with urllib.request.urlopen(req) as response:
            response = json.loads(response.read().decode('utf-8'))

        # source: Simple hint-extraction from Claude below

        # Extract and clean the hint
        print(f"Finished calling API")

        returnText = response['choices'][0]['message']['content'].strip()

        return returnText
    
    except Exception as e:
        return f"Error generating text: {str(e)}"
    

def obtainFilePathUncleaned(uncleanedTXTFolder):
    listOfTXTFilePaths = []
    for file in os.listdir(uncleanedTXTFolder):
        if file.endswith(".txt"):
            listOfTXTFilePaths.append(os.path.join(uncleanedTXTFolder, file))
    
    listOfTXTFilePaths = sorted(listOfTXTFilePaths)

    return listOfTXTFilePaths

def createCleanedFilesInFolder(listOfUncleanedTXTFilePaths, cleanedTXTFolderPath, apiKey, docOfCleanedTXTFilePaths=None):
    fileProgressCounter = 0
    failedFiles = []

    #Return a list of files that have already been cleaned
    listOfCleanedFiles = returnListOfFilesProcessed(docOfCleanedTXTFilePaths)

    for uncleanedFile in listOfUncleanedTXTFilePaths:
        fileName = os.path.basename(uncleanedFile)  #Getting the name of the newspaper without the full file path
        print(f"\n\n====Processing file {fileProgressCounter + 1}/{len(listOfUncleanedTXTFilePaths)}: {fileName}====")
        
        if fileName in listOfCleanedFiles:
            print("File already cleaned")
            fileProgressCounter += 1
            continue

        try:
            with open(uncleanedFile, "r") as uncleanedFileContent:
                uncleanedText = uncleanedFileContent.read()

            if fileProgressCounter > 0: #Add breaks between API call to prevent errors
                delayTime = 2
                print(f"Waiting {delayTime}s before API call")
                time.sleep(delayTime)
            
            print(f"Started API call to clean {fileName}")
            cleanedText = apiCall(uncleanedText, apiKey)

            if "Error generating text" in cleanedText or "HTTP Error" in cleanedText:
                print(f"API call failed for {fileName}")
                print(f"Error message: {cleanedText}")
                #skipping the file that encountered an error and not updating the txt that keeps track of all the processed files, so that, next time the function runs, it will still find the file that hit an error and try to process it.
                continue
                # return "API call failed midway through processing"
            
            cleanedFileName = os.path.join(cleanedTXTFolderPath, fileName)
            print(f"About to store cleaned file at: {cleanedFileName}")
            with open(cleanedFileName, "w", encoding="utf-8") as newFile:
                newFile.write(cleanedText)
            
            print(f"Cleaned file: {uncleanedFile.split("/")[-1]}")
            print(f"Stored cleaned file at {cleanedFileName}")
            
            #This is to keep track of all the files that have been processed, in case the function breaks or throws a fit somewhere during the cleaning process.
            with open(docOfCleanedTXTFilePaths, "a") as updateFile:
                updateFile.write(fileName+ "\n")

            fileProgressCounter += 1

        except IOError as e:
            print(F"IO error with {fileName}: {str(e)}")
            failedFiles.append(uncleanedFile)
        
        except Exception as e:
            print(f"Error with {fileName}: {str(e)}")
            failedFiles.append(uncleanedFile)
            
    if failedFiles:
        print(f"\n\n{len(failedFiles)} failed to process.")
        return failedFiles
    else:
        print(f"All files processed successfully.")
        return failedFiles

def returnListOfFilesProcessed(docOfCleanedTXTFilePaths):
    #Helper function to return a list of file paths that have already been cleaned
    with open(docOfCleanedTXTFilePaths, "r") as file:
        cleanedFiles = [filePath.strip() for filePath in file]
    
    return cleanedFiles

if __name__=='__main__':
    # Replace the string in the next line with your actual API key, obtained
    #   by logging into the AI Dashboard (https://dashboard.ai.duke.edu/),
    #   navigating to the AI Gateway tab, then clicking "Create Api Key".
    uncleanedTXTFolderPath = "/Users/Jerry/Desktop/LAoilNewspaperTXTOutputUncleaned"
    cleanedTXTFolderPath = "/Users/Jerry/Desktop/LAoilNewspaperTXTOutputCleaned"

    docOfCleanedTXTFilePaths = "/Users/Jerry/Desktop/DHproj-reading/LAOilProject/LAOil/textCleaningAndOperations/filesCleaned.txt"

    # This part takes my API key from a secure file
    with open("/Users/Jerry/Desktop/DHproj-reading/LAOilProject/LAOil/textCleaningAndOperations/apiKey.txt", "r") as keyFile:
        apiKey = keyFile.read().strip()

    listUncleanedFiles = obtainFilePathUncleaned(uncleanedTXTFolderPath)
    
    failedFiles = createCleanedFilesInFolder(listUncleanedFiles, cleanedTXTFolderPath, apiKey, docOfCleanedTXTFilePaths=docOfCleanedTXTFilePaths)
    
    if failedFiles:
        print(failedFiles)