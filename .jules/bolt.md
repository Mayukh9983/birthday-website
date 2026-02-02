## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2026-02-02 - Focus on Single Optimization
**Learning:** Attempted to bundle CSS dead code removal with Font optimization. This violated the "ONE small performance improvement" rule and created risk of unnecessary breaking changes.
**Action:** Isolate optimizations. If multiple opportunities exist, pick the most impactful/safest one and ignore the others for the current PR.
