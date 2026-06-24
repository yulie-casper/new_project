# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: StudyMap
def edit_topic(topic_id: int, new_data: dict) -> bool:
    if not isinstance(new_data, dict):
        raise ValueError("new_data must be a dictionary")
    
    for i, topic in enumerate(topics):
        if topic["id"] == topic_id:
            topics[i] = {**topic, **new_data}
            return True
    
    print(f"Topic with id {topic_id} not found.")
    return False

def edit_material(material_id: int, new_content: str) -> bool:
    for i, topic in enumerate(topics):
        if material_id in topic["materials"]:
            idx = topic["materials"].index(material_id)
            topics[i]["materials"][idx] = {"id": material_id, "content": new_content}
            return True
    
    print(f"Material with id {material_id} not found.")
    return False

def edit_checkpoint(checkpoint_id: int, new_status: str) -> bool:
    for i, topic in enumerate(topics):
        if checkpoint_id in topic["checkpoints"]:
            idx = topic["checkpoints"].index(checkpoint_id)
            topics[i]["checkpoints"][idx] = {"id": checkpoint_id, "status": new_status}
            return True
    
    print(f"Checkpoint with id {checkpoint_id} not found.")
    return False
