# 📺 EPG-RedeITV

![GitHub IPTV Automation](https://img.shields.io/badge/IPTV-Automation-blue?style=for-the-badge&logo=github-actions)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge=mit)

Repositório voltado para a extração automatizada de streams públicos da RedeITV. O script coleta os dados atualizados da API, organiza os canais por **Estados (Categorias)**, anexa as respectivas **Logos** e gera uma playlist estruturada no formato `.m3u8` ideal para players de IPTV.

Toda a atualização é feita de forma 100% dinâmica e diária através do **GitHub Actions**.

---

## 🚀 Como Usar a Playlist

Você não precisa rodar nada localmente para usar os canais. Basta copiar o link fixo abaixo e colar no seu player favorito (VLC, IPTV Smarters, Perfect Player, SS IPTV, etc.):

```text
https://raw.githubusercontent.com/JulioCesarXY/EPG-RedeITV/main/lista_canais.m3u8
```
