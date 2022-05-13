class Website:
    storage = []

    @staticmethod
    def collect_data(_host: str, _domain: str, _queries: list):
        Website.storage.append([_host, _domain, _queries])


data = input()

while data != "end":
    hostname = data.split(" | ")[0]
    domain = data.split(" | ")[1]
    try:
        queries = data.split(" | ")[2].split(",")
    except IndexError:
        queries = []
    Website.collect_data(hostname, domain, queries)
    data = input()

for item in Website.storage:
    if len(item[2]) != 0:
        print(f"https://www.{item[0]}.{item[1]}/query?=", end='')
        for i in range(len(item[2])):
            if i != len(item[2]) - 1:
                print(f"[{item[2][i]}]&", end='')
            else:
                print(f"[{item[2][i]}]")
    else:
        print(f"https://www.{item[0]}.{item[1]}")
