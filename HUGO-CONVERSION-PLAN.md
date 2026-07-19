# Hugo Conversion Plan for Bardon Scouts Website

## Executive Summary

This plan outlines the conversion of the Bardon Scouts Gatsby v4 website to Hugo (latest stable version). The conversion will modernize the data model for Scout-appropriate content, maintain the existing design (Bulma CSS + custom branding), preserve URL structure with proper redirects, and integrate Decap CMS after the data model is updated.

**Key Objectives:**
- Convert to Hugo Extended (latest stable, ~v0.134.x)
- Build custom theme (no off-the-shelf theme)
- Improve data model for Scout organization content
- Preserve all existing URLs or provide 301 redirects
- Integrate Decap CMS after data model is established
- Maintain Netlify hosting and GitHub integration
- Preserve Bardon Scouts branding (#43a09b teal, #d9432d red)

## Current Site Analysis

**Technology Stack:**
- Gatsby v4.0.0 with React 17
- Netlify CMS for content management
- Bulma CSS framework with SASS
- Netlify hosting with GitHub repo

**Content Structure:**
- 5 page types: Landing, About, Contact Us, Thanks, Products (repurposed for Scout sections)
- 3 blog posts (demo content - to be removed)
- Markdown files with YAML frontmatter
- Complex nested frontmatter structures

**User Decisions:**
- Remove all existing blog posts (start fresh)
- Rename /products/ to /sections/ with 301 redirect
- Consolidate /contactus/ to /contact/ with redirect
- Preserve color scheme AND layout structure

## Implementation Phases

### Phase 1: Hugo Setup & Structure

**Hugo Installation:**
- Install Hugo Extended (v0.134.x or latest) for SCSS support
- Verify: `hugo version` (must show "extended")
- Create branch: `gatsby-to-hugo-conversion` (already created)

**Directory Structure:**
```
bardon-scouts-hugo/
├── archetypes/           # Content templates
├── assets/               # SCSS, JS for Hugo Pipes processing
│   ├── scss/
│   └── js/
├── content/              # All markdown content
│   ├── _index.md        # Homepage
│   ├── about.md
│   ├── contact.md
│   ├── sections/        # Scout sections
│   └── news/            # Replacement for blog
├── data/                 # YAML/JSON data files
│   ├── sections.yaml    # Meeting times/info
│   └── features.yaml    # Homepage features
├── layouts/              # Templates
│   ├── _default/
│   ├── partials/
│   └── shortcodes/
├── static/               # Static assets
│   ├── img/
│   └── admin/           # Decap CMS
├── config/               # Split configuration
│   └── _default/
├── netlify.toml
└── _redirects
```

**Configuration Approach:**
- Use `config/` directory (modern Hugo approach)
- Split files: config.toml, menus.toml, params.toml
- Environment-specific configs in config/production/

**Critical Configuration Files:**
- `config/_default/config.toml` - Main settings
- `config/_default/params.toml` - Bardon colors, contact info
- `config/_default/menus.toml` - Navigation structure

### Phase 2: Improved Data Model

**New Content Types:**

1. **Homepage** (content/_index.md)
   - Simplified frontmatter (remove coffee-shop nesting)
   - Fields: hero, mainPitch, features, contactCTA
   - Alternative: Move features to data/features.yaml

2. **Scout Sections** (content/sections/)
   - Individual files: cubs.md, scouts.md, venturers.md
   - Fields: title, ageRange, meetingDay, meetingTime, color, image, description, activities, leader, contact
   - Creates individual URLs: /sections/cubs/, /sections/scouts/

3. **News** (replacement for Blog)
   - content/news/ directory
   - Fields: title, date, featured, featuredImage, summary, tags
   - URL structure: /news/YYYY-MM-DD-slug/

4. **Events** (future enhancement)
   - content/events/ directory
   - Fields: title, date, endDate, location, sections, rsvp

5. **Simple Pages**
   - content/about.md
   - content/contact.md

**Taxonomies:**
```toml
[taxonomies]
  tag = "tags"
  category = "categories"
  section = "sections"
```

**Data Files:**
- `data/sections.yaml` - Meeting schedule for homepage display
- `data/features.yaml` - Homepage feature blurbs (optional)

### Phase 3: Theme Development

**Template Architecture:**

**Critical Templates:**
1. `layouts/_default/baseof.html` - Base template (includes head, navbar, footer)
2. `layouts/index.html` - Homepage (hero, features, sections list)
3. `layouts/_default/single.html` - Single pages
4. `layouts/sections/single.html` - Section detail pages

**Key Partials:**
- `partials/head.html` - Meta tags, CSS, SEO
- `partials/navbar.html` - Navigation with hamburger menu
- `partials/footer.html` - Footer with Bardon logo
- `partials/hero.html` - Full-width hero image
- `partials/features.html` - Feature grid (4 items)
- `partials/sections-list.html` - Scout sections display
- `partials/contact-form.html` - Netlify form

**CSS Strategy:**
- Keep Bulma framework (familiarity + existing design)
- Use Hugo Pipes for SCSS processing
- Port existing styles from `src/components/all.sass`
- Split into logical partials: _variables.scss, _navbar.scss, _footer.scss, etc.
- Asset pipeline: `{{ $scss := resources.Get "scss/main.scss" | resources.ToCSS | resources.Minify | resources.Fingerprint }}`

**JavaScript:**
- Minimal JS for navbar burger menu
- Hugo Pipes processing: resources.Get, resources.Minify, resources.Fingerprint

### Phase 4: Content Migration

**Migration Steps:**

1. **Homepage Migration**
   - Extract hero, mainPitch, features from current index.md
   - Simplify nested frontmatter structure
   - Move sections/pricing data to data/sections.yaml

2. **About Page**
   - Replace coffee content with Scout values/history
   - Keep simple markdown format

3. **Scout Sections**
   - Transform products/index.md → sections/_index.md
   - Create individual pages: cubs.md, scouts.md, venturers.md
   - Extract meeting times from "pricing" field

4. **Contact Page**
   - Consolidate contactus.md → contact.md
   - Integrate Netlify form

5. **Remove Blog Posts**
   - Delete all posts in src/pages/blog/
   - Create empty news/ directory for future content

**Image Migration:**
- Copy all images from static/img/ to Hugo static/img/
- Remove unused coffee-related images
- Organize: /img/sections/, /img/events/, /img/news/
- Use Hugo image processing for hero images (resize/optimize)

### Phase 5: URL Preservation & Redirects

**URL Mapping:**

Preserve as-is:
- `/` → `/` (homepage)
- `/about/` → `/about/`
- `/contact/` → `/contact/`
- `/blog/` → `/news/` (or keep /blog/ if preferred)

301 Redirects needed:
- `/products/` → `/sections/`
- `/contactus/` → `/contact/`
- `/thanks/` → `/contact/thanks/`
- `/contact/file-upload/` → `/contact/`
- `/contact/examples/` → `/contact/`

**Implementation: Netlify _redirects file** (recommended)

Create `static/_redirects`:
```
/products/*          /sections/:splat     301
/contactus/*         /contact/:splat      301
/thanks/             /contact/thanks/     301
/contact/file-upload /contact/            301
/contact/examples    /contact/            301
```

Alternative: Use Hugo aliases in frontmatter (creates HTML meta redirects, not true 301s)

**404 Page:**
- Create `layouts/404.html` with friendly message

### Phase 6: Decap CMS Integration

**⚠️ IMPORTANT: Integrate AFTER Phase 4 (data model established)**

**Setup:**
1. Create `static/admin/index.html` (loads Decap CMS from CDN)
2. Create `static/admin/config.yml` (content type definitions)

**Configuration:**

**Collections:**
1. **Homepage** (file collection)
2. **Scout Sections** (folder collection, create: false)
3. **News** (folder collection, create: true)
4. **Events** (folder collection, create: true)
5. **Pages** (file collection - about, contact)

**Key Features:**
- Git Gateway backend (connects to GitHub)
- Editorial workflow enabled (draft/review/publish)
- Local backend support for development
- Media folder: static/img/
- Custom fields matching Hugo data model

**Preview:**
- Hugo doesn't have built-in CMS preview like Gatsby
- Recommend: Use `hugo server` locally for preview
- Alternative: Disable preview in CMS config

### Phase 7: Forms & Features

**Netlify Forms:**

1. **Contact Form**
   - HTML form with `data-netlify="true"`
   - Honeypot field for spam prevention
   - Redirects to /contact/thanks/ on submit
   - Fields: name, email, child_names, message

2. **File Upload Form** (if needed)
   - Form with `enctype="multipart/form-data"`
   - File input field
   - Same Netlify form attributes

3. **Thank You Page**
   - Simple page at /contact/thanks/
   - Confirms form submission

**Form Testing:**
- Test in Netlify deploy preview
- Verify submissions appear in Netlify dashboard
- Configure email notifications

### Phase 8: Deployment & Testing

**Netlify Configuration:**

Create `netlify.toml`:
```toml
[build]
  publish = "public"
  command = "hugo --gc --minify"

[build.environment]
  HUGO_VERSION = "0.134.3"
  HUGO_ENV = "production"

[context.production.environment]
  HUGO_ENABLEGITINFO = "true"

[context.deploy-preview]
  command = "hugo --gc --minify --buildFuture -b $DEPLOY_PRIME_URL"
```

**Testing Checklist:**

**Content & Pages:**
- [ ] Homepage renders with hero, features, sections
- [ ] About page displays
- [ ] Contact form works
- [ ] Section pages (/sections/cubs/, etc.) work
- [ ] News section works (if implemented)
- [ ] 404 page displays

**URLs & Redirects:**
- [ ] /products/ redirects to /sections/ (301)
- [ ] /contactus/ redirects to /contact/ (301)
- [ ] /thanks/ redirects to /contact/thanks/ (301)
- [ ] All navigation links work

**Design:**
- [ ] Colors match (#43a09b, #d9432d)
- [ ] Navbar works (desktop & mobile)
- [ ] Hamburger menu toggles
- [ ] Logos display correctly
- [ ] Footer layout matches original
- [ ] Responsive breakpoints work

**Forms:**
- [ ] Contact form submits
- [ ] Submissions in Netlify dashboard
- [ ] Email notifications work
- [ ] Form validation works

**CMS:**
- [ ] Accessible at /admin/
- [ ] Authentication works
- [ ] Content editable
- [ ] Images uploadable
- [ ] Changes commit to GitHub

**Performance:**
- [ ] Images optimized
- [ ] CSS minified
- [ ] Page load < 3 seconds
- [ ] Lighthouse score > 90

**SEO:**
- [ ] Page titles correct
- [ ] Meta descriptions present
- [ ] Sitemap generated (/sitemap.xml)
- [ ] Robots.txt exists

**Launch Steps:**
1. Build locally, test with `hugo server`
2. Deploy to Netlify branch preview
3. Run full testing checklist
4. Merge to master branch
5. Monitor production deployment
6. Verify redirects working
7. Submit sitemap to Google Search Console

## Critical Files

**Files to Create (Priority Order):**

1. **config/_default/config.toml** - Main Hugo configuration
2. **layouts/_default/baseof.html** - Base template structure
3. **layouts/index.html** - Homepage template
4. **assets/scss/main.scss** - Stylesheet entry point
5. **static/admin/config.yml** - Decap CMS configuration

**Files to Reference from Gatsby Site:**

1. `/Users/hamishcurrie/dev/scouts/bardon-scouts-website/src/components/all.sass` - Complete styles to migrate
2. `/Users/hamishcurrie/dev/scouts/bardon-scouts-website/src/templates/index-page.js` - Homepage structure
3. `/Users/hamishcurrie/dev/scouts/bardon-scouts-website/static/admin/config.yml` - CMS config to adapt
4. `/Users/hamishcurrie/dev/scouts/bardon-scouts-website/src/components/Navbar.js` - Navigation structure
5. `/Users/hamishcurrie/dev/scouts/bardon-scouts-website/src/components/Footer.js` - Footer structure

## Architectural Decisions

**1. Content Model: Individual Files vs Data-Driven**
- **Decision:** Individual markdown files for Scout sections
- **Rationale:** Better SEO, easier CMS editing, individual URLs
- **Trade-off:** Slightly more complex than data files

**2. CSS Framework: Bulma vs Tailwind**
- **Decision:** Keep Bulma
- **Rationale:** Preserve existing design, minimize migration risk
- **Trade-off:** Bulma is heavier, but PurgeCSS can be added later

**3. Configuration: Single File vs Directory**
- **Decision:** Use config/ directory
- **Rationale:** Modern Hugo best practice, better organization
- **Trade-off:** Slightly more complex setup

**4. Redirects: Hugo Aliases vs Netlify**
- **Decision:** Use Netlify _redirects file
- **Rationale:** True 301 redirects (better for SEO)
- **Trade-off:** Netlify-specific, but already using Netlify

**5. Blog vs News Nomenclature**
- **Decision:** Rename to "News"
- **Rationale:** More appropriate for Scout organization
- **Trade-off:** None significant

## Additional Suggestions

**1. Analytics Integration**
- Add Google Analytics 4 or Plausible (privacy-focused)
- Track: page views, form submissions, popular content
- Configure in config/params.toml

**2. RSS Feed**
- Hugo automatically generates RSS feeds
- Customize layouts/rss.xml if needed
- Promote feed for news/updates

**3. GitHub Actions (Optional)**
- Add CI/CD pipeline for automated testing
- Run `hugo build` on pull requests
- Check for broken links, validate HTML

**4. Performance Optimization**
- Image lazy loading with Hugo built-in support
- PurgeCSS to remove unused Bulma styles
- Service worker for offline support (PWA)
- Font optimization (self-host or preload)

**5. Accessibility**
- Add ARIA labels to navigation
- Ensure color contrast meets WCAG AA
- Test with screen reader
- Add skip-to-content link

**6. Content Enhancements**
- Photo galleries using Hugo image processing
- Events calendar (Google Calendar embed or custom)
- Member resources section
- Badge tracking system (future)

**7. Security Headers**
- Add security headers in netlify.toml
- CSP (Content Security Policy)
- X-Frame-Options, X-Content-Type-Options

**8. Internationalization (Future)**
- Hugo has excellent i18n support
- Consider if multilingual content needed
- Easy to add later

## Risk Mitigation

**Potential Risks & Solutions:**

1. **Hugo Learning Curve**
   - Mitigation: Document custom functions, keep templates simple, provide examples

2. **Netlify Build Failures**
   - Mitigation: Pin Hugo version in netlify.toml, test locally first

3. **Redirect SEO Impact**
   - Mitigation: Use 301 redirects, monitor Search Console, maintain old URLs 6+ months

4. **CMS Preview Limitations**
   - Mitigation: Use editorial workflow, document Hugo server preview

5. **Form Breakage**
   - Mitigation: Test in deploy previews, use standard HTML forms

6. **Image Path Issues**
   - Mitigation: Keep images in /static/img/, maintain same paths

## Success Metrics

**Post-Launch Goals:**
- All URLs redirect correctly (100% success)
- Contact form working within 1 day
- Page load time ≤ current site
- Zero console errors
- CMS editors successful within 1 week
- Mobile responsiveness matches/exceeds current

## Future Roadmap

**Phase 9: Content Expansion**
- Photo galleries
- Events calendar
- Online join forms
- Parent resources

**Phase 10: Performance**
- Image lazy loading
- Service worker
- Font optimization
- PurgeCSS

**Phase 11: Features**
- Member portal integration
- Badge tracking
- Event RSVP system
- Newsletter integration

**Phase 12: Analytics & SEO**
- Google Analytics 4
- Search Console monitoring
- Local SEO optimization
- Content strategy

## Verification & Testing

**End-to-End Testing:**

1. **Local Development**
   - Run: `hugo server -D`
   - Access: http://localhost:1313
   - Test all pages and navigation
   - Verify responsive design

2. **Build Test**
   - Run: `hugo --gc --minify`
   - Check public/ directory
   - Verify no build errors
   - Test generated HTML

3. **Deploy Preview**
   - Push to branch
   - Netlify creates preview URL
   - Test all functionality
   - Run Lighthouse audit

4. **Production Deploy**
   - Merge to master
   - Monitor Netlify build log
   - Test production URL
   - Verify DNS/SSL

5. **Post-Launch Monitoring**
   - Check Netlify analytics
   - Monitor error logs
   - Test forms daily (first week)
   - Review Search Console

---

## Implementation Order Summary

1. **Setup:** Install Hugo, create directory structure, initialize config
2. **Templates:** Build baseof.html, index.html, partials
3. **Styles:** Port SCSS from Gatsby, set up Hugo Pipes
4. **Content:** Migrate pages, create sections, update frontmatter
5. **Redirects:** Create _redirects file, test all URLs
6. **CMS:** Configure Decap CMS, test editing workflow
7. **Forms:** Integrate Netlify forms, test submissions
8. **Deploy:** Configure Netlify, test builds, launch to production
9. **Verify:** Run full testing checklist, monitor for issues
10. **Optimize:** Address performance, SEO, accessibility

---

**Estimated Timeline:** 3-4 weeks (part-time work)
- Week 1: Phases 1-2 (setup, data model)
- Week 2: Phase 3 (theme development)
- Week 3: Phases 4-5 (content migration, redirects)
- Week 4: Phases 6-8 (CMS, forms, deployment)

This plan provides a comprehensive roadmap for converting the Bardon Scouts website from Gatsby to Hugo while modernizing the content structure and preserving the existing design and URLs.
