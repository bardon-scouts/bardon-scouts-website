# Bardon Scouts website principles

- **Parents first.** Most readers are parents of current or prospective members. Lead with what they need: what it is, when, where, who it's for, cost, and how to join.
- **Accurate, not impressive.** Only publish details a leader can vouch for. If something isn't confirmed, say so or link to the official source instead of filling the gap.
- **Short and specific.** Pages cover what a parent needs, once.
- **Bullets for genuine lists only.** Use bullet points for real lists of items: what to bring, steps, dates, links. When a list is really a set of topics, give each a short heading or paragraph that stands on its own.
- **Protect families from scams.** Never publish payment methods, bank details, invoice timing or payment deadlines. Scammers time fake invoices to match real ones. Bardon Scouts' own Stripe links (e.g. fundraiser orders) are the exception: families can check them against this site.
- **Don't publish leaders' contact details.** Parents get them when they join, so pages can say to email or call their Section Leader without giving them. Everyone else uses the contact form.
- **Use the Scouts Queensland section names:** Joey Scouts, Cub Scouts, Scouts, Venturer Scouts, Rover Scouts. Never "Joeys" or "Cubs" on their own.
- **Leaders can maintain it.** Every page and data file must be editable in Sveltia CMS, so leaders without technical skills can keep it current.
- **Check before publishing.** Work on `dev`, check changes on the dev site, and publish by merging `dev` into `master`.

## Constraints

Limits we chose on purpose. Work stays inside them: if a task would break one, ask on the issue.

- **Static site, no server code:** nothing to run, patch or secure.
- **Netlify forms only:** no other form service to manage.
- **Scouts Queensland branding:** the site should look part of Scouts Queensland.
- **Bardon Scouts information only:** Scouts Queensland and Scouts Australia cover wider scouting, so link to them.
