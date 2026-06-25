# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: StudyMap
def delete_topic(topic_id: int) -> bool:
    if topic_id not in topics:
        print(f"Ошибка: тема с ID {topic_id} не найдена.")
        return False
    
    del topics[topic_id]
    
    # Удаляем связанные материалы и контрольные точки, если они привязаны к удаленной теме
    for material_id, material_data in list(materials.items()):
        if material_data.get('topic_id') == topic_id:
            del materials[material_id]
            
    for checkpoint_id, checkpoint_data in list(checkpoints.items()):
        if checkpoint_data.get('topic_id') == topic_id:
            del checkpoints[checkpoint_id]
    
    print(f"Тема {topic_id} успешно удалена вместе со связанными данными.")
    return True

def delete_material(material_id: int) -> bool:
    if material_id not in materials:
        print(f"Ошибка: материал с ID {material_id} не найден.")
        return False
    
    del materials[material_id]
    
    # Удаляем контрольные точки, связанные с удаленным материалом (если они хранят ссылку на материал)
    for checkpoint_id, checkpoint_data in list(checkpoints.items()):
        if 'material_id' in checkpoint_data and checkpoint_data['material_id'] == material_id:
            del checkpoints[checkpoint_id]
            
    print(f"Материал {material_id} успешно удален.")
    return True

def delete_checkpoint(checkpoint_id: int) -> bool:
    if checkpoint_id not in checkpoints:
        print(f"Ошибка: контрольная точка с ID {checkpoint_id} не найдена.")
        return False
    
    del checkpoints[checkpoint_id]
    
    # Удаляем материалы, если они привязаны только к этой точке (опционально, зависит от архитектуры)
    for material_id in list(materials.keys()):
        if 'checkpoints' in materials[material_id] and checkpoint_id in materials[material_id]['checkpoints']:
            del materials[material_id]['checkpoints'][checkpoint_id]
            
    print(f"Контрольная точка {checkpoint_id} успешно удалена.")
    return True
