# LAYERS autopilot: rules for any person or AI that extends it

Goal: keep LAYERS growing from new published research, while every public change stays checked and approved by the owner.

1. **Approval before publishing.** Software and AI may search, read, draft, check and suggest. A change reaches the public site only when the owner merges it, or (if the owner switched on AUTO_PUBLISH) when every record passes all rule checks and the independent goldfish review with no warnings. AI hypotheses always need the owner.
2. **Published sources only.** Every record cites a real publication. A location must be quoted from that publication (or an official listing) and stored in `coordinate_quote`. Never estimate, average or invent a coordinate, date, number or reference.
3. **Findings, interpretations and hypotheses stay separate.** AI hypotheses are drafts for the owner. They are labelled as ideas, never facts, and are never added to the app automatically.
4. **Allowed sources.** Use official APIs and open sources whose terms allow automated access (OpenAlex, Crossref, UNESCO, Protected Planet, government open data). No scraping of sites that forbid it.
5. **Naming and neutrality.** The sea is the Arabian Gulf (الخليج العربي); the countries are the Arab Gulf countries (دول الخليج العربي). No political or border claims.
6. **Keep it simple.** The site stays a static website built by GitHub Actions. Add a database, cloud functions or other paid services only when a clear need is shown and the owner agrees.
7. **Not in scope for now:** satellite or landscape-change analysis, collecting visitors' e-mails or personal data, automatic edits to existing records.
8. **Traceability.** Every added record keeps `source_paper`, `added` (date) and `review` (which approval added it). Git history keeps every change and can undo it.
9. **Costs.** AI calls are capped per run (MAX_PAPERS, MAX_HYP). The owner sets a monthly spending limit in the Anthropic console.
