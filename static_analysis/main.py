import yaml

# Side / Helper Functions

# Given List [] and Input File ""
def find_vulnerability_values_in_dict(l, d):
    for k,v in d.items():
        if isinstance(v, dict):
            find_vulnerability_values_in_dict(l, v)
        else:
            if k is not None:
                if "user" in k:
                    if v is not None and ("root" in v or "admin" in v):
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Hard-coded (username), Admin By Default"
                        temp["found"] = []
                        l.append(temp)
                    elif v is not None:
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Hard-coded (username)"
                        temp["found"] = []
                        l.append(temp)
                if "pass" in k:
                    if v == None or v == "":
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Empty Password"
                        temp["found"] = []
                        l.append(temp)
                    else:
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Hard-coded secret (password)"
                        temp["found"] = []
                        l.append(temp)
                if "ip" in k:
                    if v == "0.0.0.0":
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Unrestricted IP Address"
                        temp["found"] = []
                        l.append(temp)
                if isinstance(v, str):
                    if "http" in v and not "https" in v:
                        temp = {}
                        temp["var"] = k
                        temp["name"] = "Use of HTTP without TLS"
                        temp["found"] = []
                        l.append(temp)

# Given List [] and Input File ""
def find_line_number_of_values(l, f):
    with open(f) as fh:
        line = fh.readline()
        cnt = 1
        while line:
            for i in l:
                if i["var"] in line:
                    i["line"] = cnt
            line = fh.readline()
            cnt += 1

# Main Functions

# Given List [] and Input File ""
def find_vulnerability_values(l, f):
    with open(f) as fh:
        data = yaml.load(fh, Loader=yaml.FullLoader)
        find_vulnerability_values_in_dict(l, data)
    find_line_number_of_values(l, f)

# Given List [] and Input File ""
def find_usage_of_values(l, f):
    last_tag = ""
    with open(f) as fh:
        line = fh.readline()
        cnt = 1
        while line:
            if "name:" in line:
                start_pt = line.find("\"")
                end_pt = line.find("\"", start_pt + 1)  # add one to skip the opening "
                last_tag = line[start_pt + 1: end_pt]
            for i in l:
                if i["var"] in line:
                    found = False
                    for e in i["found"]:
                        if f in e["file"]:
                            e["lines"].append(cnt)
                            e["tags"].append(last_tag)
                            found = True
                            break
                    if not found:
                        temp = {}
                        temp["file"] = f
                        temp["tags"] = []
                        temp["lines"] = []
                        temp["lines"].append(cnt)
                        temp["tags"].append(last_tag)
                        i["found"].append(temp)
            line = fh.readline()
            cnt += 1

# Given List [] and Output File ""
def output_values(l, f):
    with open(f, "w") as fh:
        for i, v in enumerate(l):
            if v["found"]:
                fh.write(f"Security weakness name: {v['name']}\n")
                fh.write(f"Security weakness location: Variable '{v['var']}' in line {v['line']}\n")
                fh.write(f"Security weakness usage:\n")
                for e in v["found"]:
                    fh.write(f"\tfile: {e['file']}\n")
                    for o, p in enumerate(e['lines']):
                        s = e['tags'][o] if e['tags'][o] != '' else str("No Play Name")
                        fh.write(f"\t\tline {str(e['lines'][o]).rjust(3)} | Play name: {s}\n")
                if i < (len(l)-2):
                    fh.write("\n")

def main():
    value_storage = []
    usage_files = []
    usage_files.append("Workshop3.play1.yaml")
    usage_files.append("Workshop3.play2.yaml")

    find_vulnerability_values(value_storage, "Workshop3.values.yaml")

    for file in usage_files:
        find_usage_of_values(value_storage, file)

    output_values(value_storage, "output.md")

if __name__=='__main__':
    main()