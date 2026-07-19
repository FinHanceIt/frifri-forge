# TrendForge — Organization Blueprint

**Total: 168 agents across 20 divisions (78 acquisition scouts).**

Mission: operate as a standalone trend-prediction megastructure. Signals enter through the acquisition scouts, flow through engineering, quality, signal, temporal, network, forecasting, validation, lens and synthesis divisions, and exit as a ranked **Trend Atlas + Prediction Dossiers + Opportunity map**, with Governance crosscutting throughout.

## Pipeline (DAG)

```
ACQUISITION (D1-D10, 78 scouts)
      v
DATA ENGINEERING (D11)  ->  DATA QUALITY & INTEGRITY (D12)
      v
SIGNAL EXTRACTION & CLUSTERING (D13)  ->  [GATE: cross-source corroboration]
      v
TEMPORAL/MOMENTUM (D14)  +  CROSS-SIGNAL/NETWORK (D15)
      v
FORECASTING ENSEMBLE (D16)  ->  VALIDATION/CALIBRATION (D17)  [GATE: validator]
      v
DOMAIN LENSES (D18)  ->  SYNTHESIS (D19)  ->  deliverable
      ^
GOVERNANCE/COMPLIANCE/MEMORY (D20) + COMMAND (D0) crosscut every stage
[GATES: compliance + ethics over all collection]
```

## D0 — Command

| Agent | Purpose |
|---|---|
| `trendforge-director` | TrendForge chief orchestrator. The single entry point for a trend-intelligence mission: it scopes the run, routes the 20 divisions through the pipeline in the right order, holds the gates, and assembles the final Trend Atlas + dossiers + exec brief. |
| `run-planner` | TrendForge run planner. Scopes each run before work starts — which domains, regions, time-horizon and depth, which scouts and lenses to activate, the data budget, and what 'success' means for this mission. |
| `mission-router` | TrendForge router. Executes the pipeline DAG — ordering divisions, deciding parallel vs sequential, passing artifacts between stages, and triggering the gates — so 168 agents move as one coherent flow. |
| `report-assembler` | TrendForge assembler. Collects every division's output into one coherent, deduplicated, provenance-checked package — the Trend Atlas, prediction dossiers, exec brief and emerging watchlist — ready for delivery. |

## D1 — Acquisition: Startup & Company directories

| Agent | Purpose |
|---|---|
| `scout-producthunt` | TrendForge acquisition scout for Product Hunt. Pulls raw trend signals and flags brand-new entities and breakouts from Product Hunt daily/weekly/monthly leaderboards, topics, makers, comments. Use to source Product Hunt data for the trend pipeline. |
| `scout-ycombinator` | TrendForge acquisition scout for Y Combinator. Pulls raw trend signals and flags brand-new entities and breakouts from YC Launches, YC company directory, Requests for Startups (RFS), 'Launch HN' threads. Use to source Y Combinator data for the trend pipeline. |
| `scout-indiehackers` | TrendForge acquisition scout for Indie Hackers. Pulls raw trend signals and flags brand-new entities and breakouts from Indie Hackers products, milestones, revenue posts, forum. Use to source Indie Hackers data for the trend pipeline. |
| `scout-betalist` | TrendForge acquisition scout for BetaList. Pulls raw trend signals and flags brand-new entities and breakouts from BetaList new & upcoming startups, topics. Use to source BetaList data for the trend pipeline. |
| `scout-crunchbase` | TrendForge acquisition scout for Crunchbase. Pulls raw trend signals and flags brand-new entities and breakouts from Crunchbase company profiles, funding rounds, categories (where API/seat allows). Use to source Crunchbase data for the trend pipeline. |
| `scout-wellfound-angellist` | TrendForge acquisition scout for Wellfound / AngelList. Pulls raw trend signals and flags brand-new entities and breakouts from Wellfound startup + jobs listings, AngelList syndicates & rolling funds. Use to source Wellfound / AngelList data for the trend pipeline. |
| `scout-dealroom-tracxn` | TrendForge acquisition scout for Dealroom / Tracxn. Pulls raw trend signals and flags brand-new entities and breakouts from Dealroom, Tracxn and similar databases (where accessible). Use to source Dealroom / Tracxn data for the trend pipeline. |
| `scout-eu-startups` | TrendForge acquisition scout for EU-Startups & regional ecosystems. Pulls raw trend signals and flags brand-new entities and breakouts from EU-Startups, Sifted, regional startup registries & blogs. Use to source EU-Startups & regional ecosystems data for the trend pipeline. |
| `scout-failory-deadpool` | TrendForge acquisition scout for Startup graveyard. Pulls raw trend signals and flags brand-new entities and breakouts from Failory, CB Insights post-mortems, startup-graveyard lists, shutdown announcements. Use to source Startup graveyard data for the trend pipeline. |
| `scout-accelerators` | TrendForge acquisition scout for Accelerators & venture studios. Pulls raw trend signals and flags brand-new entities and breakouts from Techstars, 500 Global, Antler, a16z Speedrun, Entrepreneur First, venture-studio batches. Use to source Accelerators & venture studios data for the … |

## D2 — Acquisition: App & Software ecosystems

