from bs4 import BeautifulSoup


def epub_toc_to_md(html_file):
    # Abre o arquivo HTML e cria um objeto BeautifulSoup
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Encontra a tabela de conteúdos no HTML
    toc = soup.find("div", {"epub:type": "toc"})

    # Inicializa a string da tabela de conteúdos em Markdown
    md_toc = "# Table of Contents\n"

    # Itera sobre todos os elementos da tabela de conteúdos
    for element in toc.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        # Extrai o nível do cabeçalho
        level = int(element.name[1])

        # Extrai o texto do cabeçalho
        text = element.get_text(strip=True)

        # Adiciona o cabeçalho à tabela de conteúdos em Markdown
        md_toc += "{} {}\n".format("#" * level, text)

    return md_toc


# Exemplo de uso
print(epub_toc_to_md("toc.html"))
