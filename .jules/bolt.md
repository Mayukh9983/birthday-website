## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2025-02-04 - Unused Font Weights
**Learning:** Google Fonts imports often include weights that are never used in the CSS (e.g., `wght@400;700` when only 400 is used).
**Action:** Audit font imports against computed styles to save network requests and bytes.
