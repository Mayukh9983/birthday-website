## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2025-01-30 - Font Loading Optimization
**Learning:** Google Fonts requests can include unused weights (e.g., `wght@400;700`). Removing unused weights reduces the CSS size and prevents potential download of unused font files.
**Action:** Always check font usage and only request the weights that are actually used in CSS.
