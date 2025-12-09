from datasets import load_dataset
import json

NUM_QUESTIONS = 10_000

def main():
    ds = load_dataset("lmsys/lmsys-chat-1m")
    train = ds['train']

    model_questions = []
    
    for i, d in enumerate(train):
        if i == NUM_QUESTIONS:
            break

        # the authors of this dataset anonymize things by replacing real names
        # with with strings like "NAME_1". because I would expect the model
        # just be like confused in these situations, i don't include them in
        # the dataset to try to have a more realistic chat sample.
        if "NAME" not in d['conversation'][0]['content']:
            model_questions.append(d['conversation'][0]['content'])

    # i used claude to help me remember the syntax for this part
    # https://claude.ai/share/6f6bb481-54de-4a05-830b-31f196262a09
    with open("questions.json", 'w') as f:
        json.dump(model_questions, f, indent=2)

if __name__ == '__main__':
    main()