# AppFactory Enterprise v1.0

O companie completă de dezvoltare de aplicații, ca echipă de agenți: 80 de specialiști în 14 departamente — orice stack web (React, Next.js, Vue, Angular, Node, TypeScript, Python, Java, PHP, .NET), pipeline complet de producție de jocuri și un birou de audit independent — cu un skill de orchestrare care direcționează orice misiune prin rolurile potrivite.

A full app development company as an agent team: 80 specialists across 14 departments — any web stack (React, Next.js, Vue, Angular, Node, TypeScript, Python, Java, PHP, .NET), a full game production pipeline, and an independent audit office — with an orchestration skill that routes any mission through the right roles.

---

## 🇷🇴 Română

### Ce face

Instalezi plugin-ul și primești o „fabrică" operativă: de la viziune de produs și inginerie, până la marketing, vânzări, HR cu psiholog organizațional, juridic, contabilitate și suport. Scrii misiunea, iar sistemul alege echipa minimă necesară, rulează rolurile în paralel unde se poate, trece totul prin porți de verificare și asamblează livrabilele finale ca fișiere.

### Noutăți în v1.0 („steroizi" pe toți agenții)

Toți cei 80 de agenți au fost rescriși după un șablon validat de cercetare (cele mai bune colecții publice de agenți — wshobson/agents 35,7k★ și VoltAgent 20,2k★ — plus documentația oficială Claude Code):

