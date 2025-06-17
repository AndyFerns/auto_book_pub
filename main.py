# main.py

from scraping.scraper import scrape_chapter
from ai_agents.writer_agent import WriterAgent
from ai_agents.reviewer_agent import ReviewerAgent
from human_loop.feedback_manager import collect_feedback
from versioning.chromadb_manager import save_version
from utils.helpers import load_config
from dotenv import load_dotenv
from rl_search.retriever import retrieve_version
from versioning.chromadb_manager import list_versions
import time 
import logging
import os

if __name__ == "__main__":
    config = load_config()
    dev_mode = config.get("dev_mode", False) 
    
    try: 
        # Step 1: Scrape and save raw content
        start = time.time()
        cache_path = "data/raw/chapter.txt"
        if dev_mode and os.path.exists(cache_path):
            print("🔁 Dev mode ON — loading cached content...")
            with open(cache_path, "r", encoding="utf-8") as f:
                raw_text = f.read()
        else:
            raw_text = scrape_chapter(config['scrape']['target_url'])
            # print(f"{raw_text}")
            print(f"[✅] Scraping done in {time.time() - start:.2f}s")

        # Step 2: Generate AI rewritten version
        start = time.time()
        writer = WriterAgent()
        rewritten = writer.spin(raw_text)
        print(f"[✅] Writing done in {time.time() - start:.2f}s")

        # Step 3: Let ReviewerAgent refine it
        start = time.time()
        reviewer = ReviewerAgent()
        reviewed = reviewer.review(rewritten)
        print(f"[✅] Reviewing done in {time.time() - start:.2f}s")

        # Step 4: Allow human feedback (optional loop)
        start = time.time()
        final_version = collect_feedback(reviewed, version_id="Chapter_01")
        print(f"[✅] Human feedback done in {time.time() - start:.2f}s")

        # Step 5: Save the finalized version to ChromaDB
        start = time.time()
        save_version(final_version)
        print(f"[✅] Saving done in {time.time() - start:.2f}s")
        
        #Step 6: Search for versions (optional)
        
        choice = input("\n📂 Would you like to list all saved versions? (y/n): ").strip().lower()
        if choice == 'y':
            list_versions()

        query = input("🔍 Search for a version (optional): ")
        if query.strip():
            results = retrieve_version(query, top_k=3)
            for result in results:
                print(f"\n🎯 Match: {result['metadata']['version_name']}")
                print("-" * 40)
                print(result['content'][:500])  # Show preview
                print("-" * 40)

        
        print("✅ Workflow completed successfully.\n")
    
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