| Agent | Purpose |
|---|---|
| `scout-apple-appstore` | TrendForge acquisition scout for Apple App Store. Pulls raw trend signals and flags brand-new entities and breakouts from App Store Top Charts (free/paid/grossing) by category & country, Today tab, new apps. Use to source Apple App Store data for the trend pipeline. |
| `scout-google-play` | TrendForge acquisition scout for Google Play. Pulls raw trend signals and flags brand-new entities and breakouts from Play Store top charts, trending, new releases by category & country. Use to source Google Play data for the trend pipeline. |
| `scout-app-rank-intel` | TrendForge acquisition scout for App rank intelligence. Pulls raw trend signals and flags brand-new entities and breakouts from Sensor Tower, data.ai, AppFigures, AppFollow (where API/seat available). Use to source App rank intelligence data for the trend pipeline. |
| `scout-steam-games` | TrendForge acquisition scout for Steam & PC games. Pulls raw trend signals and flags brand-new entities and breakouts from Steam new/trending/top sellers, wishlists, SteamDB, itch.io. Use to source Steam & PC games data for the trend pipeline. |
| `scout-chrome-webstore` | TrendForge acquisition scout for Browser extensions. Pulls raw trend signals and flags brand-new entities and breakouts from Chrome Web Store, Edge Add-ons, Firefox AMO. Use to source Browser extensions data for the trend pipeline. |
| `scout-shopify-appstore` | TrendForge acquisition scout for Shopify & commerce apps. Pulls raw trend signals and flags brand-new entities and breakouts from Shopify App Store, BigCommerce & Wix app markets. Use to source Shopify & commerce apps data for the trend pipeline. |
| `scout-saas-marketplaces` | TrendForge acquisition scout for SaaS marketplaces. Pulls raw trend signals and flags brand-new entities and breakouts from G2, Capterra, GetApp new & 'emerging' grids. Use to source SaaS marketplaces data for the trend pipeline. |
| `scout-appsumo` | TrendForge acquisition scout for AppSumo & deal platforms. Pulls raw trend signals and flags brand-new entities and breakouts from AppSumo marketplace and 'most wanted', PitchGround, Dealify. Use to source AppSumo & deal platforms data for the trend pipeline. |

## D3 — Acquisition: Social platforms

| Agent | Purpose |
|---|---|
| `scout-tiktok` | TrendForge acquisition scout for TikTok. Pulls raw trend signals and flags brand-new entities and breakouts from TikTok Creative Center (trending hashtags/sounds/creators by region), trending videos, TikTok Shop. Use to source TikTok data for the trend pipeline. |
| `scout-instagram-reels` | TrendForge acquisition scout for Instagram / Reels. Pulls raw trend signals and flags brand-new entities and breakouts from Instagram Reels trends, trending audio, hashtags, Explore. Use to source Instagram / Reels data for the trend pipeline. |
| `scout-youtube-shorts` | TrendForge acquisition scout for YouTube Shorts. Pulls raw trend signals and flags brand-new entities and breakouts from YouTube Shorts trending, hashtags, breakout creators. Use to source YouTube Shorts data for the trend pipeline. |
| `scout-x-twitter` | TrendForge acquisition scout for X / Twitter. Pulls raw trend signals and flags brand-new entities and breakouts from X trending topics, curated lists, keyword search, quote volume. Use to source X / Twitter data for the trend pipeline. |
| `scout-reddit` | TrendForge acquisition scout for Reddit. Pulls raw trend signals and flags brand-new entities and breakouts from Reddit r/all and niche subs, rising tab, search, subreddit-growth tracking. Use to source Reddit data for the trend pipeline. |
| `scout-hackernews` | TrendForge acquisition scout for Hacker News. Pulls raw trend signals and flags brand-new entities and breakouts from HN front page, Ask/Show HN, Who's Hiring, search. Use to source Hacker News data for the trend pipeline. |
| `scout-linkedin` | TrendForge acquisition scout for LinkedIn. Pulls raw trend signals and flags brand-new entities and breakouts from LinkedIn trending posts, hashtags, company growth, job-change signals. Use to source LinkedIn data for the trend pipeline. |
| `scout-bluesky-mastodon-threads` | TrendForge acquisition scout for Emerging social (Bluesky/Mastodon/Threads). Pulls raw trend signals and flags brand-new entities and breakouts from Bluesky feeds & trending, Mastodon trending tags, Threads topics. Use to source Emerging social (Bluesky/Mastodon/Threads) … |
| `scout-discord-public` | TrendForge acquisition scout for Public Discord & Telegram. Pulls raw trend signals and flags brand-new entities and breakouts from public Discord servers (Disboard listings), public Telegram channels. Use to source Public Discord & Telegram data for the trend pipeline. |
| `scout-pinterest` | TrendForge acquisition scout for Pinterest. Pulls raw trend signals and flags brand-new entities and breakouts from Pinterest Trends tool, trending pins & boards by region. Use to source Pinterest data for the trend pipeline. |
| `scout-snapchat` | TrendForge acquisition scout for Snapchat. Pulls raw trend signals and flags brand-new entities and breakouts from Snapchat Trends, Spotlight trending, lenses. Use to source Snapchat data for the trend pipeline. |

## D4 — Acquisition: Video, audio, creator & content

