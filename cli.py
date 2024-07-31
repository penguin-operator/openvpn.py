argtype = str | int | float | bool

def matchtype(arg: str) -> argtype:
    if arg == "true":
        return True
    elif arg == "false":
        return False
    try:
        return int(arg)
    except:
        try:
            return float(arg)
        except:
            return arg

def argparse(*args: str) -> tuple[list[argtype], dict[str, argtype]]:
    a, kv, p = list(), dict(), ""
    for arg in args:
        if arg.startswith("-"):
            k, *v = arg.split('=')
            if v:
                kv[k[1:]] = matchtype(v[0])
            else:
                kv[k[1:]] = True
                p = arg
        elif p:
            kv[p[1:]] = matchtype(arg)
            p = ""
        else:
            a.append(arg)
    return a, kv
