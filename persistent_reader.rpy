init python:
    def pretty(d, indent=0):
        result = ""
        for key, value in sorted(d.iteritems()):
            result += '\t' * indent + str(key) + '\n'
            if  str(type(value)) in ["<type 'dict'>", "<class 'renpy.python.RevertableDict'>"]:
                result += pretty(value, indent+1)
            elif  hasattr(value, "__dict__"):
                result += pretty(value.__dict__, indent+1)
            else:
                result += '\t' * (indent+1) + `type(value)` + str(value) + '\n'
        return result
    for fn in ["persistent","persistent.old"]:
        with file(fn, "rb") as f:
            with file(fn+".out", "wb") as ff:
                ff.write(pretty(renpy.persistent.loads(f.read().decode("zlib")).__dict__))
