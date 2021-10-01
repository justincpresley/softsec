import os

privacy_list = [
    "read_calendar","write_calendar","camera","read_contacts","write_contacts","get_accounts","access_fine_location",
    "access_coarse_location","record_audio","read_phone_state","read_phone_numbers","call_phone","answer_phone_calls",
    "read_call_log","write_call_log","process_outgoing_calls","add_voicemail","use_sip","body_sensors","send_sms",
    "receive_sms","read_sms","receive_wap_push","receive_mms","read_external_storage","write_external_storage"
]

def detectDangerousJavaLeaks():
    pass
def getJavaFilesHelper(subdir, l):
    for entry in os.scandir(subdir):
        if entry.is_file():
            if entry.name.endswith(".java"):
                temp = {}
                temp["path"] = entry.path
                temp["lines"] = sum(1 for _ in open(entry.path))
                l.append(temp)
        else:
            getJavaFilesHelper(entry.path,l)
def getJavaFiles(subdir):
    res = []
    getJavaFilesHelper(subdir, res)
    return res

def detectDangerousManifestLeaks():
    pass
def getManifestHelper(subdir, l):
    for entry in os.scandir(subdir):
        if entry.is_file():
            if entry.name == "AndroidManifest.xml":
                temp = {}
                temp["path"] = entry.path
                temp["lines"] = sum(1 for _ in open(entry.path))
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

    print(main_list)
    print(privacy_list)