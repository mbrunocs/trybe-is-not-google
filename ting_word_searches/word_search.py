from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    match = list()
    for file in instance.list:
        ocorrencias = list()
        for idx, string in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in string.lower():
                ocorrencias.append({
                    "linha": idx + 1
                })
        if len(ocorrencias) > 0:
            match.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias,
            })
    return match if len(match) > 0 else []


def search_by_word(word: str, instance: Queue):
    match = list()
    for file in instance.list:
        ocorrencias = list()
        for idx, string in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in string.lower():
                ocorrencias.append({
                    "linha": idx + 1,
                    "conteudo": string,
                })
        if len(ocorrencias) > 0:
            match.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": ocorrencias,
            })
    return match if len(match) > 0 else []
