def correct_path(path):
    f = None

    try:
        f = open(path, 'r')
    except:
        try:
            if path.find(chr(92)) != None:
                path.replace(chr(92), chr(47))
                f = open(path, 'r')
            elif path.find(chr(47) != None):
                path.replace(chr(47), chr(92))
                f = open(path, 'r')
        except:
            try:
                f = open(chr(92) + path, 'r')
            except:
                try:
                    f = open(chr(47) + path, 'r')
                except:
                    print("Errore caricamento file " + "'" + path + "'.")
                    exit()
                    #return None

    f.close()
    return path

def load_textFile(path):
    f = None

    try:
        f = open(correct_path(path), 'r')
    except:
        print("Errore caricamento file " + "'" + path + "'.")
        exit()
        #return None

    b = f.read()
    f.close()
    return b

#s = load_textFile("standard_map.txt")

#pos = instr(0, s, "@name = ") + len("@name = ")

#print(s[pos:instr(pos, s, ";")])

