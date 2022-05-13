import re


# Each commit is created as an object with a repr as per below
class Commit:
    def __init__(self, _hash: str, _message: str, _add: int, _rem: int):
        self.hash = _hash
        self.message = _message
        self.add = _add
        self.remove = _rem

    def __repr__(self):
        return f"commit {self.hash}: {self.message} " \
               f"({self.add} additions, {self.remove} deletions)"


# Function that will validate input and return True if all are valid
def validate_information(_user: str, _repo: str, _hash: str,
                         _msg: str, _add: str, _remove: str):
    if len(re.findall(re_user, _user)) == len(_user):
        if len(re.findall(re_repo, _repo)) == len(_repo):
            if re.findall(re_hash, _hash):
                if len(re.findall(re_message, _msg)) == len(_msg):
                    if re.findall(re_calc, _add):
                        if re.findall(re_calc, _remove):
                            return True


# Regex validation expressions
re_user = r"[A-Za-z0-9-]"
re_repo = r"[A-Za-z-_]"
re_hash = r"[A-Fa-f0-9]{40}"
re_message = r"[^\n]"
re_calc = r"[0-9]"
# Regex commit info expression
re_find = re.compile(r",([^\n]+?),(\d+?),(\d+)")

data = input()
data_dict = {}  # {user: {repo: commit objects}}
add_sum = 0  # used for printing repo totals
remove_sum = 0 # used for printing repo totals

while data != "git push":
    # Clean and split apart the data
    clean_data = data.replace("https://github.com/", "").split("/")
    user = clean_data[0]
    repo = clean_data[1]
    hash_ = clean_data[3].split(",")[0]
    message = ""
    add = ""
    remove = ""
    for item in re.finditer(re_find, clean_data[3]):
        message = item[1]
        add = item[2]
        remove = item[3]

    # Run validation function and add to dict as object if True
    if validate_information(user, repo, hash_, message, add, remove):
        # Create object using commit info found by re_find
        commit = Commit(hash_, message, int(add), int(remove))
        if user not in data_dict.keys():
            data_dict[user] = {repo: [commit]}
        else:
            if repo not in data_dict[user]:
                data_dict[user][repo] = [commit]
            else:
                data_dict[user][repo].append(commit)
    data = input()

for user, repo in sorted(data_dict.items()):
    print(f"{user}:")
    for repo_, commits in sorted(repo.items()):
        print(f"  {repo_}:")
        for commit in commits:
            print(f"    {commit}")
            add_sum += commit.add
            remove_sum += commit.remove
        print(f"    Total: {add_sum} additions, {remove_sum} deletions")
        add_sum = 0
        remove_sum = 0
