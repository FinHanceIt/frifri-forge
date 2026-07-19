# TrendForge — Source Registry (backbone)

The "scrape everything" surface. Each acquisition scout owns a **family** below and is expected to expand it to dozens–hundreds of concrete endpoints; `source-registry-keeper` keeps the master, deduplicated, compliance-graded catalog so the fleet can responsibly reach **thousands–tens of thousands** of sources. Nothing is collected unless it is registered and graded.

## Every source is logged against these columns

`source_id | name | family | owning_scout | url/endpoint | method (API/RSS/scrape) | api_status | robots_status | tos_verdict (GREEN/AMBER/RED) | rate_limit | refresh_cadence | reliability_tier (A–F) | region | language | last_pulled | notes`

## Families and representative sources (non-exhaustive seeds)

- **Startup directories** — Product Hunt, YC (Launches, RFS), Indie Hackers, BetaList, Crunchbase, Wellfound/AngelList, Dealroom, Tracxn, EU-Startups, Sifted, Failory, CB Insights, Techstars, 500, Antler, a16z Speedrun, EF.
- **App & software** — Apple App Store charts, Google Play charts, Sensor Tower, data.ai, AppFigures, AppFollow, Steam/SteamDB, itch.io, Chrome Web Store, Edge Add-ons, Firefox AMO, Shopify App Store, G2, Capterra, GetApp, AppSumo, PitchGround.
- **Social** — TikTok Creative Center, Instagram/Reels, YouTube Shorts, X/Twitter, Reddit, Hacker News, LinkedIn, Bluesky, Mastodon, Threads, public Discord (Disboard), Telegram, Pinterest Trends, Snapchat Trends.
- **Video / audio / creator / content** — YouTube, Twitch, Kick, Apple/Spotify Podcasts, Listen Notes, Substack, beehiiv, Ghost, Sparkloop, Medium, DEV.to, Quora, Tumblr, Wattpad, AO3.
- **Search & keyword** — Google Trends, Exploding Topics, Glimpse, TrendHunter, Treendly, autocomplete/PAA (Google/Bing/YouTube/Amazon), Keyword Planner, Ahrefs/Semrush/Ubersuggest exports, Search Console, Bing, Yandex, Baidu Index, Naver.
- **Dev & tech** — GitHub Trending, npm/PyPI/crates/Maven/NuGet, libraries.io, Hugging Face, Stack Overflow/Exchange, Hashnode, Lobste.rs, There's An AI For That, Futurepedia, Toolify.
- **Funding & money** — TechCrunch/Crunchbase News, Axios Pro Rata, Term Sheet, VC blogs & portfolios, YC RFS, SBIR/STTR, EU Horizon/EIC, Kickstarter, Indiegogo, Crowd Supply, S-1 filings, M&A news.
- **Commerce** — Amazon Best Sellers/Movers, Etsy, eRank, AliExpress, Temu, 1688, Gumroad, Lemon Squeezy, Payhip, Whop, eBay, StockX, Depop, Vinted.
- **Jobs / research / news / markets / reviews** — LinkedIn Jobs, Indeed, Wellfound, Greenhouse/Lever, arXiv, bioRxiv, SSRN, Papers with Code, Semantic Scholar, OpenAlex, USPTO/EPO/WIPO, Polymarket, Kalshi, Metaculus, Manifold, CoinGecko, DeFiLlama, Dune, ARK/thematic ETFs, Trustpilot, GDELT, Google News.
- **Regional / international** — Douyin, Xiaohongshu, WeChat, Weibo, 36Kr, Huxiu, TapTap (CN); Inc42, YourStory, ShareChat (IN); Contxto, Mercado Libre (LATAM); Tech in Asia, e27, Shopee/Lazada (SEA); Naver/Kakao, LINE, Nikkei (JP/KR); Wamda, Disrupt Africa, Jumia (MENA/Africa); Sifted regional (EU).

## Tiering

- **GREEN** — official API or explicitly permitted; collect within rate limits.
- **AMBER** — allowed with conditions (attribution, low rate, no personal data); collect carefully.
- **RED** — disallowed by ToS/robots, login/paywalled, or personal/sensitive data → **never collected**.

The registry is versioned so every datum traces to a registered, permitted source (provenance).
