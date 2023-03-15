import polib
import sys

if __name__=='__main__':
    file=sys.argv[1]

    mo_file=polib.mofile(file)
    mo_file.save_as_pofile(file.replace('.mo','.po'))