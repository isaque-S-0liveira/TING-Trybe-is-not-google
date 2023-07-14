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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
