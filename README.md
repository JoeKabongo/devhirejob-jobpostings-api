# DevHire JP Scraping API

A lightweight FastAPI service that scrapes and serves software engineering job listings in Japan. This backend service is part of a broader of my project "devhirejb" that help dev finds jobs in JP and tracks their jobs haunting process.

---

## 🚀 Features

- GET endpoint to retrieve developer job listings in Japan

---

## 📚 Endpoints

### `GET /api/v1/jobs`

Returns the latest list of scraped job postings from supported sources.

---

## Future Plans

- GET /api/v1/stats → expose job stats (remote %, top stacks, companies)
- Support job scraping in other countries (Singapore, Korea, US, remote-only)
- Use LLMs to auto-tag job posts (e.g., visa sponsorship, tech stack)
- Add keyword-based search & filtering
