import yaml

def add_values(l, d):
    for k,v in d.items():
        if isinstance(v, dict):
            add_values(l, v)
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

def detail_values(l, file):
    with open(file) as f:
        line = f.readline()
        cnt = 1
        while line:
            for i in l:
                if i["var"] in line:
                    i["line"] = cnt
            line = f.readline()
            cnt += 1

def find_vars(l, file):
    with open(file) as f:
        line = f.readline()
        cnt = 1
        while line:
            for i in l:
                if i["var"] in line:
                    found = False
                    for e in i["found"]:
                        if file in e["file"]:
                            e["lines"].append(cnt)
                            found = True
                            break
                    if not found:
                        temp = {}
                        temp["file"] = file
                        temp["lines"] = []
                        temp["lines"].append(cnt)
                        i["found"].append(temp)
            line = f.readline()
            cnt += 1

def output_vars(l, file):
    with open(file, "w") as f:
        for i, v in enumerate(l):
            if v["found"]:
                f.write(f"Security weakness name: {v['name']}\n")
                f.write(f"Security weakness location: Variable '{v['var']}' in line {v['line']}\n")
                f.write(f"Security weakness usage:\n")
                for e in v["found"]:
                    f.write(f"\tfile {e['file']}, lines {e['lines']}\n")
                if i < (len(l)-2):
                    f.write("\n")

def main():
    lists_of_values = []
    with open('Workshop3.values.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        add_values(lists_of_values, data)

    detail_values(lists_of_values, "Workshop3.values.yaml")

    find_vars(lists_of_values, "Workshop3.play1.yaml")
    find_vars(lists_of_values, "Workshop3.play2.yaml")

    output_vars(lists_of_values, "output.md")

if __name__=='__main__':
    main()