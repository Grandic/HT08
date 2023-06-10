# файл dicts.py

data = {"vcs": "mercurial", "bomg": "shoot", "petka": "vasilii_ivanovi4", "doroga": "v_nebo"}


def get_val(collection, key, default='git'):
    if len(collection) > 0:
        for k, v in collection.items():
            if k == key:
                return v
    return default





print(get_val({}, "petka",  "git"))