from urllib.parse import parse_qs

def qsGetStrByName(qs, var_name):
    res = ''
    x = parse_qs(qs[2:])
    if (var_name in x):
        res = x[var_name][0]
    return res