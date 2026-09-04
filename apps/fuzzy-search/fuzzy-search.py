from sys import argv


def fuzzyMatchFilename(keyword, filename):
    """
    Match an abbreviated pattern against a filename.
    Example: keyword "g.d" may match "germany file.md", "german.md"
    """
    raise NotImplementedError


def search(keyword, directory_path):
    entries = []
    with open(file_path, "r") as f:
        for idx, line in enumerate(f):
            stripped_line = line.strip()
            if fuzzyMatchInLine(keyword, stripped_line, threshold):
                entries.append(stripped_line)
    return entries


if __name__ == "__main__":
    from pathlib import Path

    proj_root = Path(__file__).parents[2]
    datasets_path = proj_root / "datasets"

    keyword = argv[1] if len(argv) > 1 else "g.d"
    search_entries = search(keyword, datasets_path)
    for entry in search_entries:
        print(entry)
