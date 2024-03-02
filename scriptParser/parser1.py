def parse_dialogue(filename):
    dialogue_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                speaker, dialogue = line.split(' ', 1)
                if speaker in dialogue_dict:
                    dialogue_dict[speaker].append(dialogue)
                else:
                    dialogue_dict[speaker] = [dialogue]

    return dialogue_dict

filename = "your_text_file.txt"
dialogue_dict = parse_dialogue(filename)
