def group_images_into_questions(image_paths, group_size=4):
    blocks = []
    for i in range(0, len(image_paths), group_size):
        group = image_paths[i:i + group_size]
        if len(group) >= 2:
            blocks.append({
                "question": "What is the next figure?",
                "images": group[0],
                "option_images": group[1:]
            })
    return blocks
