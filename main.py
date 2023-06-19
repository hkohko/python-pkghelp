import time
import inspect
from Levenshtein import ratio
import builtins
from typing import List, Tuple, Optional, Dict


def return_methods(pkg: str) -> List[str]: 
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


def fsearch(var: str, names: List[str]) -> Tuple[None, None] | Tuple[str, Optional[List[Tuple[str, int]]]]:
    cutoff: float = 0.55 #tentative
    candidates: Dict = {}

    for i in names:
        score: float = ratio(var, i)
        if score > cutoff:
            candidates[i] = int((score*100))

    candidates_sorted = sorted(candidates.items(), key=lambda x:x[1], reverse=True)

    if candidates and candidates_sorted:
        return max(candidates, key=lambda x:candidates[x]), candidates_sorted
    else:
        return None, None


def docstring(pkg, method = '') -> None:
    try:
        pkg = __import__(pkg) #type: ignore
        print(getattr(pkg, method).__doc__)
        userinput()
    except ModuleNotFoundError:
        x = getattr(builtins, pkg)
        print(getattr(x, method).__doc__)
        userinput()


def main(pkg: str, method:str ='') -> None:
    names: List[str] = return_methods(pkg)
    if fsearch(method, names) == None: 
        print(names)
        userinput()
    else:
        matches, closest = fsearch(method, names)
        if matches is not None and closest is not None:
            print(matches)
            print(closest[0:5])
            docstring(pkg, matches)
        elif matches is None and closest is None:
            print(names)
            userinput()
        else:
            print('')
        

def userinput() -> None:
    try:
        print("Press Ctrl+C to exit")
        entry: str = input("Package/module name: ")
    except KeyboardInterrupt:
        print('Exiting...')
        time.sleep(1)
        exit()
    try:
        pkg:str
        method:str
        pkg, method = entry.strip().split('.')
        main(pkg, method)
    except ValueError:
        main(entry)

if __name__ == "__main__":
    userinput()