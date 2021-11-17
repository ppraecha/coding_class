import json


def save_dict(target_dict, target_file):
    with open(target_file, "w") as f:
        json.dump(target_dict, f)
    f.close()


def load_dict(target_file):
    with open(target_file, "r") as f:
        return json.load(f)


save_path = "./file_storage/file2.json"
dict1 = {"Country": "Laos"}
save_dict(dict1, save_path)
dict2 = load_dict(save_path)
print(dict2)
