import time
import inspect
from Levenshtein import ratio
import builtins


def return_methods(pkg): 
    try:
        try:
            current_pkg = __import__(pkg)
        except ModuleNotFoundError:
            current_pkg = getattr(builtins, pkg)
    except AttributeError:
        print("Package unavailable. Perhaps you're in a virtual environment?")
        userinput()
    methods = (inspect.getmembers(current_pkg))
    names = [module for module, _ in methods]
    return names


def fsearch(var, names):
    cutoff = 0.55 #tentative
    candidates = {}
    for i in names:
        score = ratio(var, i)
        if score > cutoff:
            candidates[i] = int((score*100))
    try:
        return max(candidates, key=candidates.get), sorted(candidates.items(), key=lambda x:x[1], reverse=True)
    except ValueError:
        pass


def docstring(pkg, method):
    try:
        pkg = __import__(pkg)
        print(getattr(pkg, method).__doc__)
        userinput()
    except ModuleNotFoundError:
        x = getattr(builtins, pkg)
        print(getattr(x, method).__doc__)
        userinput()


def main(pkg, method=''):
    names = return_methods(pkg)
    try:
        match, closest = fsearch(method, names)
    except TypeError:
        print(names)
        userinput()
    try:
        print(match)
        print(closest[0:5])
        docstring(pkg, match)
    except UnboundLocalError:
        pass


def userinput():
    try:
        entry = input("Package/module name: ")
    except KeyboardInterrupt:
        print('Exiting...')
        time.sleep(1)
        exit()
    try:
        pkg, method = entry.strip().split('.')
        main(pkg, method)
    except ValueError:
        main(entry)


userinput()