| Agent | Purpose |
|---|---|
| `scout-youtube-longform` | TrendForge acquisition scout for YouTube (long-form). Pulls raw trend signals and flags brand-new entities and breakouts from YouTube trending, search trends, breakout channels, comment mining. Use to source YouTube (long-form) data for the trend pipeline. |
| `scout-twitch` | TrendForge acquisition scout for Twitch & live. Pulls raw trend signals and flags brand-new entities and breakouts from Twitch directory & top categories, breakout streamers, Kick. Use to source Twitch & live data for the trend pipeline. |
| `scout-podcasts` | TrendForge acquisition scout for Podcasts. Pulls raw trend signals and flags brand-new entities and breakouts from Apple Podcasts & Spotify charts, Listen Notes, new-show velocity. Use to source Podcasts data for the trend pipeline. |
| `scout-substack` | TrendForge acquisition scout for Substack. Pulls raw trend signals and flags brand-new entities and breakouts from Substack leaderboards by category, rising newsletters, Notes. Use to source Substack data for the trend pipeline. |
| `scout-newsletter-economy` | TrendForge acquisition scout for Newsletter economy. Pulls raw trend signals and flags brand-new entities and breakouts from beehiiv, Ghost, Sparkloop recommendation directories, Kit (ConvertKit). Use to source Newsletter economy data for the trend pipeline. |
| `scout-medium-blogs` | TrendForge acquisition scout for Medium & blogging. Pulls raw trend signals and flags brand-new entities and breakouts from Medium tags & trending, dev-community blogs, blog aggregators. Use to source Medium & blogging data for the trend pipeline. |
| `scout-quora` | TrendForge acquisition scout for Q&A demand. Pulls raw trend signals and flags brand-new entities and breakouts from Quora trending questions & spaces, cross-referenced with PAA. Use to source Q&A demand data for the trend pipeline. |
| `scout-tumblr-fandom` | TrendForge acquisition scout for Fandom & youth culture. Pulls raw trend signals and flags brand-new entities and breakouts from Tumblr trending tags, fandom wikis, Wattpad trends, AO3 tag growth. Use to source Fandom & youth culture data for the trend pipeline. |

## D5 — Acquisition: Search & keyword demand

| Agent | Purpose |
|---|---|
| `scout-google-trends` | TrendForge acquisition scout for Google Trends. Pulls raw trend signals and flags brand-new entities and breakouts from Google Trends rising & breakout queries, related queries by geo/time, realtime trends. Use to source Google Trends data for the trend pipeline. |
| `scout-exploding-topics-glimpse` | TrendForge acquisition scout for Exploding Topics / Glimpse. Pulls raw trend signals and flags brand-new entities and breakouts from Exploding Topics database & trend pages, Glimpse data. Use to source Exploding Topics / Glimpse data for the trend pipeline. |
| `scout-trendhunter-treendly` | TrendForge acquisition scout for Trend aggregators. Pulls raw trend signals and flags brand-new entities and breakouts from TrendHunter, Treendly, TrendWatching, Springwise. Use to source Trend aggregators data for the trend pipeline. |
| `scout-autocomplete-paa` | TrendForge acquisition scout for Autocomplete & People-Also-Ask. Pulls raw trend signals and flags brand-new entities and breakouts from Google/Bing/YouTube/Amazon autocomplete, People Also Ask, query expansion. Use to source Autocomplete & People-Also-Ask data for the trend pipeline. |
| `scout-keyword-volume` | TrendForge acquisition scout for Keyword volume & SEO. Pulls raw trend signals and flags brand-new entities and breakouts from Keyword Planner, Ahrefs/Semrush/Ubersuggest exports, Google Search Console. Use to source Keyword volume & SEO data for the trend pipeline. |
| `scout-bing-yandex-trends` | TrendForge acquisition scout for Alternative search engines. Pulls raw trend signals and flags brand-new entities and breakouts from Bing Trends, Yandex (RU/CIS), Baidu Index (CN), Naver (KR), DuckDuckGo signals. Use to source Alternative search engines data for the trend pipeline. |

## D6 — Acquisition: Dev & tech leading indicators

| Agent | Purpose |
|---|---|
| `scout-github` | TrendForge acquisition scout for GitHub. Pulls raw trend signals and flags brand-new entities and breakouts from GitHub Trending (daily/weekly by language), star-velocity, topics, new repos, code search. Use to source GitHub data for the trend pipeline. |
| `scout-package-registries` | TrendForge acquisition scout for Package registries. Pulls raw trend signals and flags brand-new entities and breakouts from npm, PyPI, crates.io, Maven, NuGet, RubyGems download stats; libraries.io. Use to source Package registries data for the trend pipeline. |
| `scout-huggingface` | TrendForge acquisition scout for Hugging Face. Pulls raw trend signals and flags brand-new entities and breakouts from Hugging Face trending models, datasets and spaces; downloads & likes. Use to source Hugging Face data for the trend pipeline. |
| `scout-stackoverflow` | TrendForge acquisition scout for Stack Overflow & Q&A. Pulls raw trend signals and flags brand-new entities and breakouts from Stack Overflow tag trends, new tags, question volume, Stack Exchange network. Use to source Stack Overflow & Q&A data for the trend pipeline. |
| `scout-devto-hashnode` | TrendForge acquisition scout for Dev blogging. Pulls raw trend signals and flags brand-new entities and breakouts from DEV.to tags & trending, Hashnode, Lobste.rs. Use to source Dev blogging data for the trend pipeline. |
| `scout-ai-tool-directories` | TrendForge acquisition scout for AI tool directories. Pulls raw trend signals and flags brand-new entities and breakouts from There's An AI For That, Futurepedia, Toolify, Future Tools, AI 'awesome' lists. Use to source AI tool directories data for the trend pipeline. |

