## 2025-01-22 - Unused and Broken Script Cleanup
**Learning:** The project included a `js/script.js` file linked in `index.html` that contained code for a completely different application (a Valentine's Day proposal), referencing non-existent DOM elements. This caused runtime errors and wasted resources.
**Action:** When auditing performance, always verify that linked resources are actually relevant and functional. Removing broken, unused code is a valid and necessary performance optimization.
