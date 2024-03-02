from TTS import ttsPlay, ttsElevenLabs
from VTT import speech_to_text

from fuzzywuzzy import fuzz



def parse_dialogue(filename):
    dialogue_list = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(' ', 1)
                if len(parts) == 2:
                    speaker, dialogue = parts
                    dialogue_list.append((speaker,dialogue))

    return dialogue_list



if __name__ == "__main__":
    #text = speech_to_text()
    #ttsPlay("You said: "+ text)
    print("Which character would you like to be, A or B?")
    character = input("")

    dialogue = parse_dialogue("scripts/careful.txt")
    for line in dialogue:
        if line[0] != character:
            print(line[1])
            ttsElevenLabs(line[1])


        elif line[0] == character:
            print("Please say your line now:")
            userLine = speech_to_text()

            ratio = fuzz.ratio(userLine, line[1])

            if ratio>80:
                print(u'\u2713')
            else:
                #print("You said : " + userLine)
                print("\n The actual line was : " + line[1])
                print("\n If what you said was actually correct ignore this message.")

    #print(dialogue_dict)
