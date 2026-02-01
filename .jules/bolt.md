## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2025-02-01 - Clean Workspace
**Learning:** Generated temporary analysis files (`fonts_full.css`, `server.log`) were almost committed.
**Action:** Always verify `ls -a` or `git status` equivalent before submitting to ensure no garbage files are included.
