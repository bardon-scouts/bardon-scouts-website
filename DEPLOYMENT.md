# Deployment Guide - Bardon Scouts Hugo Site

## Pre-Deployment Checklist

### ✅ Completed
- [x] Hugo Extended v0.148.2 installed
- [x] Site builds successfully (99ms build time)
- [x] 14 pages generated
- [x] 6 URL redirects configured
- [x] 39 static files included
- [x] Decap CMS configured
- [x] Netlify forms integrated
- [x] Responsive design implemented
- [x] SEO meta tags configured

## Deployment Steps

### 1. Commit Changes to Git

```bash
# Check current status
git status

# Stage all Hugo files
git add .

# Commit the Hugo conversion
git commit -m "Convert Bardon Scouts site from Gatsby to Hugo

- Migrated to Hugo Extended v0.148.2
- Updated data model for Scout content (removed coffee shop content)
- Created individual section pages (Cubs, Scouts, Venturers)
- Configured Decap CMS for content management
- Set up URL redirects (/products → /sections, /contactus → /contact)
- Preserved Bardon branding (#43a09b teal, #d9432d red)
- Integrated Netlify forms

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push to GitHub
git push origin gatsby-to-hugo-conversion
```

### 2. Netlify Configuration

The site is already configured for Netlify deployment via `netlify.toml`:

```toml
[build]
  publish = "public"
  command = "hugo --gc --minify"

[build.environment]
  HUGO_VERSION = "0.148.2"
  HUGO_ENV = "production"
```

### 3. Deploy to Netlify

**Option A: Deploy Preview (Recommended First)**

1. Push branch to GitHub
2. Netlify will automatically create a deploy preview
3. Test all functionality on the preview URL
4. Review the deploy preview checklist below

**Option B: Deploy to Production**

1. Create Pull Request from `gatsby-to-hugo-conversion` to `master`
2. Review changes in GitHub
3. Merge PR to master
4. Netlify auto-deploys to production

### 4. Post-Deployment Verification

After deployment, verify:

**URLs & Redirects:**
- [ ] https://bardonscouts.org.au/ (homepage)
- [ ] https://bardonscouts.org.au/about/
- [ ] https://bardonscouts.org.au/sections/
- [ ] https://bardonscouts.org.au/sections/cubs/
- [ ] https://bardonscouts.org.au/sections/scouts/
- [ ] https://bardonscouts.org.au/sections/venturers/
- [ ] https://bardonscouts.org.au/contact/
- [ ] https://bardonscouts.org.au/products/ → redirects to /sections/ (301)
- [ ] https://bardonscouts.org.au/contactus/ → redirects to /contact/ (301)
- [ ] https://bardonscouts.org.au/thanks/ → redirects to /contact/thanks/ (301)

**Forms:**
- [ ] Contact form submits successfully
- [ ] Form submissions appear in Netlify dashboard
- [ ] Email notifications working

**Design:**
- [ ] Bardon colors correct (#43a09b, #d9432d)
- [ ] Scouts Australia logo displays with white background
- [ ] Hero text: "Bardon Scouts" / "Get ready for adventure"
- [ ] Navbar hamburger menu works on mobile
- [ ] Footer displays correctly

**CMS:**
- [ ] Admin accessible at https://bardonscouts.org.au/admin/
- [ ] Git Gateway authentication configured
- [ ] Content editable through CMS
- [ ] Editorial workflow enabled

**SEO:**
- [ ] Sitemap at https://bardonscouts.org.au/sitemap.xml
- [ ] Meta descriptions present
- [ ] OpenGraph tags configured
- [ ] Canonical URLs set

## Netlify CMS Setup

### Enable Git Gateway

1. Go to Netlify dashboard → Site settings → Identity
2. Click "Enable Identity"
3. Under "Registration preferences", select "Invite only"
4. Under "Services → Git Gateway", click "Enable Git Gateway"

### Invite Users

1. Go to Identity tab
2. Click "Invite users"
3. Enter email addresses for content editors
4. Users will receive invitation emails

### Access CMS

Content editors can access:
- Production: https://bardonscouts.org.au/admin/
- Local: http://localhost:8080/admin/ (with `npx decap-server`)

## Local Development

### Start Hugo Server

```bash
# Development server with drafts
hugo server -D

# Production-like server
hugo server
```

### Start Decap CMS Local Backend

```bash
# In separate terminal
npx decap-server

# Then access http://localhost:8080/admin/
# Click "Work with local repository"
```

### Build for Production

```bash
# Clean build
hugo --gc --minify

# Output in public/ directory
```

## Environment Variables

No environment variables required for basic deployment.

Optional (set in Netlify dashboard if needed):
- `HUGO_VERSION=0.148.2` (already in netlify.toml)
- `HUGO_ENV=production` (already in netlify.toml)

## Troubleshooting

### Build Fails on Netlify

**Issue:** Hugo version mismatch
**Solution:** Verify `netlify.toml` specifies Hugo Extended v0.148.2

**Issue:** CSS not loading
**Solution:** Check Bulma CDN is accessible from production

### Forms Not Working

**Issue:** Form submissions not appearing
**Solution:**
1. Verify form has `data-netlify="true"`
2. Check Netlify Forms tab in dashboard
3. Ensure form name matches hidden field

### CMS Not Accessible

**Issue:** 401/403 errors
**Solution:**
1. Enable Identity in Netlify
2. Enable Git Gateway
3. Invite users via Identity tab

### Redirects Not Working

**Issue:** Old URLs return 404
**Solution:**
1. Verify `_redirects` file in public/ directory
2. Check Netlify deploy log for redirect rules
3. Test with curl: `curl -I https://bardonscouts.org.au/products/`

## Rollback Plan

If issues occur after deployment:

1. **Immediate:** Revert in Netlify
   - Go to Deploys tab
   - Find previous working deploy
   - Click "Publish deploy"

2. **Git-based:** Revert commit
   ```bash
   git revert HEAD
   git push origin master
   ```

3. **Branch switch:** Deploy old branch
   - In Netlify: Site settings → Build & deploy
   - Change branch from master back to previous

## Performance Benchmarks

**Build Time:** ~100ms
**Pages:** 14
**Static Files:** 39
**Bundle Size:** ~50KB (minified CSS + JS)

## Support

**Hugo Documentation:** https://gohugo.io/documentation/
**Decap CMS Documentation:** https://decapcms.org/docs/
**Netlify Documentation:** https://docs.netlify.com/

## Next Steps After Deployment

1. **Monitor:** Check Netlify analytics for first 24 hours
2. **Test Forms:** Submit test form to verify email delivery
3. **Train Editors:** Provide CMS training to content editors
4. **Content Update:** Create first Scout news post via CMS
5. **SEO:** Submit sitemap to Google Search Console
6. **Backup:** Ensure GitHub backups are working
