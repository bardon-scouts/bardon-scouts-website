# Forms

## What it's for

The contact, website feedback, complaints and Den hire enquiry forms: how parents and others reach the group. A broken form fails silently, so these rules say what each form must have and how to check it without sending a real submission.

## Requirements

### Every form

- Is a Netlify form: `data-netlify="true"`, a `name`, `method="post"`, and a hidden `form-name` field with the same name. The form lives in a partial in `layouts/partials/` and is turned on by a front matter flag on its page.
- Has spam protection: the `bot-field` honeypot (`data-netlify-honeypot="bot-field"`) in a hidden field.
- Sends the visitor to its own thanks page (the form's `action`), which exists in `content/`.
- Never asks for payment details, bank details, passwords or other sensitive information.
- Submissions are emailed to a group role mailbox, never a leader's personal address. This is set in Netlify (site settings, Forms, form submission notifications), not in the code.

### The forms

| Form (`name`) | Page | Flag | Thanks page | Fields (* required) |
|---|---|---|---|---|
| `contact` | `/contact/` | `showForm` | `/contact/thanks/` | name\*, email\*, child_names (optional, so volunteers without a child at the group can use it; #84), message\* |
| `website-feedback` | `/website-feedback/` | `showFeedbackForm` | `/website-feedback/thanks/` | name\*, email, page\*, feedback_type\* (a list), details\* |
| `complaints` | `/complaints/` | `showComplaintsForm` | `/complaints/thanks/` | name\*, email\*, phone, complaint_type\* (a list), when_occurred\*, details\*, preferred_contact\* (Email, Phone or Either) |
| `hire-enquiry` | `/hire-the-den/` | `showHireForm` | `/hire-the-den/thanks/` | name\*, organisation\*, email\*, phone, hire_dates\*, details |

Netlify registers a form's fields when it first sees the form in a deploy. If fields are renamed, check Netlify's form list shows the new names.

## How to check

On the dev site, without sending a submission:
- **FM-1:** Each form page returns 200 and has its processed form: Netlify replaces `data-netlify` with a hidden `form-name` input whose value is the form's name. The whole-site check (`scripts/site_check.py`) does this for all four.
- **FM-2:** Each form has the hidden `bot-field` input, and its `action` is its thanks page.
- **FM-3:** Each thanks page returns 200.
- **FM-4:** The fields and required flags match the table above.
- **FM-5:** In Netlify (site settings, Forms), each form is listed with the fields above, and the submission notification goes to a group role mailbox.

Sending a test submission is a manual check (see `docs/testing/README.md`).
