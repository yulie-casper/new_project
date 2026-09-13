# === Stage 43: Добавь пагинацию длинных списков ===
# Project: StudyMap
def paginate_study_map(study_map, page_size=10):
    """Return paginated view of study map topics with progress."""
    total_pages = (len(study_map["topics"]) + page_size - 1) // page_size
    page = 1
    while True:
        start = (page - 1) * page_size
        end = start + page_size
        page_topics = study_map["topics"][start:end]
        if not page_topics:
            break
        for topic in page_topics:
            print(f"\n--- {topic['title']} (page {page}/{total_pages}) ---")
            print(f"  Status: {topic['status']}")
            if topic.get("materials"):
                print(f"  Materials: {len(topic['materials'])} items")
            if topic.get("checkpoints"):
                print(f"  Checkpoints: {topic['checkpoints'][-1] if topic['checkpoints'] else 'none'}")
        page += 1
