# Harfia Rush 🦊⭐ — Arabisch leren door écht te spelen

**Speel nu:** https://muwattah.github.io/Game/ (na activeren van GitHub Pages)

Een echt 3-banen-renspel. Ren met een vosje, wissel van baan, spring over blokken, pak sterren en kies onderweg de juiste Arabische letter, het juiste woord of cijfer. Het spel werkt in een browser, ook op telefoon of tablet.

## Kennisniveaus — geen leeftijden
- **🐣 Ik begin net**: vier werelden, de 28 Arabische letters.
- **🦊 Ik herken al iets**: twaalf woorden met plaatjes, tien Arabische cijfers en negen combinaties met korte klinkertekens.
- **🚀 Ik lees al wat**: zes dagelijkse uitdrukkingen en veertien letters in de beginvorm in woorden.

**Totaal: 79 levels, 9 werelden.** Een level bevat vijf juiste poorten. Daarna verdien je een beloning en speel je de volgende baan vrij. De opdracht is steeds kindvriendelijk: bijvoorbeeld *Zoek deze letter!* in plaats van termen als *foneem* of *klank*.

## Besturing
**Gsm/tablet:** gebruik de knoppen of veeg links, rechts, omhoog (springen), omlaag (bukken). Je kunt ook een baan aantikken. **Computer:** pijltjes, WASD en spatie. **🔊:** luister opnieuw. **⏸️:** pauze.

## Installatie en GitHub Pages
Alles wat het spel nodig heeft staat rechtstreeks in **`index.html`** — inclusief Canvas-renspel, grafische weergave, alle letters en woorden en spelcode. Je hoeft niets te installeren en er is geen build nodig.

GitHub → repository **Game** → Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save. Wacht tot de publicatie gereed is, open dan https://muwattah.github.io/Game/.

**Opmerking over oudere bestanden:** `game.js`, `styles.css`, `check.js` en `browser_smoke.py` horen bij de vorige quizversie en worden niet ingeladen door deze standalone renspel-versie. De huidige code staat in `index.html`.

## Geluid en privacy
Het spel gebruikt `speechSynthesis` met taal `ar-SA` voor de Arabische uitspraak, en Web Audio voor beloningsgeluidjes. De Arabische stem en de kwaliteit hangen af van apparaat en browser. **Dit is geen ingesproken kinderstem.** Voor een echte kinderstem moeten gecontroleerde audiobestanden toegevoegd worden. Een kind kan de Arabische tekst blijven zien, ook als spraak niet beschikbaar is.

Er zijn geen accounts, advertenties, trackers of online opslag van voortgang. Het spel slaat voortgang lokaal in de browser op via `localStorage`.

## Onderbouwing en onderwijsontwerp
Bij het ontwerp is gekeken naar gestructureerde letterherkenning, korte herhaling, directe feedback en opbouw op basis van beheersing in plaats van leeftijd. Bronnen: [NICHD / National Reading Panel](https://www.nichd.nih.gov/publications/pubs/nrp/findings) en [overzicht van Arabische lettervormen](https://khatarabic.com/courses/initiate/lessons/l13-all-letter-forms.html).

Dit is een **speelbaar prototype**, nog geen pedagogisch gevalideerde volledige Arabische leesmethode. Idealiter volgt een speeltest met kinderen en controle van de MSA-uitspraak door een Arabisch docent. Vooral kinderen die nog geen Nederlands kunnen lezen kunnen in de eerste levels begeleiding van een ouder gebruiken.

## Wat is getest?
- Desktop (1280×800) en mobiel (390×844).
- Keuze uit 3 kennisniveaus; de eerste wereld heeft 7 levels.
- Alle **79 levels × 3 oefenrondes = 237** op geldige en unieke antwoordopties.
- Rennen, vijf goede poortkeuzes, sterren en overwinningsscherm.
- Geen JavaScript-runtimefouten in de geautomatiseerde browsertest.
