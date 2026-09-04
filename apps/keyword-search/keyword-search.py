
import keyword
from sys import argv
from pathlib import PureWindowsPath

def searchKeywordInLine(keyword,line,case=False):
    casedLine = line if case else line.lower()
    casedKeyword = keyword if case else keyword.lower()
    if casedKeyword in casedLine:
        return True
    else:
        False

def searchMultipleKeywordInLine(keyword,line):
    keywords = keyword.split()
    loweredLine = line.lower()
    for word in keywords:
        if word.lower() not in loweredLine:
            return False
    return True
    
def search(keyword,file_path):
    entries = []
    with open(file_path,"r") as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if len(keyword.split()) == 1:
                if searchKeywordInLine(keyword,stripped_line):
                    entries.append(stripped_line)
            else:
                if searchMultipleKeywordInLine(keyword,stripped_line):
                    entries.append(stripped_line)
            
    return entries




if __name__ == "__main__":
    from pathlib import Path
    proj_root = Path(__file__).parents[2]
    datasets_path = proj_root / "datasets"

    dataset = datasets_path / "small-tasks.md"
    keyword = argv[1] if len(argv) > 1 else "Germany" 
    search_entries = search(keyword,dataset)
    for entry in search_entries:
        print(entry)
