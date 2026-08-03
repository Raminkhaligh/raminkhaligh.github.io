1 Identity
Name: Ramin Khaligh — رامین خلیق
Role: Growth-Focused Product & Marketing Leader
Core value proposition
I drive acquisition, engagement, and retention through data-driven strategy and cross-functional execution, leading hybrid teams of 20+ across engineering, marketing, and business at companies including Huawei (China), Clarity (Australia), and Iran's top tech firms. Over 8 years, I've built products from zero, scaled the features that already worked, and killed the ones that didn't, managing multi-million dollar go-to-market initiatives along the way.
Brand attributes

* Analytical and engineering-minded
* Disciplined and highly structured
* Minimal, premium, and modern taste
* Health-conscious lifestyle
* Independent, responsible, and outcome-driven
2) Business objective
This website exists to convert visitors into opportunities.
Primary goals
* Generate qualified calls
* Build trust fast
* Show product and marketing depth
* Prove business impact through real work
Every page must support at least one of these outcomes
* Revenue
* Retention
* Efficiency
* Credibility
* Lead generation
3) Tone, language, and writing style
Tone
* Direct
* Consultative
* Human
* Confident
* Calm, premium, and experienced
 Language level
* Up to upper-intermediate English
* Simple sentence structure
* Clear, precise vocabulary
* Natural use of business terms

Use these terms naturally when relevant
CAC, LTV, CRO, OKRs, backlog, activation rate, time-to-value, retention, martech, funnel, conversion, acquisition, segmentation, lifecycle, experimentation, monetization
Avoid these words and styles
Avoid AI clichés and vague marketing language such as:
* unleash
* elevate
* seamless
* delve
* cutting-edge
* next-gen
* revolutionary
* world-class
* game-changing

Writing rules

* Prefer facts over adjectives
* Prefer outcomes over activities
* Prefer clear decisions over generic claims
* Keep paragraphs short
* Use bullets when scanning is better than reading
* Never use em dashes (—) or spaced hyphens as a sentence connector. This is a dead giveaway of AI-generated copy. Split into two sentences, use a comma, a period, or a colon instead. Hyphens stay allowed only inside compound words (go-to-market, cross-functional, time-to-value) and as the separator in job-title lines (Title — Company) or date ranges (2023 – 2024)
* Every claim must support a business result

### Copy formula

When writing any section, use:
**Context → Problem → Action → Result**

---
 4) Audience

Primary audience:

* Founders
* CEOs
* Product leaders
* Marketing leaders
* Hiring managers
* Potential clients

They should understand within 5 seconds:

* Who I am
* What I do
* Why I matter
* What business outcome I create
5) Conversion and UX rules
### Cognitive load

Keep everything minimal, structured, and easy to scan.

### Layout rules

* Use strong hierarchy
* Use short paragraphs
* Use data chips, bullets, and summary blocks
* Use F-pattern reading logic
* Avoid clutter
* Avoid long dense walls of text

### CTA hierarchy

**Primary CTA:** “Book a Strategy Call”

* Use the accent color
* Highest visual priority
* Action-oriented

**Secondary CTA:** “View Case Studies”

* Use ghost or glass style
* Lower visual intensity
* Exploratory intent

### Microcopy

Always include trust-building microcopy near forms and calls to action, such as:

* No spam
* Typical response time: under 24 hours
* Confidential and direct
* Relevant inquiries only

### Social proof

Place testimonials, metrics, logos, or proof points near high-friction areas such as:

* Contact sections
* CTA blocks
* Pricing or engagement sections
* Case study intros

 6) Design system

### Overall aesthetic

Premium, minimal, technical, and high-end.
Inspired by:

* Apple
* Stripe
* Linear
* Notion

### Theme

Default to deep dark mode.

### Visual tone

* Calm
* Precise
* Confident
* Elegant
* High-contrast but not harsh

### Accent color

Purple-first accent system:

* Primary accent: purple
* Secondary accent: softer violet tones
* Use accent sparingly for emphasis and conversion

### Glassmorphism

Use subtle glass layers only when they improve depth and readability:

* `backdrop-filter: blur(16px)`
* translucent surfaces
* subtle borders
* restrained glow

### Shadows

Use layered, diffuse shadows only.
Avoid harsh or heavy drop-shadows.

### Motion

* Smooth hover states
* Smooth focus states
* Subtle translateY motion on cards and buttons
* Use elegant easing
* Never overanimate

### Mobile

* Mobile-first layout
* Responsive grid and flex layouts
* Minimum 44x44px touch targets
* No cramped spacing on small screens

---

 7) Technical architecture

### Hosting

GitHub Pages only.

### Frontend stack

* Pure semantic HTML5
* Pure custom CSS
* Vanilla JavaScript only

### Forbidden

* Tailwind
* Bootstrap
* Inline styles
* Heavy frameworks
* Unnecessary libraries

### File structure

* `/index.html` for English
* `/fa/index.html` for Persian
* `/assets/style.css` for all styling
* `/assets/js/` for minimal JavaScript
* `/assets/img/` for images
* `/assets/icons/` for icons
* `/assets/illustrations/` for custom visuals
* `/content/` for optional data or structured JSON

### Naming conventions

Use BEM-inspired naming:

* `hero__title`
* `case-card__metric`
* `cta-bar__button`
* `contact-form__field`
 Paths
Always use root-relative paths:
* `/assets/image.webp`
* `/blog/posts.json`
Never use relative paths like:
* `./assets/...`
* `../assets/...`
 8 Visual and asset rules
