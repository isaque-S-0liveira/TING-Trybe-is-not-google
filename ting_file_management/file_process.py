import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for i in range(len(instance._data)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    text_list = txt_importer(path_file)
    dic = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text_list),
        "linhas_do_arquivo": text_list,
    }
    instance.enqueue(dic)
    print(dic)
    return dic


def remove(instance: Queue):
    name_arq = instance.dequeue()
    if name_arq is not None:
        print(f"Arquivo {name_arq['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance: Queue, position):
    try:
        inf = instance.search(position)
        print(inf)
        return inf
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return None
