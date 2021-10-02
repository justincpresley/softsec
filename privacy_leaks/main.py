import os

privacy_list = [
    "read_calendar","write_calendar","camera","read_contacts","write_contacts","get_accounts","access_fine_location",
    "access_coarse_location","record_audio","read_phone_state","read_phone_numbers","call_phone","answer_phone_calls",
    "read_call_log","write_call_log","process_outgoing_calls","add_voicemail","use_sip","body_sensors","send_sms",
    "receive_sms","read_sms","receive_wap_push","receive_mms","read_external_storage","write_external_storage"
]

def makeCVS(ml, fname):
    with open(fname, "w") as fhandle:
        for subdir in ml:
            for manifest in subdir["manifests"]:
                for manifestleak in manifest["leaks"]:
                    temp = subdir["subdir"] + "," + manifest["path"] + "," + str(manifest["lines"]) + "," + manifestleak + "\n"
                    fhandle.write(temp)
            for java in subdir["javas"]:
                for javaleak in java["leaks"]:
                    temp = subdir["subdir"] + "," + java["path"] + "," + str(java["lines"]) + "," + javaleak + "\n"
                    fhandle.write(temp)

def detectDangerousJavaLeaks(path):
    res = []
    with open(path, "r") as fhandle:
        for leak in privacy_list:
            for aline in fhandle:
                temp = "Manifest.permission." + leak.upper()
                if temp in aline:
                    res.append(leak)
                    break
    return res
def getJavaFilesHelper(subdir, l):
    for entry in os.scandir(subdir):
        if entry.is_file():
            if entry.name.endswith(".java"):
                temp = {}
                temp["path"] = entry.path
                temp["lines"] = sum(1 for _ in open(entry.path))
                temp["leaks"] = detectDangerousJavaLeaks(entry.path)
                if temp["leaks"]:
                    l.append(temp)
        else:
            getJavaFilesHelper(entry.path,l)
def getJavaFiles(subdir):
    res = []
    getJavaFilesHelper(subdir, res)
    return res

def detectDangerousManifestLeaks(path):
    res = []
    with open(path, "r") as fhandle:
        for leak in privacy_list:
            for aline in fhandle:
                temp = "android.permission." + leak.upper()
                if temp in aline:
                    res.append(leak)
                    break
    return res
def getManifestHelper(subdir, l):
    for entry in os.scandir(subdir):
        if entry.is_file():
            if entry.name == "AndroidManifest.xml":
                temp = {}
                temp["path"] = entry.path
                temp["lines"] = sum(1 for _ in open(entry.path))
                temp["leaks"] = detectDangerousManifestLeaks(entry.path)
                if temp["leaks"]:
                    l.append(temp)
        else:
            getManifestHelper(entry.path,l)
def getManifest(subdir):
    res = []
    getManifestHelper(subdir, res)
    return (res if res else None)

if __name__ == "__main__":
    main_list = []
    main_dir = "./FARMING_ANDROID_REPOS"
    csv_name = "Workshop#5.Output.csv"

    print("Please wait while we process all these repositories.")
    for entry in os.scandir(main_dir):
        manifestPath = getManifest(entry)
        if manifestPath is not None:
            sub_list = {}
            sub_list["subdir"] = entry.name
            sub_list["manifests"] = manifestPath
            sub_list["javas"] = getJavaFiles(entry)
            main_list.append(sub_list)
    print("Done processing all the repositories.")

    makeCVS(main_list, csv_name)

    print(f"Wrote privacy leak information in {csv_name}.")


