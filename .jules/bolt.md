## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2025-01-25 - Unused Animations
**Learning:** Found complex CSS animations (`.flower`, `fall`, `rotate`) that were completely unused in HTML/JS.
**Action:** Always grep for CSS class usage in HTML/JS before assuming they are needed.
