import json
import csv

def selective_info_from_json_data(data):
    selective_data = []
    for i in data:
        temp = {}
        temp["CVE-ID"] = i["identifiers"]["CVE"]
        temp["DESCRIPTION"] = i["description"]
        temp["SEVERITY"] = i["severity"].upper()
        selective_data.append(temp)
    return selective_data


def analyze_docker_scan(input_file, output_file):
    selective_data = []
    with open(input_file, 'r') as fhandle:
        data = json.load(fhandle)
        selective_data = selective_info_from_json_data(data["vulnerabilities"])

    with open(output_file, 'w', newline='') as fhandle:
        writer = csv.writer(fhandle)
        writer.writerow(["CVE-ID", "DESCRIPTION", "SEVERITY"])
        for i in selective_data:
            cvestring = ' '.join([str(elem) for elem in i["CVE-ID"]])
            writer.writerow([cvestring, i["DESCRIPTION"].replace("\n", ""), i["SEVERITY"]])

if __name__=='__main__':
    input_file = "./scanned_image_output.txt"
    output_file = "./results.csv"
    analyze_docker_scan(input_file, output_file)