## D7 — Acquisition: Funding & money flows

| Agent | Purpose |
|---|---|
| `scout-funding-rounds` | TrendForge acquisition scout for Funding rounds. Pulls raw trend signals and flags brand-new entities and breakouts from TechCrunch funding, Crunchbase News, Axios Pro Rata, Fortune Term Sheet, regional funding trackers. Use to source Funding rounds data for the trend pipeline. |
| `scout-vc-theses` | TrendForge acquisition scout for VC theses & RFS. Pulls raw trend signals and flags brand-new entities and breakouts from VC blogs & portfolios (a16z, Sequoia, YC RFS, Antler), requests-for-startups, public memos. Use to source VC theses & RFS data for the trend pipeline. |
| `scout-grants-gov` | TrendForge acquisition scout for Grants & public programs. Pulls raw trend signals and flags brand-new entities and breakouts from SBIR/STTR, EU Horizon & EIC, national innovation grants, government RFPs. Use to source Grants & public programs data for the trend pipeline. |
| `scout-crowdfunding` | TrendForge acquisition scout for Crowdfunding. Pulls raw trend signals and flags brand-new entities and breakouts from Kickstarter, Indiegogo, Crowd Supply, Gumroad pre-orders. Use to source Crowdfunding data for the trend pipeline. |
| `scout-ma-ipo` | TrendForge acquisition scout for M&A, IPOs & exits. Pulls raw trend signals and flags brand-new entities and breakouts from exit announcements, S-1 filings, acquisition news, thematic public-market moves. Use to source M&A, IPOs & exits data for the trend pipeline. |

## D8 — Acquisition: Commerce & marketplaces

| Agent | Purpose |
|---|---|
| `scout-amazon-movers` | TrendForge acquisition scout for Amazon. Pulls raw trend signals and flags brand-new entities and breakouts from Amazon Best Sellers, Movers & Shakers, New Releases, Most Wished For by category. Use to source Amazon data for the trend pipeline. |
| `scout-etsy` | TrendForge acquisition scout for Etsy & handmade. Pulls raw trend signals and flags brand-new entities and breakouts from Etsy best sellers, trending searches, eRank-style data. Use to source Etsy & handmade data for the trend pipeline. |
| `scout-aliexpress-temu` | TrendForge acquisition scout for Cross-border commerce. Pulls raw trend signals and flags brand-new entities and breakouts from AliExpress hot products, Temu trending, Alibaba/1688 demand. Use to source Cross-border commerce data for the trend pipeline. |
| `scout-gumroad-digital` | TrendForge acquisition scout for Digital products. Pulls raw trend signals and flags brand-new entities and breakouts from Gumroad discover & trending, Lemon Squeezy, Payhip, Whop. Use to source Digital products data for the trend pipeline. |
| `scout-ebay-trends` | TrendForge acquisition scout for Resale & secondary demand. Pulls raw trend signals and flags brand-new entities and breakouts from eBay trending & watch counts, StockX, Depop, Vinted. Use to source Resale & secondary demand data for the trend pipeline. |

## D9 — Acquisition: Jobs, research, news, markets, reviews

| Agent | Purpose |
|---|---|
| `scout-job-boards` | TrendForge acquisition scout for Job boards. Pulls raw trend signals and flags brand-new entities and breakouts from LinkedIn Jobs, Indeed, Wellfound, Otta, Greenhouse/Lever boards. Use to source Job boards data for the trend pipeline. |
| `scout-skills-demand` | TrendForge acquisition scout for Skills demand. Pulls raw trend signals and flags brand-new entities and breakouts from job-posting skill extraction, LinkedIn Skills, Coursera/Udemy enrollment trends. Use to source Skills demand data for the trend pipeline. |
| `scout-tech-news` | TrendForge acquisition scout for Tech news. Pulls raw trend signals and flags brand-new entities and breakouts from TechCrunch, The Verge, Ars Technica, Wired, The Information, Rest of World. Use to source Tech news data for the trend pipeline. |
| `scout-google-news-rss` | TrendForge acquisition scout for News at scale (RSS/GDELT). Pulls raw trend signals and flags brand-new entities and breakouts from Google News, a mass RSS fleet across outlets & topics, GDELT. Use to source News at scale (RSS/GDELT) data for the trend pipeline. |
| `scout-press-releases` | TrendForge acquisition scout for Press releases & PR. Pulls raw trend signals and flags brand-new entities and breakouts from PR Newswire, Business Wire, EIN Presswire, company newsrooms. Use to source Press releases & PR data for the trend pipeline. |
| `scout-arxiv` | TrendForge acquisition scout for arXiv & preprints. Pulls raw trend signals and flags brand-new entities and breakouts from arXiv (cs.AI/LG/CL and more), bioRxiv, SSRN, Papers with Code. Use to source arXiv & preprints data for the trend pipeline. |
| `scout-scholar-semantic` | TrendForge acquisition scout for Scholarly demand. Pulls raw trend signals and flags brand-new entities and breakouts from Google Scholar, Semantic Scholar, OpenAlex, Dimensions. Use to source Scholarly demand data for the trend pipeline. |
| `scout-patents` | TrendForge acquisition scout for Patents. Pulls raw trend signals and flags brand-new entities and breakouts from USPTO, EPO Espacenet, WIPO PatentScope, Google Patents. Use to source Patents data for the trend pipeline. |
| `scout-prediction-markets` | TrendForge acquisition scout for Prediction markets. Pulls raw trend signals and flags brand-new entities and breakouts from Polymarket, Kalshi, Metaculus, Manifold. Use to source Prediction markets data for the trend pipeline. |
| `scout-crypto-onchain` | TrendForge acquisition scout for Crypto & on-chain. Pulls raw trend signals and flags brand-new entities and breakouts from CoinGecko, DeFiLlama, Dune dashboards, DappRadar, crypto GitHub. Use to source Crypto & on-chain data for the trend pipeline. |
| `scout-thematic-etfs` | TrendForge acquisition scout for Thematic ETFs & public markets. Pulls raw trend signals and flags brand-new entities and breakouts from ARK and thematic ETF holdings, sector indices, analyst theme reports. Use to source Thematic ETFs & public markets data for the trend pipeline. |
| `scout-reviews-voc` | TrendForge acquisition scout for Reviews & voice-of-customer. Pulls raw trend signals and flags brand-new entities and breakouts from App Store/Play reviews, Trustpilot, G2/Capterra, Amazon reviews. Use to source Reviews & voice-of-customer data for the trend pipeline. |

