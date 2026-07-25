# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bardon Scouts website - a static site built with Hugo and Sveltia CMS, deployed on Netlify. Recently converted from Gatsby to Hugo for faster builds (300-600x improvement) and simpler content management.

**Tech Stack:** Hugo Extended v0.148.2, Bulma CSS v1.0.2, Sveltia CMS, Netlify

**Branch Context:** Currently on `gatsby-to-hugo-conversion` branch (main branch is `master`)

## Development Commands

### Local Development
```bash
# Start Hugo development server (with drafts)
hugo server -D

# Start Hugo server (production-like)
hugo server

# Alternative npm scripts
npm run dev     # hugo server -D --disableFastRender
npm start       # hugo server -D
```

### CMS Development
```bash
# Sveltia CMS can work with local git directly (no separate server needed)
# Access http://localhost:1313/admin/ (or dev server port) and login with GitHub

# For local-only testing without GitHub, you can still use the legacy backend:
npx @sveltia/cms-auth@latest
# Then set local_backend: true in config.yml
```

### Building
```bash
# Production build (same as Netlify)
hugo --gc --minify

# Clean build artifacts
npm run clean   # removes public/ and resources/
```

### Deployment
- **Deploy Preview:** Push to any branch - Netlify auto-creates preview
- **Production:** Merge to `master` - Netlify auto-deploys
- **Build Command:** `hugo --gc --minify` (configured in netlify.toml)
- **Hugo Version:** 0.128.2 (Netlify), 0.148.2 (local development)

## Architecture

### Hugo Site Structure

This is a **custom Hugo theme** (not an off-the-shelf theme) with the following architecture:

```
content/              # Markdown content files
├── _index.md         # Homepage content
├── about.md          # About page
├── contact.md        # Contact page
├── sections/         # Scout sections (Cubs, Scouts, Venturers)
│   ├── cubs.md
│   ├── scouts.md
│   └── venturers.md
└── news/             # News posts (managed via CMS)

layouts/              # Hugo templates
├── _default/
│   ├── baseof.html   # Base template (HTML shell)
│   └── single.html   # Generic single page template
├── sections/
│   └── single.html   # Scout section page template
├── partials/         # Reusable template components
│   ├── head.html     # SEO, meta tags, CSS
│   ├── navbar.html   # Navigation
│   ├── footer.html   # Footer
│   ├── hero.html     # Hero image sections
│   ├── features.html # Feature grid
│   ├── sections-list.html  # Scout sections display
│   └── contact-form.html   # Netlify form
├── index.html        # Homepage template
└── 404.html          # Error page

data/                 # YAML data files
├── features.yaml     # Homepage features (4 items)
└── sections.yaml     # Meeting schedule for homepage

static/               # Static assets (copied to public/)
├── img/              # Images
├── admin/            # Sveltia CMS configuration
│   ├── config.yml    # CMS schema
│   └── index.html    # CMS entry point
└── _redirects        # Netlify URL redirects

assets/               # Processed by Hugo Pipes
├── scss/             # SCSS files (compiled to CSS)
└── js/               # JavaScript (minified)

config/_default/      # Hugo configuration
├── config.toml       # Main config (baseURL, markup settings)
├── params.toml       # Site parameters (colors, contact info)
└── menus.toml        # Navigation menu structure
```

### Content Model

**Scout Sections:** Each section (Cubs, Scouts, Venturers) has:
- Individual page in `content/sections/`
- Frontmatter: `sectionName`, `ageRange`, `meetingDay`, `meetingTime`, `activities[]`, `leader`, `contact`
- Custom template: `layouts/sections/single.html`
- Cannot be created/deleted via CMS (only edited)

**Homepage:**
- Managed in `content/_index.md`
- Hero section with image/heading/subheading
- Main pitch section (Why Join Scouts?)
- Features pulled from `data/features.yaml`
- Sections list pulled from `data/sections.yaml`

**Pages (About, Contact):**
- Simple markdown files with optional hero images
- Contact page has `showForm` parameter to toggle Netlify form

**News & Events:**
- Managed entirely through Sveltia CMS
- Support for featured posts, tags, images
- Events support multiple sections, RSVP, date ranges

### Styling & Design

**Bardon Brand Colors:**
- Primary Teal: `#43a09b`
- Primary Red: `#d9432d`
- Defined in `config/_default/params.toml`

**CSS Framework:**
- Bulma v1.0.2 loaded from CDN (see `layouts/partials/head.html:15`)
- Custom SCSS in `assets/scss/` compiled via Hugo Pipes
- Variables in `assets/scss/_variables.scss`
- Component styles: `_navbar.scss`, `_sections.scss`, `_hero.scss`, etc.

