## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2026-02-06 - Font Weight Optimization
**Learning:** Google Fonts requests often include unused weights (e.g., `wght@400;700` when only 400 is used).
**Action:** Audit font requests and remove unused weights to reduce critical rendering path blocking and save bandwidth.
