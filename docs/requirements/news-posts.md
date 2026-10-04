# News posts

## What it's for

Short posts about what the group has done or is about to do (results, thank-yous, fundraisers, repairs to the den), listed on the News page.

## Requirements

### The post

- Lives at `content/news/YYYY-MM-DD-<slug>.md` and is served at `/news/YYYY-MM-DD-<slug>/`. The URL comes from the file name, so don't rename a published post.
- Front matter:
  - `title`
  - `date`: sets the date shown on the post and its place in the listing
  - `summary`: one or two sentences, shown in the listing and in bold at the top of the post
  - optional: `featuredImage` (shown in the listing and at the top of the post), `tags` (shown on the post)
- Doesn't repeat the title as the first heading, and follows the content standards and principles like any other page.
- A post with a `date` in the future isn't published. The site doesn't rebuild on its own, so it only appears at the first deploy after that date.

### Where posts appear

- The News page, `/news/`, lists every post, newest `date` first, 10 to a page with Previous and Next links. Each entry shows the title, date, summary, featured image if there is one, and a "Read more" link.
- The News page is in the main menu and the footer.
- Posts aren't shown on the home page.

### Adding a post in the CMS

Leaders add posts in the CMS under **News** ("New News"), which creates the file in `content/news/` with the date in its name. Fill in the title, date and summary. The CMS's `featured` checkbox isn't used by the site.

## How to check

On the dev site:
- **NP-1:** The post returns 200 at `/news/YYYY-MM-DD-<slug>/` and shows the title, date and summary.
- **NP-2:** `/news/` lists the post, with every post in order of `date`, newest first.
- **NP-3:** The dev site's `/admin/config.yml` has the `news` folder collection for `content/news`.