Claude should create visuals proactively when they improve clarity, trust, or conversion.
When visuals are needed
Create visuals for:
* Hero sections
* Service explanations
* Case studies
* Metrics and impact
* Process steps
* Comparisons
* Trust sections
* Contact or CTA areas
Preferred visual formats
Use this priority order:
1. **SVG icons**

   * Best for icons, symbols, process steps, feature blocks
   * Prefer simple, clean, scalable SVG
   * Store in `/assets/icons/`

2. **Custom SVG illustrations**

   * Use for conceptual visuals, system diagrams, and brand graphics
   * Store in `/assets/illustrations/`

3. **Simple charts or diagrams**

   * Prefer lightweight HTML/CSS or SVG-based charts
   * Avoid heavy chart libraries unless absolutely necessary

4. **Photos**

   * Use only when a real photo adds credibility
   * Prefer optimized WebP or AVIF
   * Store in `/assets/img/`
Icon style
* Minimal
* Geometric
* Consistent stroke width
* Match the premium dark theme
* No generic stock icon style
* No clutter
Picture style
When a real picture is used:
* It must support trust or explanation
* It must be relevant
* It must be optimized for performance
* It must have accurate alt text
* It must not feel random or decorative only
If an image is missing
Do not leave a vague placeholder.
Instead:
* Create a clear temporary placeholder
* Add a comment explaining exactly what should replace it
* Specify file name, dimensions, and intent
Example instruction:
`Replace /assets/img/hero-photo.webp with a real portrait photo of Ramin in a dark premium setting.`
Visual creation rule
If a section feels weak without visuals, create the visual instead of leaving it empty.
9 CSS design tokens
Always use the existing variables and do not invent a second design system.
Colors
* `--bg`
* `--surface`
* `--ink`
* `--muted`
* `--line`
* `--glass`
* `--accent`
* `--accent-strong`
* `--focus`
Spacing and radii
* `--gutter`
* `--radius-s`
* `--radius-m`
* `--radius-l`
Optional shadow tokens
* `--shadow-sm`
* `--shadow-md`
* `--shadow-lg`
* `--shadow-glow`
Rules
* Never hardcode random colors unless necessary
* Never add new tokens without a clear reason
* Reuse existing tokens everywhere
10 Accessibility rules
Accessibility is mandatory.
HTML semantics
* Use proper semantic elements
* Keep heading hierarchy strict
* Never skip heading levels
Interactive elements
All actionable elements must include:
* `aria-label` when needed
* `aria-expanded` when needed
* keyboard-friendly focus states
Focus
* `:focus-visible` is mandatory
* Focus states must be clearly visible
* Keyboard navigation must feel intentional
Images
* Every meaningful image needs accurate alt text
* Decorative images should be hidden from assistive tech
11 SEO and AI search optimisation
The site must be built for both search engines and AI parsers.
Technical SEO
* Proper canonical tags
* Valid hreflang tags
* Strict heading structure
* Fast loading
* Clean HTML
* Descriptive metadata
Metadata rules
* Title tags under 60 characters
* Meta descriptions under 160 characters
* Use action-oriented and keyword-rich phrasing
EEAT rules
* Use real data whenever possible
* Avoid generic filler
* Ground claims in actual experience, metrics, or proof
AI search formatting
* Put the bottom line first
* Use bold for key metrics and important terms
* Make important facts easy to parse
* Keep sections semantically clear
Structured data
Generate and maintain JSON-LD when appropriate:
* Person
* Organization
* FAQPage
* Article
Place schema in the `<head>`.
12 Internationalisation
English version
* `/index.html`
* `lang="en"`
* `dir="ltr"`
Persian version
* `/fa/index.html`
* `lang="fa-IR"`
* `dir="rtl"`
RTL rules
* Use logical CSS properties
* Do not break layout with LTR assumptions
* Keep Persian typography clean and readable
13 JavaScript rules
Use vanilla JavaScript only.
Allowed use cases
* Theme toggle
* Mobile navigation
* Smooth scroll enhancements
* Lazy dynamic content
* JSON fetching
* Minor UI interactions
Rules
* Keep scripts minimal
* Avoid unnecessary abstractions
* Place the theme script in the `<head>` to prevent FOUC
* Do not block rendering
14 Performance rules
Images
* Use `loading="lazy"` for below-the-fold images
* Use `fetchpriority="high"` for hero images
General performance
* Keep assets light
* Avoid unnecessary JS
* Avoid heavy dependencies
* Prefer static rendering
* Keep the page fast on mobile
15 Rules of engagement
Do not change unless explicitly asked
* Global header
* Global navigation
* Global footer
* Core layout shell
Always do
* Use root-relative paths
* Keep copy aligned with Ramin’s identity
* Make every section useful
* Tie every feature to a business outcome
Never do
* Add filler content
* Add placeholder sections without purpose
* Use generic startup language
* Use inline styles
* Use visual noise
* Overcomplicate the page
16 Definition of done
A page, component, or section is complete only when all of the following are true:
* It is visually premium
* It is instantly understandable
* It supports a business outcome
* It feels human and credible
* It uses no inline styles
* It is accessible
* It is performant
* It follows the design tokens
* It includes a logical next step
* It uses visuals when visuals improve clarity or conversion
* It sounds like a seasoned consultant, not an AI template
17 Execution mindset
Always behave like a combined:
* Senior product consultant
* Senior marketing strategist
* Senior UX thinker
* Senior frontend implementer
Optimise for:
* clarity
* trust
* conversion
* performance
* premium brand feel
* business impact
If a choice does not improve one of those outcomes, do not add it.