## D10 — Acquisition: Regional & international

| Agent | Purpose |
|---|---|
| `scout-china` | TrendForge acquisition scout for China. Pulls raw trend signals and flags brand-new entities and breakouts from Douyin, Xiaohongshu (RED), WeChat, Weibo hot search, 36Kr, Huxiu, TapTap. Use to source China data for the trend pipeline. |
| `scout-india` | TrendForge acquisition scout for India. Pulls raw trend signals and flags brand-new entities and breakouts from Indian app charts, Inc42, YourStory, ShareChat/Moj, regional-language apps. Use to source India data for the trend pipeline. |
| `scout-latam` | TrendForge acquisition scout for Latin America. Pulls raw trend signals and flags brand-new entities and breakouts from Contxto, LABS, regional app charts, Mercado Libre trends, Brazil & Mexico ecosystems. Use to source Latin America data for the trend pipeline. |
| `scout-sea` | TrendForge acquisition scout for Southeast Asia. Pulls raw trend signals and flags brand-new entities and breakouts from Tech in Asia, e27, Shopee/Lazada trends, Grab/Gojek ecosystem, regional charts. Use to source Southeast Asia data for the trend pipeline. |
| `scout-japan-korea` | TrendForge acquisition scout for Japan & Korea. Pulls raw trend signals and flags brand-new entities and breakouts from Japanese & Korean app charts, Naver/Kakao, LINE, Korean webtoon/IP, Nikkei tech. Use to source Japan & Korea data for the trend pipeline. |
| `scout-mena-africa` | TrendForge acquisition scout for MENA & Africa. Pulls raw trend signals and flags brand-new entities and breakouts from Wamda, Disrupt Africa, regional app charts, mobile-money ecosystems, Jumia. Use to source MENA & Africa data for the trend pipeline. |
| `scout-eu-regional` | TrendForge acquisition scout for EU regional deep-dive. Pulls raw trend signals and flags brand-new entities and breakouts from DACH, Nordics, France, UK and CEE startup media & charts; Sifted regional. Use to source EU regional deep-dive data for the trend pipeline. |

## D11 — Data Engineering / Pipeline

| Agent | Purpose |
|---|---|
| `ingestion-engineer` | TrendForge ingestion engineer. Writes and runs the Python that actually pulls data for the scouts — API clients, pagination, incremental pulls, retries, backfills — and lands raw batches for the pipeline. |
| `scraper-engineer` | TrendForge scraping engineer. Builds compliant HTML/JS scrapers (requests+BeautifulSoup, Playwright) ONLY for sources without a usable API and where robots.txt/ToS allow — sitemaps, pagination, politeness, parsing. |
| `api-integrations-keeper` | TrendForge API integrations keeper. Owns API clients, authentication, key management (env vars), quota budgeting and schema-drift detection across every data provider the scouts use. |
| `rate-limit-proxy-manager` | TrendForge throttle authority. Sets concurrency caps, politeness delays, exponential backoff, caching and (where lawful) IP rotation so the whole fleet collects at scale without abusing sources or getting blocked. |
| `source-registry-keeper` | TrendForge source registry keeper. Maintains the master catalog of every source the fleet touches — potentially thousands of sites — with URL, access method, API/robots/ToS status, rate limit, refresh cadence, reliability and owning scout. |
| `schema-normalizer` | TrendForge schema normalizer. Maps every source's messy payload into one canonical signal schema (entity, type, source, timestamp, magnitude, geo, lang, raw_ref) so heterogeneous data becomes one queryable panel. |
| `entity-resolver-deduper` | TrendForge entity resolver. Recognizes when the same company, app, product or topic appears across sources under different names and merges them into one canonical entity with stable IDs. |
| `language-normalizer` | TrendForge language normalizer. Detects language and produces canonical (English) text for clustering and search while preserving the original — so non-English signals (China, India, LATAM, EU) are not lost. |
| `enrichment-tagger` | TrendForge enrichment tagger. Adds the metadata that makes signals analyzable: taxonomy category, geography, named entities, and a first-pass sentiment/intent tag. |
| `embeddings-vectorizer` | TrendForge embeddings engineer. Computes text embeddings for every signal and maintains the vector store that powers clustering, semantic dedupe and emerging-term search. |
| `storage-timeseries-architect` | TrendForge storage architect. Designs the data lake and time-series panel (DuckDB/Parquet/SQLite) the whole system reads and writes — partitioning, the signal panel, and the trend history that makes backtesting possible. |

