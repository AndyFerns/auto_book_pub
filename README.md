# 📘 Automated Book Publication Workflow

An intelligent agent-driven pipeline to automate the rewriting and publication of public-domain books with human-in-the-loop editing and content versioning.

---

## ✨ Features

- **🌐 Web Scraping**  
  Scrapes book chapters from online sources (e.g., [Wikisource](https://en.wikisource.org)) using Playwright.

- **🧠 AI Content Generation**  
  Uses a multi-agent architecture (Writer & Reviewer) powered by LLMs (like Google Gemini) to rewrite and refine chapters.

- **🧑‍💻 Human-in-the-Loop Editing**  
  Optional manual feedback after AI rewriting allows human writers/editors to make changes before finalizing.

- **📚 Content Versioning**  
  Final outputs are saved into **ChromaDB** with automatic version labels (v1, v2, ...), UUIDs, and metadata.

- **🔍 RL-inspired Retrieval**  
  Query past versions using TF-IDF + cosine similarity (stubbed for future reinforcement learning-based retrieval).

---

## 📂 Directory Structure

```text
auto_book_pub/
├── main.py                    # Entry point
├── README.md
├── LICENSE
├── requirements.txt
├── .env
├── .gitignore
├── config/
│   └── settings.yaml
├── data/
│   ├── raw/                   # Raw scraped HTML + screenshots
│   ├── processed/             # AI-edited versions
│   └── versions/              # Finalized, versioned outputs
├── scraping/
│   └── scraper.py             # Playwright-based scraper
├── ai_agents/
│   ├── writer_agent.py        # AI "spinner"
│   ├── reviewer_agent.py      # Reviewer LLM
│   └── editor_agent.py        # Optional human/AI edit flow
├── human_loop/
│   └── feedback_manager.py    # Handle user input iterations
├── versioning/
│   └── chromadb_manager.py    # Store/retrieve versioned content
├── rl_search/
│   └── retriever.py           # Reinforcement Learning-based retriever
└── utils/
    └── helpers.py             # Common utilities

```

## 🚀 How It Works

1. **Scrape Content**

```python
   raw_text = scrape_chapter(target_url)
   ```

2. **AI Rewriting + Review**

```python
rewritten = WriterAgent().spin(raw_text)
reviewed  = ReviewerAgent().review(rewritten)

```

3. **Human Feedback (Optional)**

```python
final_version = collect_feedback(reviewed)
```

4. **Save to ChromaDB**

```python
save_version(final_version)
```

5. **Retrieve Similar Versions**

```python
results = retrieve_version("version-number")
```

## ⚙️ Setup

### 🔧 Prerequisites

-Python 3.10+

-Google Gemini API Key (optional)

-Playwright dependencies

## 📦 Installation

```bash
git clone https://github.com/yourusername/auto_book_pub
cd auto_book_pub
```

### Set up Python environment

```bash
pip install -r requirements.txt
```

### Set up Playwright

```bash
playwright install
```

### 🔐 .env Configuration

Create a .env file:

```env
GEMINI_API_KEY=your_google_gemini_key
```

## 🧪 Dev Mode (Optional)

To avoid re-scraping each time, enable dev mode in main.py:

```python
dev_mode = True
if dev_mode:
    raw_text = load_cached_text()
else:
    raw_text = scrape_chapter(url)
```

## 📄 License

MIT License. See LICENSE for details.
