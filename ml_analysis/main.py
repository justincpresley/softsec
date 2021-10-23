import os
import subprocess
import json

def bandit_analyze_file(path, filelist):
    command = ["bandit","-f","json",path]
    output = subprocess.run(command, capture_output=True).stdout
    output = json.loads(output.decode("utf-8"))

    temp = {}
    temp["FILE"] = path
    temp["ALERTS"] = []
    for i in output["results"]:
        alert = {}
        alert["SEVERITY"] = i["issue_severity"]
        alert["CONFIDENCE"] = i["issue_confidence"]
        alert["NAME"] = i["test_name"]
        alert["LINE_NO"] = i["line_number"]
        if alert["CONFIDENCE"] != "LOW" and alert["SEVERITY"] != "LOW":
            temp["ALERTS"].append(alert)

    if temp["ALERTS"]:
        filelist.append(temp)


def bandit_analyze_directory(directory, output):
    files = os.listdir(directory)
    concerned_files = []
    for file in files:
        bandit_analyze_file(directory + "/" + file, concerned_files)

    with open(output, 'w') as fhandle:
        json.dump(concerned_files, fhandle, indent=4)
        fhandle.write("\n")

if __name__=='__main__':
    directory = "./ML-CODE"
    json_output_file = "./json_dump.txt"
    bandit_analyze_directory(directory, json_output_file)