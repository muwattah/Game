# Harfia ✦ Arabisch avontuur

Een volledig statisch, mobielvriendelijk Nederlandstalig leerspel om kinderen van **3 t/m 10 jaar** spelenderwijs **Modern Standaardarabisch (الفصحى)** te leren. Zonder accounts, advertenties, tracking of backend.

## 🎮 Spelinhoud (65 levels)

| Wereld | Levels | Inhoud |
| --- | ---: | --- |
| 🌼 De Letterweide | 7 | ا ب ت ث ج ح خ |
| 🌳 Het Klankenbos | 7 | د ذ ر ز س ش ص |
| 🌟 De Sterrenhemel | 7 | ض ط ظ ع غ ف ق |
| 🏰 Het Letterkasteel | 7 | ك ل م ن ه و ي |
| 🎶 De Klankentuin | 9 | Fatha, kasra, damma; ب / ت / م |
| 🧸 De Woordenschat | 12 | Dieren, eten, spullen en emoji's |
| 🔢 Het Tel-eiland | 10 | ١ tot ١٠; tellen, woorden en cijfers |
| 💬 Het Praatplein | 6 | Eenvoudige begroetingen en zinnetjes |

**Leeftijdsinstellingen:** 3–5 jaar — grote visuele herkenningsopgaven; 6–7 jaar — ook klanktekens en vrij tekenen; 8–10 jaar — lettervormen en zinnetjes. Dit zijn *startinstellingen*, niet de garantie dat elk kind hetzelfde tempo volgt. Elk level bestaat uit een korte instructie, gerichte feedback en oefeningen. Levels en werelden openen geleidelijk; het telspel is onmiddellijk beschikbaar.

**Leermechaniek:** leren → actief ophalen uit het geheugen (meerkeuze/luisteropdracht) → bemoedigende feedback → herhaling na 1/3/7/14/30 dagen. Drie sterren per level; fouten leiden niet tot straf. Handmatig tracen is niet automatisch beoordeeld. Voortgang wordt opgeslagen via `localStorage`.

## 🔊 Arabische uitspraak – belangrijk

De applicatie gebruikt de **Web Speech API** en kiest een beschikbare Arabische systeemstem (`ar-*`). De stem wordt iets hoger en langzamer afgespeeld voor een vriendelijke, speelse klank. De letter **naam** en de **klank met fatha** worden afzonderlijk aangeboden. Voor Alif wordt het verschil tussen de alif en de hamza in de uitleg genoemd. Woorden en voorbeelden zijn voorzien van Arabische klinkertekens.

**Grenzen:** dit is **geen opgenomen echte kinderstem**; stemkwaliteit, uitspraak, beschikbaarheid en offline werking zijn afhankelijk van browser/besturingssysteem. Installeer een Arabische TTS-stem in de systeeminstellingen en controleer de uitspraakkwaliteit, met name keelklanken (ح، ع، غ، ق) en korte klinkers. Zonder Arabische stem zijn luistertoetsen vervangen door visuele vragen, en toont de instellingenpagina de beperking. Voor een productie-uitgave kan een professioneel ingesproken, door een moedertaalspreker gecontroleerde audiobibliotheek worden toegevoegd.

## 🚀 Lokaal openen

Open `index.html` in een moderne browser, of voer vanuit deze map uit:

```sh
python3 -m http.server 8000
```

Open vervolgens `http://localhost:8000`. Voor GitHub Pages: open **Settings → Pages** en kies **Deploy from a branch → main → /(root)**. Er zijn geen buildstappen, accounts, API-sleutels, packages of frameworks nodig.

### Geautomatiseerde controles

```sh
node --check game.js
node check.js
```

De controles bewaken het aantal lessen en of elke meerkeuzeopgave precies één correct antwoord heeft voor iedere leeftijdsgroep. Visuele browser- en audioacceptatietesten moeten nog op concrete apparaten worden uitgevoerd.

## 🔍 Onderzoek en didactische verantwoording

1. **Arabische lettervormen:** het Arabische alfabet heeft 28 basisletters, van rechts naar links; de meeste letters veranderen visueel afhankelijk van hun positie. [Arabisch alfabet en schrijfvormen](https://khatarabic.com/courses/initiate/lessons/l13-all-letter-forms.html).
2. **Klinkertekens:** fatha َ, kasra ِ, damma ُ tonen de korte klinkers. Jonge kinderen leren vaak eerst gevocaliseerde teksten, waarna latere lezers steeds meer tekst zonder klinkertekens lezen. [Early Sensitivity to Morphology in Beginning Readers of Arabic](https://pmc.ncbi.nlm.nih.gov/articles/PMC7538675/). Het effect van klinkertekens is niet uitsluitend positief; ze maken tekst visueel ook dichter. [Asadi, 2017](https://www.tandfonline.com/doi/abs/10.1080/17586801.2017.1400493).
3. **Klankbewustzijn:** expliciet oefenen met de relatie tussen geluid en geschreven teken helpt beginnende lezers. Daarom worden *naam* en *klank* bewust apart aangeboden. [National Reading Panel (NICHD)](https://www.nichd.nih.gov/publications/pubs/nrp/Pages/findings.aspx). Dit onderzoek gaat over beginnend lezen in het algemeen en is geen effectiviteitsstudie van dit spel.
4. **Leeftijdsgericht en samen spelen:** voor peuters/kleuters werkt overzichtelijke, hoogwaardige mediacontent het best in samenspraak met een ouder. Daarom zijn sessies kort, animaties beperkt en ontbreekt een negatieve tijdslimiet. [American Academy of Pediatrics](https://publications.aap.org/pediatrics/article/138/5/e20162591/60503) en [AAP Toolkit](https://www.aap.org/en/patient-care/media-and-children/center-of-excellence-on-social-media-and-youth-mental-health/early-childhood-development-and-screen-time-toolkit/).
5. **Technisch:** beschikbare Arabische stemmen komen van het besturingssysteem/de browser; de Web Speech API ondersteunt taal, stem en toonhoogte, maar garandeert geen specifieke kinderstem. [MDN `SpeechSynthesisUtterance`](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance) en [`getVoices`](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices).

**Inhoudelijke review aanbevolen:** Arabische lesinhoud, uitspraak, spelling en pedagogische opbouw zouden vóór grootschalig gebruik door een docent Arabisch/Moedertaalspreker en een kinderpedagoog moeten worden nagekeken. Het spel is een educatieve eerste versie, geen klinisch gevalideerde leermethode.

## 🛡️ Privacy en toegankelijkheid

- Geen registratie, publieke profielen, tracking, advertentiecode of uitgaande verzoeken vanuit de applicatie.
- Lokale opslag bevat alleen leeftijdsstand, behaalde levels, sterren en reviewtijdstippen.
- Mobielvriendelijke knoppen, toetsenbordfocus, statusmeldingen, `lang="ar"` en verminderde animaties bij `prefers-reduced-motion`.
- Geen scorevermindering, geen aflopende timers en geen oneindige beloningsmechanieken.
- Geïntegreerde spraaksynthese kan buiten de applicatie afhankelijk zijn van systeem-/browserdiensten.

## Techniek

Plain HTML, CSS en JavaScript. Bestanden: `index.html`, `styles.css`, `game.js`, `check.js`. Er zijn geen externe runtimebibliotheken nodig.