- **Porți de finalizare cuantificate** (`done_when`): cifre, nu adjective — p95 < 100 ms, acoperire > 80%, crash < 0,1%.
- **Granițe explicite între roluri** (`workflow_position`): cine consumă ce, cine predă cui, prin ce poartă trece — rutare curată în 80 de roluri.
- **Cunoștințe la zi (iunie 2026)**: React 19.2 + Compiler GA, Next.js 16.2 LTS, TypeScript 6/7-beta, Node 24 LTS, Vue 3.5/Vapor, Nuxt 4.4, Angular 22, Python 3.14, Spring Boot 4/Java 25 LTS, PHP 8.5/Laravel 13, .NET 10 LTS, Unity 6.4, Unreal 5.7, Godot 4.6.3 — cu regulă de verificare a faptelor volatile.
- **Integrare skills.sh**: agenții folosesc skill-uri instalabile ca surse de reguli (vezi `skills/appfactory/references/skills-sh-picks.md`).
- **Garduri profesionale**: rolurile juridice, fiscale, financiare și de psihologie includ disclaimere, întrebări de jurisdicție și escaladare către profesioniști licențiați.
- **Reparat**: 3 agenți trunchiați reconstruiți (`angular-engineer`, `audit-director`, `financial-auditor`), SKILL.md și organigrama rebuilt complet, referințe învechite („48 de agenți") corectate.

### Cum îl folosești

1. Instalează `appfactory-enterprise.plugin` (buton „Save plugin" în Cowork).
2. Scrie misiunea în limbaj natural, de exemplu:
   - „Construiește o aplicație de fitness și lanseaz-o" → fluxul complet W1 + W2;
   - „Construiește un joc roguelike pentru mobil" → pipeline-ul de producție W6 (Game Studio);
   - „Aplicația e lentă și serviciile se desincronizează" → W7 (Web Platform, condus de `tech-lead`);
   - „Plan de marketing cu buget de 5.000 €/lună" → `cmo` + echipa de marketing;
   - „Scrie secvența de e-mailuri reci pentru manageri de HR" → doar `sdr`;
   - „Doi colegi sunt în conflict și echipa dă semne de epuizare" → `org-psychologist`;
   - „Codul e în Next.js, fă funcționalitatea X" → rutare automată către `nextjs-engineer`;
   - „Audit complet înainte de lansare" → `audit-director` + biroul de audit (W8).
3. Primești livrabile ca fișiere, cu decizii, ipoteze și riscuri listate explicit.

### Organigrama (80 de agenți, 14 departamente)

| Departament | Agenți |
|---|---|
| Executiv | `ceo` (orchestrator), `coo` (planuri, termene, RACI, comandă de incident) |
| Produs | `cpo`, `product-manager`, `ux-researcher`, `product-designer`, `product-analyst` |
| Inginerie | `cto`, `solutions-architect`, `frontend-engineer`, `backend-engineer`, `mobile-engineer`, `devops-engineer`, `qa-engineer`, `security-engineer`, `data-engineer`, `ml-engineer`, `tech-writer` |
| Platformă web (seniori) | `tech-lead` (poartă de revizie), `fullstack-engineer`, `distributed-systems-engineer`, `database-engineer`, `realtime-engineer`, `performance-engineer` |
| Ghilda de stack-uri | `react-engineer`, `nextjs-engineer`, `typescript-engineer`, `node-engineer`, `vue-nuxt-engineer`, `angular-engineer`, `python-engineer`, `java-spring-engineer`, `php-laravel-engineer`, `dotnet-engineer` |
| Birou de audit (independent) | `audit-director` (conduce), `code-auditor`, `security-auditor`, `accessibility-auditor`, `ux-auditor`, `compliance-auditor`, `financial-auditor` — doar citesc și raportează, nu implementează |
| Studio de jocuri | `game-producer` (conduce pipeline-ul), `game-designer`, `gameplay-engineer`, `game-engine-engineer`, `game-server-engineer`, `technical-artist`, `level-designer`, `narrative-designer`, `liveops-monetization` |
| Creație | `creative-director` (poartă de calitate), `brand-designer`, `copywriter`, `motion-designer` |
| Marketing | `cmo`, `marketing-strategist`, `content-marketer`, `social-media-manager`, `seo-aso-specialist`, `performance-marketer`, `pr-manager` |
| Vânzări | `cro-sales`, `sdr`, `account-executive`, `customer-success-manager`, `partnerships-manager` |
| Oameni (HR) | `chro`, `recruiter`, `org-psychologist`, `learning-development` |
| Juridic | `general-counsel` (triaj), `contracts-counsel`, `privacy-dpo`, `ip-counsel` |
| Finanțe | `cfo`, `accountant`, `fpa-analyst`, `tax-advisor` |
| Operațiuni | `support-lead`, `procurement-ops` |

### Reguli ale companiei

- Echipa minimă necesară, nu toate departamentele odată.
- Fără fapte inventate: cifrele, legile și limitele de platformă se verifică sau se marchează `[ASSUMPTION]` / `[VERIFY]`.
- Rolurile cu caracter profesional (juridic, fiscal, financiar, psihologie) includ mereu mențiunea că oferă orientare, nu consultanță licențiată.
- Fiecare misiune trece printr-o poartă de verificare (QA, securitate, director de creație sau juridic) înainte de livrare.
- Biroul de audit este independent: citește, punctează, dă verdict PASS/FIX — nu repară niciodată ce auditează.

---

## 🇬🇧 English

### What it does

Install the plugin and you get an operating factory: from product vision and engineering to marketing, sales, HR with an organizational psychologist, legal, accounting, and support. State your mission; the system picks the smallest team that covers it, runs roles in parallel where possible, passes everything through verification gates, and assembles final deliverables as files.

### What's new in v1.0 (every agent on steroids)

All 80 agents rewritten to a research-backed template (top public agent collections — wshobson/agents 35.7k★, VoltAgent 20.2k★ — plus official Claude Code docs): quantified `done_when` gates, explicit `workflow_position` role boundaries, June-2026 stack knowledge with a verify-volatile-facts rule, skills.sh rule-source integrations, professional-services guardrails, and dual routing examples with "Use PROACTIVELY" triggers. Fixed: 3 truncated agents reconstructed, SKILL.md and org chart rebuilt in full, stale facts corrected. Details in `CHANGELOG.md`.

### Components

| Component | Count | Purpose |
|---|---|---|
| Agents | 80 | Specialist roles across 14 departments |
| Skill | 1 | `appfactory` — orchestration: intake → route → execute → gate → assemble |
| References | 2 | `org-chart.md` (full blueprint, workflows W1–W8), `skills-sh-picks.md` (installable rule-source skills) |

### Standard workflows

W1 build an app · W2 launch/GTM · W3 sales motion · W4 back office · W5 incident/crisis · W6 game production · W7 web platform deep work · W8 independent audit. Details in `skills/appfactory/references/org-chart.md`.

### Credits

Structural patterns adapted from the MIT-licensed collections [wshobson/agents](https://github.com/wshobson/agents) and [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents); companion skills from the [skills.sh](https://www.skills.sh) registry. Version facts verified against official release channels (June 2026).

### License

MIT