**JavaScript:**
- Minimal JS for navbar burger menu toggle
- Located in `assets/js/main.js`
- Minified and fingerprinted via Hugo Pipes

### URL Structure & Redirects

**Current URLs:**
- `/` - Homepage
- `/about/` - About page
- `/sections/` - Scout sections index
- `/sections/cubs/`, `/sections/scouts/`, `/sections/venturers/` - Individual sections
- `/contact/` - Contact form
- `/news/` - News listing
- `/admin/` - Sveltia CMS

**Redirects (from Gatsby conversion):**
- `/products/*` → `/sections/:splat` (301)
- `/contactus/*` → `/contact/:splat` (301)
- `/thanks/*` → `/contact/thanks/:splat` (301)

Configured in `static/_redirects` for Netlify

### Sveltia CMS Configuration

**Collections** (in `static/admin/config.yml`):
1. **Homepage** - Edit hero, main pitch, contact CTA
2. **Scout Sections** - Edit Cubs/Scouts/Venturers (create: false)
3. **News** - Create/edit news posts
4. **Events** - Create/edit Scout events
5. **Pages** - Edit About and Contact pages
6. **Homepage Features** - Edit 4 feature blurbs (data/features.yaml)
7. **Sections Schedule** - Edit meeting times (data/sections.yaml)

**Editorial Workflow:** Draft → Review → Ready (publish_mode: editorial_workflow)

**Local Backend:** Enabled - Sveltia CMS works with local git directly (no separate server needed for most use cases)

**Media Management:** Files uploaded to `static/img/`, referenced as `/img/...`

## Important Notes

### When Editing Content

- **Scout Section Pages:** Never delete the three section files (cubs.md, scouts.md, venturers.md) - CMS configured with `create: false`
- **Frontmatter:** Scout sections use structured frontmatter (sectionName, ageRange, activities list, etc.) - maintain this schema
- **Data Files:** Features and sections in `data/` are managed via CMS - avoid manual editing
- **Images:** Always place in `static/img/` for CMS compatibility

### When Editing Templates

- **Base Template:** All pages inherit from `layouts/_default/baseof.html`
- **Partials:** Shared components in `layouts/partials/` - used across multiple templates
- **Hugo Pipes:** SCSS/JS processed via Hugo Pipes - don't reference directly, use `.Permalink` and `.RelPermalink`
- **Bulma Classes:** Site uses Bulma CSS - consult https://bulma.io/documentation/ when styling

### When Editing Styles

- **SCSS Entry Point:** `assets/scss/main.scss` imports all other SCSS files
- **Variables:** Always use Bardon brand colors from `_variables.scss`
- **Compilation:** Hugo Pipes compiles SCSS on-the-fly - no separate build step needed
- **Custom Styles:** Add component-specific styles in separate `_component.scss` files

### Netlify Configuration

- **Build Command:** `hugo --gc --minify` (configured in netlify.toml)
- **Hugo Version:** 0.128.2 for Netlify compatibility (extended version)
- **Forms:** Use `data-netlify="true"` attribute - see `layouts/partials/contact-form.html` for reference
- **Redirects:** Netlify reads `static/_redirects` file automatically
- **Identity:** Required for Sveltia CMS authentication in production (GitHub OAuth configured)

### Common Gotchas

- **Hugo Version:** Netlify uses 0.128.2 (specified in netlify.toml) - local may differ
- **Draft Content:** Content with `draft: true` only shows with `hugo server -D`
- **URL Trailing Slashes:** Hugo generates `/about/index.html` - always link to `/about/` with trailing slash
- **Asset Fingerprinting:** CSS/JS URLs change with content - Hugo handles automatically
- **CDN Dependencies:** Bulma loaded from CDN - internet required for local development

## Migration Context

This site was recently converted from Gatsby v4 to Hugo. Key changes:
- Removed all Gatsby/React dependencies
- Simplified content model (removed GraphQL layer)
- Migrated from Decap CMS to Sveltia CMS (drop-in replacement, same config)
- Preserved all URLs with 301 redirects
- Improved build times from 30-60s to ~100ms

See `CONVERSION-SUMMARY.md` for full migration details.

## Node.js Requirements

**Minimum Version:** 14.15.0 (specified in package.json)
**Current Version:** 18.20.0 (specified in netlify.toml)

Node.js not required for Sveltia CMS (works directly with git) - Hugo itself doesn't require Node either.
