ARTICLES = ["da", "de", "do", "das", "dos"]

def generate_name(name):
    parts = name.split()
    if len(parts) == 1:
        return name.upper()
    elif len(parts) == 2:
            last_name = parts[1]
            name = parts[0]
            return f"{name} {last_name}".upper()
    else:
        name = parts[0]
        mid_name = parts[1:-1]
        last_name = parts[-1]
    return f"{name} {' '.join(generate_mid_names(mid_name))} {last_name}"


def generate_mid_names(mid_name):
    return ['{}'.format(mid_names[:1]) if mid_names not in ARTICLES else mid_names for mid_names in mid_name]

