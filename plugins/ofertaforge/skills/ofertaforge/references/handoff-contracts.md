# OfertaForge — Handoff Contracts
*Every inter-agent handoff is a small block with named fields. If a required field is missing, request it by name — never silently guess.*

## Lead Profile  *(Prospector →)*
`who · company · source/trigger · fit_score (1–5) · decision_maker? · likely_pains[] · suggested_service[] · opening_angle · outreach_variants[]`

## Scope Sheet  *(Discovery →)* — **Human Gate 1**
`client_tier · language · service[] · deliverables[] · assumptions[] · effort_hours{role:hours} · complexity (Simple/Standard/Complex) · risks[] · urgency · missing_info_questions[]`

## Market Band  *(Market Analyst →)*
`service · region/tier · currency · low · typical · high · confidence (low/med/high) · sources_or_basis · positioning_angles[2–3]`

## Price Structure  *(Pricing Engineer →)* — **Human Gate 2 — INTERNAL**
`currency · effort_hours · hourly_used · floor · target · anchor · risk_buffer · tiers{good,better,best:{scope,price}} · rationale`
*Floor and margin are INTERNAL. They never appear in client-facing text.*

## Offer Draft  *(Offer Writer →)* — **Human Gate 3 (before send)**
`language · client_name · context · scope · deliverables[] · timeline · tiers{good,better,best:price} · terms · CTA · format(email/doc)`
*Client-facing prices only — no floor, no margin, no hourly.*

## Negotiation Playbook  *(Negotiator →)*
`floor(internal) · anticipated_objections[] · responses[] · concession_ladder[] · batna · walk_line · recommended_opening`

## Follow-up Plan  *(Closer →)*
`cadence[{day,channel,message}] · scenarios{silence,stall,thinking,ready} · close_ask · hold_until_date`

## Expansion Plan  *(Upsell/Retainer →)*
`trigger_moment · retainer_pitch · recurring_packages[] · cross_sell[] · referral_ask · timing`

## Deal File  *(Deal Lead — aggregates everything)*
`situation_type · status · prior_lessons[] · {all artifacts above} · predicted_win · win_walk_recommendation · next_action_for_Fri`

## Ledger Entry  *(Ledger Keeper → the persistent ledger)*
`date · deal_slug · situation_type · tags(tier·service·complexity) · did · predicted_win · outcome(WON/LOST/GHOSTED/PENDING) · value(if WON) · worked · friction · lesson · promote(yes/no)`
*Persisted to `~/.forge/ofertaforge/LEDGER.md` (not the read-only plugin). First name + tier + service only — no PII, no floor/margin. Never fabricate an outcome.*
