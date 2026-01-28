## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2025-01-28 - Unused Font Weights
**Learning:** Google Fonts imports often include unused weights (e.g. 700) by default or from copy-paste. In this static site, 'Atma' was imported with 700 but only used at 400.
**Action:** Audit font imports against actual CSS usage to save ~20KB per weight.
