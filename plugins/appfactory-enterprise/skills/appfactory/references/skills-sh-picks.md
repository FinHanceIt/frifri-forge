# skills.sh picks — recommended add-ons for AppFactory (refreshed June 2026)

Curated from the skills.sh leaderboard (the open-source Agent Skills registry by Vercel — install: `npx skills add <owner/repo>`, discover: `npx skills find`). When any of these skills is installed locally, the matching AppFactory agent applies it as an authoritative rule source — installed skill rules take precedence over agent defaults when they conflict (they are maintained upstream).

## Web development (Stack Guild + Engineering companions)

| Skill | Install | Used by agent |
|---|---|---|
| vercel-react-best-practices (perf rules: waterfalls, bundle, re-renders) | `npx skills add vercel-labs/agent-skills` | react-engineer, nextjs-engineer |
| vercel-composition-patterns | `npx skills add vercel-labs/agent-skills` | react-engineer |
| vercel-react-view-transitions | `npx skills add vercel-labs/agent-skills` | react-engineer, frontend-engineer |
| vercel-optimize | `npx skills add vercel-labs/agent-skills` | performance-engineer |
| next-best-practices (App Router, RSC boundaries) | `npx skills add vercel-labs/next-skills` | nextjs-engineer |
| next-cache-components (PPR, use cache, cacheTag) | `npx skills add vercel-labs/next-skills` | nextjs-engineer |
| official React skills | `npx skills add facebook/react` | react-engineer |
| typescript-advanced-types | `npx skills add wshobson/agents` | typescript-engineer |
| tailwind-design-system | `npx skills add wshobson/agents` | frontend-engineer, product-designer |
| shadcn (component usage + Tailwind integration) | `npx skills add shadcn/ui` | frontend-engineer, react-engineer |
| frontend-design (Anthropic) | `npx skills add anthropics/skills` | product-designer, frontend-engineer |
| design-taste pack (design-taste-frontend, high-end-visual-design, minimalist-ui, brandkit) | `npx skills add leonxlnx/taste-skill` | product-designer, brand-designer |
| supabase-postgres-best-practices | `npx skills add supabase/agent-skills` | database-engineer, backend-engineer |
| better-auth-best-practices | `npx skills add better-auth/skills` | backend-engineer, security-engineer |
| firebase-basics / firebase-security-rules-auditor / firebase-app-hosting-basics | `npx skills add firebase/agent-skills` | backend-engineer, security-engineer |
| convex-quickstart | `npx skills add get-convex/agent-skills` | backend-engineer, realtime-engineer |
| vercel-react-native-skills (Expo/RN) | `npx skills add vercel-labs/agent-skills` | mobile-engineer |
| building-native-ui (Expo) | `npx skills add expo/skills` | mobile-engineer |
| deploy-to-vercel | `npx skills add vercel-labs/agent-skills` | devops-engineer |
| sentry-cli (official Sentry) | `npx skills add sentry/dev` | devops-engineer, performance-engineer |
| turborepo (monorepo pipelines) | `npx skills add vercel/turborepo` | typescript-engineer, devops-engineer |
| ai-sdk (Vercel AI SDK) | `npx skills add vercel/ai` | ml-engineer |
| agent-browser (browser automation for agents) | `npx skills add vercel-labs/agent-browser` | qa-engineer, ml-engineer |

## Testing & quality

| Skill | Install | Used by agent |
|---|---|---|
| webapp-testing (unit/integration/e2e patterns) | `npx skills add anthropics/skills` | qa-engineer |
| playwright-best-practices | `npx skills add currents-dev/playwright-best-practices-skill` | qa-engineer |
| playwright-cli (official Microsoft) | `npx skills add microsoft/playwright-cli` | qa-engineer |
| test-driven-development (superpowers) | `npx skills add obra/superpowers` | qa-engineer, engineers |
| systematic-debugging (superpowers) | `npx skills add obra/superpowers` | all engineers |
| verification-before-completion (superpowers) | `npx skills add obra/superpowers` | ceo, audit-director |
| dispatching-parallel-agents / subagent-driven-development / writing-plans / executing-plans (superpowers) | `npx skills add obra/superpowers` | ceo, coo, audit-director |
| mattpocock dev-workflow pack (grill-me, grill-with-docs, handoff, tdd, to-prd, diagnose, review, qa, design-an-interface, setup-pre-commit) | `npx skills add mattpocock/skills` | tech-lead, tech-writer, product-manager |
| improve-codebase-architecture | `npx skills add mattpocock/skills` | code-auditor, tech-lead |

## Audit Office companions

| Skill | Install | Used by agent |
|---|---|---|
| web-design-guidelines (UI/a11y/UX review checklists) | `npx skills add vercel-labs/agent-skills` | ux-auditor, accessibility-auditor |
| impeccable: audit / critique / polish / optimize | `npx skills add pbakaus/impeccable` | ux-auditor, code-auditor |
| audit-website (site-wide audit) | `npx skills add squirrelscan/skills` | audit-director, seo-aso-specialist |
| firebase-security-rules-auditor | `npx skills add firebase/agent-skills` | security-auditor |

## Marketing, sales & analytics companions

| Skill | Install | Used by agent |
|---|---|---|
| copywriting / copy-editing | `npx skills add coreyhaines31/marketingskills` | copywriter |
| content-strategy | `npx skills add coreyhaines31/marketingskills` | content-marketer |
| seo-audit / programmatic-seo / ai-seo | `npx skills add coreyhaines31/marketingskills` | seo-aso-specialist |
| marketing-psychology / marketing-ideas | `npx skills add coreyhaines31/marketingskills` | cmo, marketing-strategist |
| page-cro / form-cro / onboarding-cro | `npx skills add coreyhaines31/marketingskills` | performance-marketer |
| pricing-strategy | `npx skills add coreyhaines31/marketingskills` | cro-sales |
| analytics-tracking | `npx skills add coreyhaines31/marketingskills` | product-analyst |
| posthog (product analytics) | `npx skills add posthog/skills` | product-analyst |
| remotion-best-practices (video-in-React) | `npx skills add remotion-dev/skills` | motion-designer |
| firecrawl / firecrawl-scrape / firecrawl-search | `npx skills add firecrawl/cli` | ux-researcher, marketing-strategist (competitive research) |
| notion-api | `npx skills add intellectronica/agent-skills` | coo (if the team runs on Notion) |

Protocol: agents check for these skills before deep work in their domain. Anything uncertain about current versions still gets verified via web search.
