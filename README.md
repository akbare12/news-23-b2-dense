# The World Today — 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b2-dense/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b2-dense/reward.svg)](https://make.fun/bounty/news-image-20261123)

One image summing up 23 November 2026's world news: a dense newspaper
front page — 31 stories, 6 regions, every item dated 23 Nov.

## What it shows

- **Hero 1 — Markets, Seoul:** the AI rout hits Asia. Kospi closes 4,708.54,
  down 3.3% (intraday -5.8%) as the Wall Street sell-off spreads.
- **Hero 2 — United Nations, Barbados:** Guterres urges global AI safety
  rules at the Bridgetown summit: "Regulate AI before it's too late."
- **Hero 3 — Asia Power Index 2026:** the US lead over China is at its
  narrowest since 2018 (78.9 vs 73.6, gap 5.3).
- **World map** with a numbered pin for every story, plus a "Day in Numbers"
  box and a "Not Yet" strip for things still unresolved.
- **Story grid** in four region columns (North America, Europe, Middle East,
  Africa + Asia-Pacific), each card carrying a certainty badge
  (REPORTED / CLAIM / DENIAL / ONGOING) and a named source.
- **Date-check footer** naming the items excluded for not being 23 Nov news
  (Democrats reach 258, Sparta II fire, El Chapo Isidro — all 22 Nov;
  EU–Indonesia pact and the Nigeria boat — 21 Nov; ICJ Myanmar ruling —
  19 Nov).

## How it is built

`draw.py` renders `entry.png` (1024×1024, PIL) from the verified story
list. `main.py` is a standard-library-only copy program: it copies
`entry.png` to `/output/entry.png`. Running it twice produces
byte-identical output, and it makes no network requests.

## Verification

Every headline was checked against at least two independent sources
(AP, Reuters, CNN, BBC, AFP, UN News, WHO, Lowy Institute,
Korea JoongAng Daily, Bloomberg, Morningstar). Items whose date could not
be pinned to 23 November 2026 were left out and are named in the footer.
