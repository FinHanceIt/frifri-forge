# SearchForge — Schema Library (copy-paste JSON-LD)

Owned by `structured-data-specialist`. Each recipe = a validated JSON-LD block + when to use it + an eligibility note. Placeholders use `example.com` and RO examples where natural; swap in real values. Deliver as JSON-LD in a `<script type="application/ld+json">` in `<head>` or `<body>`.

**Read this first (honesty note):** Structured data **does not rank** and **does not guarantee a rich result**. It **clarifies entities** for classic rich results **and** AI engines — that's the value. Google has narrowed rich results over time (FAQ rich result heavily narrowed/removed by Google on the 2026 timeline `[VERIFY current status]` — don't rely on a rich result; the FAQPage markup still helps entity/Q&A clarity for classic and AI search; HowTo heavily reduced) — treat all rich-result eligibility as **`[VERIFY]`** against current Google docs + Rich Results Test before promising it.

---

## Organization
Identifies the brand as an entity; powers knowledge-panel signals and AI entity resolution via `sameAs`. Site-wide, once.
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Example SRL",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Short factual description of what the company does.",
  "sameAs": [
    "https://www.linkedin.com/company/example",
    "https://www.facebook.com/example",
    "https://www.instagram.com/example"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+40-21-000-0000",
    "contactType": "customer support",
    "areaServed": "RO",
    "availableLanguage": ["Romanian", "English"]
  }
}
```
*Eligibility:* no standalone rich result, but core to entity clarity. Keep `sameAs` to canonical profiles only.

---

## WebSite (+ Sitelinks Searchbox)
Declares the site entity and **may** enable the search box in branded SERPs. Site-wide, once.
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://example.com/#website",
  "url": "https://example.com",
  "name": "Example",
  "publisher": { "@id": "https://example.com/#organization" },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```
*Eligibility:* sitelinks searchbox is **Google's discretion** `[VERIFY]`; the entity value stands regardless.

---

## BreadcrumbList
Shows hierarchy in results and helps engines understand site structure. On any nested page.
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://example.com/blog" },
    { "@type": "ListItem", "position": 3, "name": "Article Title", "item": "https://example.com/blog/article-title" }
  ]
}
```
*Eligibility:* breadcrumb rich result is widely supported and low-risk.

---

## Article / BlogPosting (+ author + dates)
For editorial content; supplies the **author + published/updated dates** that classic results and AI engines reward. The dates should also be **visible on the page**.
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Article Title Under ~60 Characters",
  "description": "One-sentence summary of the article.",
  "image": "https://example.com/images/article.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author/author-name"
  },
  "publisher": { "@id": "https://example.com/#organization" },
  "datePublished": "2026-06-01",
  "dateModified": "2026-06-17",
  "mainEntityOfPage": "https://example.com/blog/article-title"
}
```
*Eligibility:* article rich result mainly for news/`NewsArticle`; for blogs the value is entity + freshness clarity (cross-ref `geo-aeo-playbook.md`).

---

## Product (+ Offer + AggregateRating + Review)
For PDPs. Can drive price/availability/review rich results. Only include `AggregateRating`/`Review` for **genuine** on-page reviews — faking them is a spam violation.
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/images/product.jpg"],
  "description": "Factual product description.",
  "sku": "SKU-123",
  "brand": { "@type": "Brand", "name": "Example" },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product/product-name",
    "priceCurrency": "RON",
    "price": "199.00",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "reviewCount": "128"
  }
}
```
*Eligibility:* product rich results supported; rating snippets require real, visible reviews `[VERIFY merchant rules]`.

---

## FAQPage
Q&A markup. FAQ rich result heavily narrowed/removed by Google on the 2026 timeline `[VERIFY current status]` — don't rely on a rich result; the FAQPage markup still helps entity/Q&A clarity for classic and AI search. Valid Schema.org type that Google ignores harmlessly. Use Q&A *content* on-page regardless.
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the return window?",
      "acceptedAnswer": { "@type": "Answer", "text": "Returns are accepted within 14 days." }
    },
    {
      "@type": "Question",
      "name": "Do you ship across the EU?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, we ship to all EU member states." }
    }
  ]
}
```
*Eligibility:* FAQ rich result heavily narrowed/removed on the 2026 timeline `[VERIFY current status]`; keep for clarity, don't promise SERP enhancement.

---

