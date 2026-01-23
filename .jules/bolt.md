## 2025-01-23 - Dead Code and Hidden Content
**Learning:** Found `js/script.js` was completely unrelated to the HTML (referencing missing IDs) and caused runtime errors. Also, images were hidden via CSS opacity animation for 11 seconds, making them perfect candidates for aggressive lazy loading/async decoding without LCP impact.
**Action:** Always check if scripts match the HTML structure. For content hidden by long animations, defer loading as much as possible.
