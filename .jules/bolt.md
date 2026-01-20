## 2025-01-20 - Legacy Script Cleanup
**Learning:** Found a `script.js` file included in `index.html` that referenced non-existent DOM elements (`noButton`, `yesButton`). This indicates the file was copy-pasted from another project ("Will you be my Valentine?" prank) and left unused.
**Action:** Always verify that included scripts are actually used and compatible with the current DOM. Removing dead scripts saves requests and prevents runtime errors.
