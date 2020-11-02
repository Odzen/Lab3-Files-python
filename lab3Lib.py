import sys
import json
import yaml
import time

def parsingLibrary():

    outputFile = open("timetableLibrery.yaml", "w", encoding="utf-8")

    with open('timetable.json', encoding='utf-8') as fh:
              data = json.load(fh)
    outputFile.write(yaml.dump(data, allow_unicode=True))

start_time = time.time()
parsingLibrary()
print("Library %s seconds ---" % (time.time() - start_time))