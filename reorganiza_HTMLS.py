import os
import shutil

PASTA_RAIZ = r"C:\Users\Usuário\Documents\Projetos Dev\EmailMarketing\JustALittleData\clientes\Cencosud\Giga"

EXTENSOES_HTML = {".html", ".htm"}


def gerar_nome_unico(destino):
    """
    Se já existir um arquivo com o mesmo nome,
    adiciona _1, _2, _3...
    """
    if not os.path.exists(destino):
        return destino

    pasta = os.path.dirname(destino)
    nome, ext = os.path.splitext(os.path.basename(destino))

    contador = 1

    while True:
        novo_nome = f"{nome}_{contador}{ext}"
        novo_caminho = os.path.join(pasta, novo_nome)

        if not os.path.exists(novo_caminho):
            return novo_caminho

        contador += 1


def mover_htmls_para_raiz():
    for raiz, dirs, arquivos in os.walk(PASTA_RAIZ, topdown=False):

        if raiz == PASTA_RAIZ:
            continue

        for arquivo in arquivos:

            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao in EXTENSOES_HTML:

                origem = os.path.join(raiz, arquivo)
                destino = os.path.join(PASTA_RAIZ, arquivo)

                destino = gerar_nome_unico(destino)

                try:
                    shutil.move(origem, destino)
                    print(f"Movido: {origem}")
                    print(f"   -> {destino}")

                except Exception as e:
                    print(f"Erro: {origem}")
                    print(e)


def remover_pastas_vazias():
    for raiz, dirs, arquivos in os.walk(PASTA_RAIZ, topdown=False):

        if raiz == PASTA_RAIZ:
            continue

        try:
            if not os.listdir(raiz):
                os.rmdir(raiz)
                print(f"Pasta vazia removida: {raiz}")

        except Exception as e:
            print(f"Erro ao remover {raiz}: {e}")


if __name__ == "__main__":

    print("Movendo HTMLs...")
    mover_htmls_para_raiz()

    print("\nRemovendo pastas vazias...")
    remover_pastas_vazias()

    print("\nConcluído!")