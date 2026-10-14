# Publishing the privacy / support pages (Crave Harbor, Pill Window, Stepsmith)

Prepared 2026-10-14. **Nothing has been published.** No commit, no push and no account was created.

## What already exists (found in the vault)

| Item | Where | Status |
|---|---|---|
| Site repo | `VELKMOOR_SITE/` (this folder) is a git repo. Remote: `https://github.com/loopcatz0001/velkmoor-site.git`, branch `main` | Last commit `cca233b` matches `origin/main` locally. Live state not checked (network was blocked in this session) |
| Custom domain | `VELKMOOR_SITE/CNAME` = `velkmoor.com` → GitHub Pages custom domain | DNS, HTTPS and domain registration not checked |
| Contact email | `info.velkmoor@gmail.com` (commit `4c1c3c4`, used on `/support.html` and all existing policies) | Whether the inbox actually receives mail is not checked |
| Older Crave Harbor pages | `US_APP_VAPEFREE/site_upload/craveharbor/{privacy,support}.html` (2026-10-11), meant for the separate repo `loopcatz0001/craveharbor` → `https://loopcatz0001.github.io/craveharbor/…` | Whether that repo is live is not checked. The new `/craveharbor/` pages here replace them |
| Other hosting configs | No `wrangler.toml`, `netlify.toml`, `vercel.json` or `_config.yml` anywhere in the vault | none |

New in this folder (uncommitted): `assets/app.css`, `craveharbor/`, `pillwindow/`, `stepsmith/` (4 pages + `icon.png` each), plus 3 added lines in `index.html`.

## Options

### A. Push to the existing GitHub Pages site (recommended)
The repo, the `velkmoor.com` CNAME and the contact address are already set up, and the 9 older app policies are served from here. The new pages only need a push.
1. Owner, or AI with the owner's go-ahead for this exact step: `cd VELKMOOR_SITE && git add assets craveharbor pillwindow stepsmith index.html PUBLISH_OPTIONS.md && git commit -m "Privacy and support pages: Crave Harbor, Pill Window, Stepsmith" && git push`
   (Leaving `PUBLISH_OPTIONS.md` out keeps it off the public site.)
2. On GitHub, open repo `velkmoor-site` › Settings › Pages. Check that Custom domain shows `velkmoor.com` with a green DNS check, and that **Enforce HTTPS** is on.
3. Open the 6 URLs below on your phone and check that each one loads.
- Cost: free (GitHub Pages on a public repo). The only cost is the yearly renewal of `velkmoor.com` at its registrar.
- Contracts the owner covers: GitHub Terms of Service (already accepted), domain registration and renewal (registrar). No new sign-up.

### B. Cloudflare Pages, Direct Upload (drag and drop)
1. Sign up at dash.cloudflare.com (owner accepts Cloudflare's terms), then go to Workers & Pages › Create › Pages › **Upload assets**.
2. Name the project (e.g. `velkmoor`) and drag in a copy of this folder **without** `.git` and `PUBLISH_OPTIONS.md`. Deploy.
3. The URL becomes `https://velkmoor.pages.dev/<app>/privacy.html`. Optionally add `velkmoor.com` as a custom domain; this needs DNS changes and conflicts with option A if A is live.
- Cost: free plan. Contracts: Cloudflare account and terms.
- Use it only if GitHub Pages turns out not to be working.

### C. GitHub Pages without the custom domain
Only if `velkmoor.com` is not owned or not pointed at GitHub. Remove `CNAME`, push, and the pages are served at `https://loopcatz0001.github.io/velkmoor-site/<app>/privacy.html`. Free. This exposes the account name `loopcatz0001` in public URLs, and every older app policy URL would change, so it is not recommended.

**Recommendation: A.** It needs no new account. The URLs match what Stepsmith already expects, and they sit next to the other Velkmoor policies.

## URLs to paste into App Store Connect (option A)

| App | Privacy Policy URL (EN-US) | Support URL (EN-US) | Japanese localization |
|---|---|---|---|
| Crave Harbor | `https://velkmoor.com/craveharbor/privacy.html` | `https://velkmoor.com/craveharbor/support.html` | `…/craveharbor/privacy-ja.html`, `…/support-ja.html` (only if a JA localization is added) |
| Pill Window | `https://velkmoor.com/pillwindow/privacy.html` | `https://velkmoor.com/pillwindow/support.html` | `https://velkmoor.com/pillwindow/privacy-ja.html`, `…/support-ja.html` |
| Stepsmith | `https://velkmoor.com/stepsmith/privacy.html` | `https://velkmoor.com/stepsmith/support.html` | `https://velkmoor.com/stepsmith/privacy-ja.html`, `…/support-ja.html` |

The pattern is `https://<host>/<app>/{privacy|support}[-ja].html`. With option B, `<host>` = `velkmoor.pages.dev`.

## What to replace once the URL is live (do not change yet)

### Crave Harbor (`US_APP_VAPEFREE`)
- `AppStore/metadata.md` line 66 (Description: "Privacy Policy: https://loopcatz0001.github.io/craveharbor/privacy.html")
- `AppStore/metadata.md` lines 69–70 (URLs: Privacy Policy URL, Support URL)
- `App/VapeFree/OtherViews.swift:649` `Links.privacy` (and the comment on line 647). Used by the paywall "Privacy" link (line 569).
- Owner decision: either keep `loopcatz0001.github.io/craveharbor` (if that repo is live, also update its content to these pages) or move to `velkmoor.com/craveharbor`. Recommended: move, so there is one source of truth.

### Pill Window (`US_APP_PILLWINDOW`)
- `AppStore/metadata.md` line 54 (EN Description: "Privacy Policy: TODO(human)")
- `AppStore/metadata.md` line 104 (JA 説明: "プライバシーポリシー: TODO(human)")
- `AppStore/metadata.md` lines 169–172 (Support URL, Privacy Policy URL)
- `App/PillWindow/Views/SettingsView.swift:157` `Links.privacy`. It is currently the placeholder `https://velkmoor.github.io/pillwindow/privacy.html`, which is a GitHub account that is not ours and will not resolve. Used in Settings › About and on the paywall (`PaywallView.swift:212`). **This one must change before submission**, so a new build is needed.

### Stepsmith (`US_APP_TASKSTEPS`)
- `AppStore/metadata.md` line 60 (EN Description) and line 117 (JA 説明): `https://velkmoor.com/stepsmith/privacy`
- `AppStore/metadata.md` lines 167–168 (Privacy Policy URL, Support URL: extensionless `/privacy`, `/support`)
- `App/TaskSteps/PaywallView.swift:172` `Links.privacy` = `https://velkmoor.com/stepsmith/privacy`. Used on the paywall and in Settings › About.
- GitHub Pages and Cloudflare Pages both serve `privacy.html` for the extensionless `/privacy`, so the current constant works with option A. Switching to the explicit `.html` is still safer. If the host stays `velkmoor.com`, no new build is strictly required.

## Owner decisions still open
1. Where to publish: A (recommended), B or C.
2. Contact email: keep `info.velkmoor@gmail.com` (already used on the site). Confirm that the inbox receives mail; App Review may write to it.
3. Crave Harbor: move its URLs to `velkmoor.com/craveharbor/` (recommended) or keep the `loopcatz0001.github.io/craveharbor` repo.
4. The legal name for "© 2026 Velkmoor" (also open in Pill Window's and Stepsmith's metadata).
