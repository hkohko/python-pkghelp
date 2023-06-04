# python-pkghelp
A simple program to show internal dosctrings of external/internal python packages.  

`local` branch provides the barebones. Do `python main.py` in your terminal to use it.  
GUI app is pending.

## USAGE  
**Package/module name currently is case-sensitive, methods aren't**.

Type in the package/module and method as how you would in a python code:  
Example: `str.join`
```  
Package/module name: str.join
join
[('join', 100)]
Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
```
Or type in just the package/module to get a list of available methods:  
Example: `Levenshtein`  
```  
['_Editops', '_Hamming', '_Indel', '_Jaro', '_JaroWinkler', '_Levenshtein', '_Opcodes', '__all__', '__annotations__',   
'__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__',   
'__path__', '__spec__', '__version__', 'apply_edit', 'distance', 'editops', 'hamming', 'inverse', 'jaro', 'jaro_winkler',   
'levenshtein_cpp', 'matching_blocks', 'median', 'median_improve', 'opcodes', 'quickmedian', 'ratio', 'seqratio', 'setmedian',   
'setratio', 'subtract_edit']
```