## LocalBusiness (RO example)
For a physical location; supports local entity signals and matches GBP NAP. Use the most specific subtype (e.g. `Restaurant`, `Store`) when it fits.
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://example.ro/#localbusiness",
  "name": "Cofetăria Exemplu",
  "image": "https://example.ro/images/shop.jpg",
  "url": "https://example.ro",
  "telephone": "+40-21-000-0000",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Strada Exemplu 12",
    "addressLocality": "București",
    "addressRegion": "B",
    "postalCode": "010101",
    "addressCountry": "RO"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 44.4268, "longitude": 26.1025 },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00", "closes": "18:00"
  }]
}
```
*Eligibility:* supports local results; **NAP must match** GBP + citations exactly (cross-ref `audit-checklists.md` §5).

---

## VideoObject (+ optional Clip / key moments)
For pages hosting/embedding video; can drive video rich results + key-moments. Mirror `video-seo-specialist`'s metadata.
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Video Title",
  "description": "What the video covers.",
  "thumbnailUrl": ["https://example.com/images/video-thumb.jpg"],
  "uploadDate": "2026-06-10",
  "duration": "PT4M30S",
  "contentUrl": "https://example.com/video.mp4",
  "embedUrl": "https://example.com/embed/video",
  "hasPart": [
    { "@type": "Clip", "name": "Intro", "startOffset": 0, "url": "https://example.com/watch?t=0" },
    { "@type": "Clip", "name": "Main point", "startOffset": 60, "url": "https://example.com/watch?t=60" }
  ]
}
```
*Eligibility:* video rich result + key moments supported `[VERIFY]`; needs a real, accessible thumbnail + duration.

---

## Person (author / E-E-A-T)
Builds the **author entity** behind bylined content; pair with author bio pages and `sameAs`. Strengthens Experience/Expertise signals for classic + AI.
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://example.com/author/author-name/#person",
  "name": "Author Name",
  "url": "https://example.com/author/author-name",
  "jobTitle": "Senior Editor",
  "worksFor": { "@id": "https://example.com/#organization" },
  "sameAs": [
    "https://www.linkedin.com/in/authorname",
    "https://twitter.com/authorname"
  ]
}
```
*Eligibility:* no standalone rich result; high value for E-E-A-T + AI author resolution.

---

## Event
For events; supports event rich results + Google event listings. Use absolute `startDate`/`endDate` with timezone.
```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Event Name",
  "startDate": "2026-09-15T10:00:00+03:00",
  "endDate": "2026-09-15T17:00:00+03:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Venue Name",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Strada Exemplu 1",
      "addressLocality": "Cluj-Napoca",
      "addressCountry": "RO"
    }
  },
  "organizer": { "@id": "https://example.com/#organization" },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/event/tickets",
    "price": "0",
    "priceCurrency": "RON",
    "availability": "https://schema.org/InStock"
  }
}
```
*Eligibility:* event rich result supported `[VERIFY]`; online events need `eventAttendanceMode` + a virtual `location`.

---

## Recipe
For recipe pages; supports recipe rich results + carousels. Mark times in ISO 8601.
```json
{
  "@context": "https://schema.org",
  "@type": "Recipe",
  "name": "Recipe Name",
  "image": ["https://example.com/images/recipe.jpg"],
  "author": { "@type": "Person", "name": "Author Name" },
  "datePublished": "2026-06-01",
  "description": "Short recipe description.",
  "prepTime": "PT15M",
  "cookTime": "PT30M",
  "totalTime": "PT45M",
  "recipeYield": "4 servings",
  "recipeIngredient": ["200 g flour", "2 eggs", "100 ml milk"],
  "recipeInstructions": [
    { "@type": "HowToStep", "text": "Mix the dry ingredients." },
    { "@type": "HowToStep", "text": "Add eggs and milk, whisk." }
  ],
  "nutrition": { "@type": "NutritionInformation", "calories": "320 calories" }
}
```
*Eligibility:* recipe rich result supported `[VERIFY]`; ratings need real reviews.

---

## Validation steps (run before shipping any block)
1. **Rich Results Test** (Google) — confirms eligibility + flags errors for the supported types.
2. **Schema Markup Validator (schema.org)** — confirms the markup is syntactically valid (covers types Google's tool doesn't).
3. **GSC → Enhancements / structured-data reports** — confirms Google parsed it live after deployment, and surfaces site-wide errors.

> Match schema to **on-page reality** (don't mark up content that isn't visible). One `@id` per entity, referenced across blocks, keeps the entity graph clean. When in doubt about a rich result, ship the schema for entity clarity but promise only `[VERIFY]`-confirmed enhancements.
