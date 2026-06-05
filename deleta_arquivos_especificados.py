import os
import shutil

# CAMINHO DA PASTA PRINCIPAL
PASTA_RAIZ = r"C:xxxxx"

# Extensões de arquivos que quero remover:
EXTENSOES_ARQUIVOS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp",
    ".svg",
    ".tiff",
    ".ico",
    ".csv",
    ".xlsx",
    ".pdf",
    ".txt"
}

# Extensões HTML
EXTENSOES_HTML = {
    ".html",
    ".htm"
}


def remover_arquivos():
    for raiz, dirs, arquivos in os.walk(PASTA_RAIZ):
        for arquivo in arquivos:
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao in EXTENSOES_ARQUIVOS:
                caminho_arquivo = os.path.join(raiz, arquivo)

                try:
                    os.remove(caminho_arquivo)
                    print(f"Arquivo removido: {caminho_arquivo}")
                except Exception as e:
                    print(f"Erro ao remover {caminho_arquivo}: {e}")


def pasta_tem_html(caminho):
    for raiz, dirs, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao in EXTENSOES_HTML:
                return True

    return False


def remover_pastas_sem_html():
    # Percorre de baixo para cima
    for raiz, dirs, arquivos in os.walk(PASTA_RAIZ, topdown=False):

        if raiz == PASTA_RAIZ:
            continue

        if not pasta_tem_html(raiz):
            try:
                shutil.rmtree(raiz)
                print(f"Pasta removida: {raiz}")
            except Exception as e:
                print(f"Erro ao remover pasta {raiz}: {e}")


if __name__ == "__main__":
    print("Removendo arquivos...")
    remover_arquivos()

    print("\nRemovendo pastas sem HTML...")
    remover_pastas_sem_html()

    print("\nProcesso concluído!")