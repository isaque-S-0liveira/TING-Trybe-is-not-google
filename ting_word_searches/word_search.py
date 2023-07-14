from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []
    for i in range(len(instance._data)):
        word_occurrences = []
        for index, line in enumerate(instance.search(i)["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                word_occurrences.append({"linha": index + 1})
        if word_occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(i)["nome_do_arquivo"],
                    "ocorrencias": word_occurrences,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
