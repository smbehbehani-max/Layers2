# LAYERS autopilot: set-up and daily use

## What it does

**Every Sunday (automatic):**
1. Looks for new papers about the six Arab Gulf countries in OpenAlex, a free index of research papers.
2. Claude reads each new paper and drafts a map record **only if the paper itself gives the site's coordinates**. Relevant papers without coordinates are listed as *leads* for you.
3. Drafts up to 3 **AI hypotheses** that link nearby places from different layers.
4. Checks 30 random reference links and lists the broken ones.
5. Runs the automatic checks: the location is inside the right country, the quoted coordinates match, it is not a duplicate, a reference exists, the names are right and the Arabic characters are clean.
6. Opens a **pull request** (a review page on GitHub) and you get a notification.

**When you approve (merge the pull request):**
- The approved records are added to the map. Records that fail the checks are never added.
- Every edition is rebuilt and the website is published automatically.

**AI hypotheses** are saved as drafts in `autopilot/review/done/`. To add one to the app, ask Claude to turn it into a hypothesis entry. They are never added automatically.

## Optional: fully automatic publishing

Two safety layers run on every draft before anything can be published:
1. **Rule checks.** These test the location, the coordinates, duplicates, the source, the names and the Arabic.
2. **The goldfish reviewer.** A second, independent Claude review. It never saw how the record was written. It gets only the paper and the draft, and it fails any claim the paper does not state. This is the "review with a goldfish" idea.

If you set the variable `AUTO_PUBLISH` to `true`, a weekly run publishes **by itself only when every record passes both layers with no warnings at all**. Anything doubtful still waits for you. AI hypotheses are always drafts.

Auto-publish stays **on hold until 8 January 2027** (after the award judging). Change this with the variable `HOLD_UNTIL`.

Every automatic publish leaves a comment on the review page. You can undo it by reverting the merge.

## One-time set-up (about 20 minutes)

1. **Get an API key.** At console.anthropic.com, create an API key and set a **monthly spending limit** (for example 10 USD). The weekly run uses a few dollars a month at most with the default caps.
2. **Put the source in your repository.**
   - Install **GitHub Desktop** and clone your `Layers` repository.
   - Inside that folder, delete the old website files but keep the hidden `.git` folder.
   - Unzip `layers-github-repo.zip` into the folder.
   - In GitHub Desktop, **Commit** and then **Push**.
3. **Point Pages at the website.** In the repository, open **Settings → Pages** and set **Source** to **Deploy from a branch**. Choose branch **main** and folder **/docs**, then **Save**. The finished website lives in `docs/`, and the autopilot refreshes it after every approved update.
4. **Allow the workflows to work.** Open **Settings → Actions → General**. Under *Workflow permissions*, choose **Read and write permissions** and tick **Allow GitHub Actions to create and approve pull requests**.
5. **Add the key.** Open **Settings → Secrets and variables → Actions**.
   - Under *New repository secret*, set the name to `ANTHROPIC_API_KEY` and paste your key.
   - Optional *Variables*:
     - `CONTACT`: your e-mail, which OpenAlex prefers so it can contact you.
     - `SITE_URL`: only if you move to your own domain (the default is `https://smbehbehani-max.github.io/Layers2/`).
     - `MAX_PAPERS`: default 20.
     - `MAX_HYP`: default 3.
6. **First run.**
   - Your site works straight away from `docs/`.
   - Then run **Weekly research** once to see a first review.
7. **Notifications on your phone.** In the GitHub app, open the repository and choose **Watch → All activity**.

## Reviewing on your phone

Open the pull request in the GitHub app.
- **Approve:** if everything looks right, tap **Merge**. The site updates within about 10 minutes.
- **Fix a draft:** open *Files changed*, edit the JSON (change a value or delete a record), then merge.
- **Reject:** close the pull request.
- **Checks:** a red ✗ on the pull request means a record failed the checks. That record will not be added even if you merge. Fix it or delete it.

## Safety

- **Undo:** every change is a git commit. Use *Revert* in GitHub Desktop or on the commit page.
- **Pause:** in the Actions tab, open a workflow and choose **⋯ → Disable workflow**. It is wise to merge carefully, or pause, while the awards are being judged (late Nov to Jan).
- **Kuwait:** new Kuwait finds appear as leads only, because Kuwait is the hand-curated home edition.