## D12 — Data Quality & Integrity

| Agent | Purpose |
|---|---|
| `bot-astroturf-detector` | TrendForge manipulation detector. Flags coordinated inauthentic behavior, bought engagement and bot-driven spikes so fake virality does not get predicted as a real trend. |
| `spam-noise-filter` | TrendForge noise filter. Removes spam, off-topic, duplicate-content and junk items so the analysis layer works on clean signal, not garbage. |
| `source-reliability-grader` | TrendForge reliability grader. Scores each source on an Admiralty-style scale (reliability x credibility) so signals are weighted by how trustworthy their origin is. |
| `sampling-bias-auditor` | TrendForge sampling-bias auditor. Detects when the data over-represents some languages, regions, platforms or demographics and corrects the lens so trends aren't just 'what English Twitter thinks'. |
| `survivorship-bias-auditor` | TrendForge survivorship-bias auditor. Forces the dead and the failed into the analysis (via the startup-graveyard scout) so we don't mistake a category's winners for the whole story. |
| `independence-correlation-auditor` | TrendForge independence auditor. Stops correlation laundering — the same story echoed across many outlets counted as many confirmations — by clustering correlated sources into one effective signal. |
| `coverage-gap-monitor` | TrendForge coverage-gap monitor. Tracks which sources, regions and domains are missing, stale or thin and dispatches requests to fill them so the fleet's view stays complete. |
| `outlier-validator` | TrendForge outlier validator. Decides whether a sudden spike is a real signal or an artifact (data glitch, one-off event, duplicate) before it propagates into trend scores and forecasts. |

## D13 — Signal Extraction & Clustering

| Agent | Purpose |
|---|---|
| `signal-atomizer` | TrendForge signal atomizer. Converts every normalized record into an atomic signal — entity + timestamp + source + magnitude + context — the indivisible unit the whole analysis layer counts. |
| `topic-clusterer` | TrendForge topic clusterer. Groups atomic signals into coherent themes/niches using embeddings and topic modeling, turning a firehose of items into a manageable set of candidate trends. |
| `entity-graph-builder` | TrendForge graph builder. Builds the network of entities and niches — who co-occurs with whom, competitors, suppliers, adjacents — so trends are understood in context, not in isolation. |
| `cross-source-corroborator` | TrendForge corroborator. Enforces the graduation rule: a candidate trend is only real if it shows up across multiple INDEPENDENT sources and source-types — killing single-source hype before it reaches forecasting. |
| `taxonomy-keeper` | TrendForge taxonomy keeper. Maintains the stable category tree that every agent classifies into, so the same trend isn't filed five different ways across runs and domains. |
| `emerging-entity-detector` | TrendForge emerging-entity detector. Hunts the newest of the new — brand-new terms, names, tools and memes appearing across sources for the first time — the raw material of next-wave trends. |
| `sentiment-intent-classifier` | TrendForge sentiment & intent classifier. Distinguishes excitement, complaint, purchase-intent and the gold signal 'I would pay for this' so trends are read by what people FEEL and INTEND, not just volume. |
| `jtbd-pain-extractor` | TrendForge jobs-to-be-done extractor. Mines complaints, wishes and workarounds into crisp pain statements and jobs-to-be-done — the fuel that turns a trend into a concrete product opportunity. |

## D14 — Temporal & Momentum Analysis

| Agent | Purpose |
|---|---|
| `momentum-velocity-analyst` | TrendForge momentum analyst. Measures the first derivative — how fast each trend is growing right now — normalized across sources, the base metric of 'what's hot'. |
| `acceleration-inflection-analyst` | TrendForge acceleration analyst. Tracks the second derivative to catch inflection points — the moment a trend's growth itself starts accelerating or rolling over — the single most valuable timing signal. |
| `breakout-detector` | TrendForge breakout detector. Flags statistically significant spikes against each trend's own baseline (z-score, STL residual, change-point) so genuine breakouts are caught fast and noise isn't. |
| `seasonality-decomposer` | TrendForge seasonality decomposer. Separates seasonal patterns from real trend so a December spike in 'gifts' isn't mistaken for an emerging movement. |
| `fad-vs-trend-classifier` | TrendForge fad-vs-trend classifier. Judges durability — distinguishing a spike-and-crash fad from a sustained trend — by curve shape, breadth and adoption signals, so we don't predict fireworks as sunrises. |
| `lifecycle-scurve-stager` | TrendForge lifecycle stager. Places each trend on the adoption S-curve — emerging, rising, peaking, mature, declining — so timing advice ('enter now' vs 'too late') is grounded. |
| `saturation-tam-estimator` | TrendForge saturation estimator. Estimates the ceiling — how big a trend can get and how much room is left — so a near-saturated trend isn't sold as a wide-open opportunity. |
| `lead-lag-correlator` | TrendForge lead-lag correlator. Discovers which sources reliably LEAD others (e.g. arXiv -> GitHub -> Product Hunt -> App Store) and by how long — the leading-indicator map that makes real prediction possible. |
| `diffusion-bass-modeler` | TrendForge diffusion modeler. Fits Bass/diffusion adoption curves to estimate innovation and imitation rates, ultimate market size and the timing of takeoff and peak. |

