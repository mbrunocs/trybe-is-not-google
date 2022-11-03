import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, encoding="utf-8") as file:
            file_reader = file.read()
        return file_reader.split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
