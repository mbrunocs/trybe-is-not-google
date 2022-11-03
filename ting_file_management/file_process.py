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


def remove(instance: Queue):
    if instance.__len__() == 0: sys.stdout.write('Não há elementos\n')
    else:
        removed = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {removed} removido com sucesso\n")


def file_metadata(instance: Queue, position: int):
    if position < 0 or position >= len(instance):
        sys.stderr.write(f"Posição inválida")
    else:
        file = instance.search(position)
        sys.stdout.write(f"{file}")
