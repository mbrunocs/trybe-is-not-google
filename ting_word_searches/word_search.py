import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    match = list()
    model = {
        "palavra": word,
        "arquivo": '',
        "ocorrencias": list(),
    }
    for file in instance.list:
        model["arquivo"] = file["nome_do_arquivo"]
        for idx, string in enumerate(file["linhas_do_arquivo"]):
            if string.lower() in word.lower():
                model["ocorrencias"].append({
                    "linha": idx + 1
                })
        if len(model["ocorrencias"]) > 0:
            match.append(model) 
            model["ocorrencias"] = list()
    return match if len(match) > 0 else []


def search_by_word(word: str, instance: Queue):
    match = list()
    model = {
        "palavra": word,
        "arquivo": '',
        "ocorrencias": list(),
    }
    for file in instance.list:
        model["arquivo"] = file["nome_do_arquivo"]
        for idx, string in enumerate(file["linhas_do_arquivo"]):
            if string.lower() in word.lower():
                model["ocorrencias"].append({
                    "linha": idx + 1,
                    "conteudo": string,
                })
        if len(model["ocorrencias"]) > 0:
            match.append(model) 
            model["ocorrencias"] = list()
    return match if len(match) > 0 else []