## D15 — Cross-Signal & Network Intelligence

| Agent | Purpose |
|---|---|
| `convergence-detector` | TrendForge convergence detector. Finds where two or more trends are merging (e.g. AI + the specific vertical) because the intersections are usually where the biggest, least-crowded opportunities are. |
| `virality-network-modeler` | TrendForge virality modeler. Estimates how contagious a trend is — effective reproduction rate, branching structure — to tell explosive organic spread from a flat push that will fizzle. |
| `influencer-propagation-tracker` | TrendForge propagation tracker. Identifies the seed accounts and amplifiers spreading a trend and whether the spread is organic, creator-led or coordinated/paid — context that changes what a trend means. |
| `geographic-diffusion-tracker` | TrendForge geographic diffusion tracker. Follows trends across regions ('big in Korea, hitting the US in ~4 months') to exploit the geographic lag that is one of the most reliable predictors. |
| `capital-attention-flow-mapper` | TrendForge flow mapper. Fuses funding + hiring + search + social + dev signals into one 'where is energy going' map, because trends backed by money AND attention AND builders are the ones that stick. |
| `competitive-density-mapper` | TrendForge competitive-density mapper. Measures how crowded a trend already is — number of entrants, funded players, incumbents — so a saturated red ocean isn't predicted as an open opportunity. |

## D16 — Forecasting Ensemble

