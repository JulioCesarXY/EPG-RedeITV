import json
import requests


def extrair_streams_com_detalhes():
    url = "https://v2.redeitv.com.br/channels?sort=recent"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://v2.redeitv.com.br/",
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            canais_json = response.json()
            lista_canais = []

            for canal in canais_json:
                if canal.get("isActive") and canal.get("hlsUrl"):
                    nome = canal.get("name", "Sem Nome").strip()
                    url_stream = canal.get("hlsUrl", "").strip()

                    logo = canal.get("logoUrl")
                    logo = logo.strip() if logo else ""

                    categoria_obj = canal.get("category")
                    if categoria_obj and isinstance(categoria_obj, dict):
                        estado = categoria_obj.get("name", "Geral").strip()
                    else:
                        estado = "Geral"

                    lista_canais.append(
                        {
                            "name": nome,
                            "url": url_stream,
                            "logo": logo,
                            "estado": estado,
                        }
                    )
            return lista_canais
        return None
    except Exception as e:
        print(f"Erro na extração: {e}")
        return None


def gerar_m3u8_organizado(lista_canais, nome_arquivo="lista_canais.m3u8"):
    if not lista_canais:
        print("Nenhum canal para salvar.")
        return

    canais_por_estado = {}
    for canal in lista_canais:
        est = canal["estado"]
        if est not in canais_por_estado:
            canais_por_estado[est] = []
        canais_por_estado[est].append(canal)

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for estado, lista in canais_por_estado.items():
            for canal in lista:
                f.write(
                    f'#EXTINF:-1 tvg-logo="{canal["logo"]}" group-title="{estado}",{canal["name"]}\n'
                )
                f.write(f'{canal["url"]}\n')
    print(f"Playlist salva com sucesso: {len(lista_canais)} canais.")


if __name__ == "__main__":
    dados = extrair_streams_com_detalhes()
    if dados:
        gerar_m3u8_organizado(dados)
