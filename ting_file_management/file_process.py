import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue

def process(path_file, instance: Queue):
    data = txt_importer(path_file)
    new_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }
    if not new_file in instance.list:
        instance.enqueue(new_file)
        sys.stdout.write(f'{new_file}')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