| Agent | Purpose |
|---|---|
| `forecast-orchestrator` | TrendForge forecast orchestrator. Assigns each graduated trend to the right forecasting methods based on its data shape, runs the ensemble, and collects point+interval forecasts for blending and validation. |
| `forecaster-arima-sarimax` | TrendForge forecasting specialist using ARIMA/SARIMAX. Produces point forecasts WITH 80% and 95% prediction intervals for trend trajectories; strongest when the series is fairly stationary with clear autocorrelation or seasonality and enough history. |
| `forecaster-prophet` | TrendForge forecasting specialist using Prophet. Produces point forecasts WITH 80% and 95% prediction intervals for trend trajectories; strongest when there is strong multi-seasonality, holidays, and some missing data. |
| `forecaster-xgboost-quantile` | TrendForge forecasting specialist using gradient-boosted trees with quantile regression. Produces point forecasts WITH 80% and 95% prediction intervals for trend trajectories; strongest when rich exogenous features such as lead-lag indicators are available. |
| `forecaster-bayesian-structural` | TrendForge forecasting specialist using Bayesian structural time series. Produces point forecasts WITH 80% and 95% prediction intervals for trend trajectories; strongest when you need interpretable components and principled uncertainty with regressors. |
| `forecaster-analogy-historical` | TrendForge forecasting specialist using historical-analogy matching. Produces point forecasts WITH 80% and 95% prediction intervals for trend trajectories; strongest when the trend closely resembles past trends whose trajectories are known. |
| `leading-indicator-chain-forecaster` | TrendForge causal-chain forecaster. Uses the lead-lag map to predict later-stage signals from earlier ones (e.g. forecast App Store demand from today's GitHub + arXiv + Reddit activity) — the most causal forecaster in the ensemble. |
| `emergence-predictor` | TrendForge emergence predictor — the special sauce. Predicts trends BEFORE they break out, from early-source patterns (research, dev, fringe communities, emerging entities) plus acceleration, outputting candidate FUTURE trends with probability and ETA. |
| `scenario-planner` | TrendForge scenario planner. For each major prediction (and the landscape overall) builds best / base / worst scenarios plus wildcards, with probabilities — so Fri sees a distribution of futures, not one fragile guess. |
| `counterfactual-premortem` | TrendForge premortem analyst. Assumes each prediction turns out WRONG and works backward to find why — fragile assumptions, missing data, regime risks — then recommends confidence cuts. The adversary of the forecast. |
| `timing-window-estimator` | TrendForge timing estimator. Converts forecasts into actionable timing — the entry window, expected peak, and decline onset — so a correct trend call comes with WHEN to move, not just whether. |
| `ensemble-blender` | TrendForge ensemble blender. Combines the individual forecasters into one consensus forecast, weighting each model by its validated accuracy and reconciling their prediction intervals into honest, calibrated uncertainty. |

## D17 — Validation, Calibration & Bias Control

| Agent | Purpose |
|---|---|
| `backtester-walkforward` | TrendForge backtester. Walk-forward backtests the forecasting methods on historical trends and computes honest error metrics (MAE/RMSE/MAPE/pinball/Brier) per method and per regime, so model weights are earned, not assumed. |
| `calibration-auditor` | TrendForge calibration auditor. Checks whether the prediction intervals are honest — do 80% intervals actually contain the truth 80% of the time? — and recalibrates over/under-confident forecasts. |
| `forecast-validator-gate` | TrendForge validation gate. The mandatory checkpoint before any prediction ships: verifies no leakage, acceptable backtest accuracy, honest calibration, and basic sanity — then issues ACCEPT / RE-RUN / REJECT. |
| `hype-cycle-corrector` | TrendForge hype-cycle corrector. Applies Gartner-style correction so a trend at the peak of inflated expectations isn't naively extrapolated to the moon — anticipating the trough before the plateau. |
| `recency-bias-corrector` | TrendForge recency-bias corrector. Stops the system from over-weighting the latest spike or newest data point at the expense of base rates and history, a top cause of bad trend calls. |
| `lookahead-leakage-auditor` | TrendForge leakage auditor. Guarantees no future information sneaks into the features used for forecasting — the silent killer that makes backtests look great and live predictions fail. |
| `confidence-scorer` | TrendForge confidence scorer. Assigns each prediction a final, calibrated confidence from data quality, corroboration, model agreement and backtested accuracy — so Fri knows which calls to bet on and which to merely watch. |

## D18 — Domain Lenses

| Agent | Purpose |
|---|---|
| `lens-consumer-apps` | TrendForge domain lens for consumer apps. Re-reads ranked trends through consumer apps-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which consumer apps trends are real and when they break. |
| `lens-b2b-saas` | TrendForge domain lens for B2B SaaS. Re-reads ranked trends through B2B SaaS-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which B2B SaaS trends are real and when they break. |
| `lens-ai-ml-tools` | TrendForge domain lens for AI/ML tools. Re-reads ranked trends through AI/ML tools-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which AI/ML tools trends are real and when they break. |
| `lens-fintech` | TrendForge domain lens for fintech. Re-reads ranked trends through fintech-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which fintech trends are real and when they break. |
| `lens-healthtech` | TrendForge domain lens for healthtech. Re-reads ranked trends through healthtech-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which healthtech trends are real and when they break. |
| `lens-gaming` | TrendForge domain lens for gaming. Re-reads ranked trends through gaming-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which gaming trends are real and when they break. |
| `lens-creator-economy` | TrendForge domain lens for creator economy. Re-reads ranked trends through creator economy-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which creator economy trends are real and when they break. |
| `lens-ecommerce-dtc` | TrendForge domain lens for e-commerce / DTC. Re-reads ranked trends through e-commerce / DTC-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which e-commerce / DTC trends are real and when they break. |
| `lens-devtools-infra` | TrendForge domain lens for developer tools & infrastructure. Re-reads ranked trends through developer tools & infrastructure-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which developer tools & infrastructure trends are real and when they break. |
| `lens-crypto-web3` | TrendForge domain lens for crypto / web3. Re-reads ranked trends through crypto / web3-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which crypto / web3 trends are real and when they break. |
| `lens-edtech` | TrendForge domain lens for edtech. Re-reads ranked trends through edtech-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which edtech trends are real and when they break. |
| `lens-climate-energy` | TrendForge domain lens for climate & energy. Re-reads ranked trends through climate & energy-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which climate & energy trends are real and when they break. |
| `lens-hardware-iot` | TrendForge domain lens for hardware & IoT. Re-reads ranked trends through hardware & IoT-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which hardware & IoT trends are real and when they break. |
| `lens-social-community` | TrendForge domain lens for social & community. Re-reads ranked trends through social & community-specific dynamics — leading indicators, adoption lag and monetization signals — to sharpen which social & community trends are real and when they break. |

## D19 — Application & Synthesis

| Agent | Purpose |
|---|---|
| `trend-ranker` | TrendForge ranker. Scores and ranks every graduated trend on a composite of momentum, durability, corroboration, headroom, capital/attention alignment, low crowdedness and confidence — producing the master ranked list. |
| `opportunity-mapper` | TrendForge opportunity mapper. Translates top trends into concrete, buildable product/app opportunities by fusing the trend with extracted pains (JTBD), open whitespace and the domain lens — turning 'what's trending' into 'what to build'. |
| `whitespace-finder` | TrendForge whitespace finder. Locates the unmet gaps — high-pain niches with bad or missing solutions, and open sub-niches inside crowded trends — where a newcomer can actually win. |
| `trend-atlas-writer` | TrendForge atlas writer. Produces the flagship deliverable — a ranked Trend Atlas where each trend gets evidence, momentum, lifecycle, forecast and confidence — in clear bilingual (RO/EN) prose, no hallucinated numbers. |
| `prediction-dossier-writer` | TrendForge dossier writer. For each top prediction, writes a deep dossier: trajectory and intervals, timing window, scenarios, the driving evidence chain, risks/premortem, and sources — the document you act on. |
| `exec-brief-writer` | TrendForge exec-brief writer. Distills the entire run into a one-page TL;DR — the top calls, what to do about them, and how confident to be — for fast decisions. |

## D20 — Governance, Compliance & Memory

| Agent | Purpose |
|---|---|
| `compliance-officer` | TrendForge compliance officer — the legal/ethical gate over all collection. Enforces robots.txt, ToS, rate limits and GDPR across every source, marks sources GREEN/AMBER/RED, and can block any collection. Scouts must obey it. |
| `ethics-manipulation-guard` | TrendForge ethics guard. Flags trends and opportunities that are manipulative, harmful, or exploit vulnerable groups, and stops the system from amplifying astroturfed or dangerous trends. Holds the safety flag. |
| `provenance-tracker` | TrendForge provenance tracker. Ensures every claim, number and prediction can be traced to its source and timestamp, so the whole report is auditable and nothing is an orphan assertion. |
| `memory-ledger-keeper` | TrendForge memory ledger. Keeps the cross-run record of every trend and prediction — what was called, when, at what confidence — so trends are tracked over time and the system can learn from its own history. |
| `run-retrospective` | TrendForge retrospective. After each run, scores past predictions against what actually happened, computes hit-rate and calibration, and feeds the lessons back to improve model weights and process — the learning loop. |
