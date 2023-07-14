import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return []

    try:
        file = open(path_file, mode="r")
        file_contents = file.read().split('\n')
        file.close()
        return file_contents
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []
