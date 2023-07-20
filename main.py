#Read filenames to memory
def read_filenames():
    filenames = []
    with open('filenames.txt') as f:
        for line in f:
            if line.find("(File)") == -1:
                filenames.append(line.strip())
    return filenames

def main():
    filenames = read_filenames()
    TOC_entries = []
    for filename in filenames:
        TOC_entry = ""
        path = "./" + filename
        title = filename.replace(".md", "")
        title = title.replace("_", " ")
        title = title.replace("-", " ")
        title = title.replace("README.", "")
        TOC_entry = "## [" + title + "](" + path + ")\n"
        TOC_entries.append(TOC_entry)
    
    with open('TOC.md', 'w') as f:
        for entry in TOC_entries:
            f.write(entry)
        f.close()
        

if __name__ == '__main__':
    main()