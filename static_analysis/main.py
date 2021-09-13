import yaml

def add_values(list, d):
    for k,v in d.items():
        if isinstance(v, dict):
            add_values(list, v)
        else:
            print(k)

def main():
    lists_of_values = []
    with open('values.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        add_values(lists_of_values, data)

    for i in lists_of_values:
        print(i)

if __name__=='__main__':
    main()