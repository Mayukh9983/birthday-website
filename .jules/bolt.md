## 2025-01-21 - CSS Animation & Content Visibility
**Learning:** Long CSS animation sequences (e.g., 11s delay) effectively hide content, but browsers still prioritize downloading it immediately.
**Action:** Use `loading="lazy"` for assets hidden behind long animations to defer their network usage until they are needed/visible.
