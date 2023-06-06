# Vypracované zadání 
viz: https://github.com/czech-radio/assignment
## Instalace
Pro instalaci je potřeba vytvořit virtuální prostředí a poté ho spustit
```bash
py -3.10 -m venv .venv
```
```bash
.\.venv\Scripts\activate
```
Nejdříve je potřeba aktualizovat pip a nainstalovat knihovny potřebné pro běh skriptu
```bash
python -m pip install --upgrade pip
```
```bash
python -m pip install -r requirements.txt
```
Poté je možné build nainstalovat
```bash
pip install .
```
## Použití programu
Pokud máte program nainstalovaný je možné ho otestovat pomocí 
```bash
sort_data -v
sort_data -h
```
Pro spuštění skriptu je třeba zadat argumenty s umístěním input a kam chcete umístit output, defaultně je to následovně:
```bash
sort_data -i ./source -o ./target
```
Tímto se nám zobrazily změny, které skript provede, pro propsání změn je ovšem potřeba přiložit argument write
```bash
sort_data -i ./source -o ./target -w
```
Skript automaticky přesune json soubory, které nesplňují předpoklady pro zpracování (liší se název s datumem uvnitř) do složky `./NEED_CHANGE` pokud i tyto soubory chcete opravit a pracovat snimi je třeba je nejdříve opravit, to buď ručně, nebo využít skriptu `edit_prepared_data.py`, ten opraví atribut datum v json souboru a zpátky ho přesune do složky `./source`. 
Skript je možné spustit následovně:
```bash
python edit_prepared_data.py
```
Poté je nutné znovu opakovat spuštění skriptu
```bash
sort_data -i ./source -o ./target -w
```
Bez instalace je možné skript využívat stejně pomocí + argumenty 
```bash
python sort_data.py 
```
Funkcionalita programu byla testována primárně na macOS.

## Část zpracování dat
V poslední řadě jsou připojeny soubory `p3.xlsx` a skript `process_data.py`. Skript slouží pro vytvoření datasetu, který je následně exportován do .xlsx souboru. V .xlsx jsou poté manuálně data upravena pomocí kontingenční tabulky a vyobrazena na požadovaných grafech.

