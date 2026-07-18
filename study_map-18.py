# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: StudyMap
def add_tags(topic_id, tags):
    topic = topics[topic_id]
    for tag in tags:
        if tag not in topic.tags:
            topic.tags.append(tag)
            return True
    return False


def remove_tags(topic_id, tags):
    topic = topics[topic_id]
    changed = False
    for tag in tags:
        if tag in topic.tags:
            topic.tags.remove(tag)
            changed = True
    return changed
