## 2025-01-24 - Dead Code Removal
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements, causing runtime errors.
**Action:** Always verify that included scripts are actually used and functional. Removing dead code saves HTTP requests and prevents console pollution.

## 2026-01-29 - Feature Preservation vs. Code Cleanup
**Learning:** Attempted to remove unused `.flower` CSS, but it was flagged as a potential feature removal rather than just dead code.
**Action:** When optimizing, distinguish between "dead code" (referencing missing files/ids) and "unused code" (definitions that might be used dynamically or in future). Prioritize purely technical optimizations (like font weights) over logic/feature removal unless certain.
