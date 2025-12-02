# This file contains the code that I run on DCC to use Mistral's model locally so that I can request more GPUs througoh the Duke Compute Cluster to increase speed.
'''Code attribution: I borrowed from Mistral's HuggingFace documentation and added my own prompt'''
import os, sys, json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "mistralai/Mistral-7B-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto"
)

storageJSONFilePath = "/Users/Jerry/Desktop/CS376/FinalProject/storageJSON.json"

with open(storageJSONFilePath, "r") as dataStorage:
    dataContent = json.load(dataStorage)

for newspaperTitle, newspaperContent in dataContent.items():
    prompt = f"""You are an OCR text cleaning specialist. Your task is to fix OCR errors in historical newspaper text.

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
    {newspaperContent}

    Corrected text: """ 

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(**inputs)

    # Decode output
    outputs = tokenizer.decode(outputs[0])

    cleanedTextFile = newspaperTitle + ".txt"
    with open(cleanedTextFile, "w") as storageTXT:
        storageTXT.write(outputs)

    print(f"Cleaned newspapaer page {newspaperTitle}")

print("Cleaning completed")
