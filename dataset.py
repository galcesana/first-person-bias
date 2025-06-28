import pandas as pd
import os
import generate_personas

personas = None
def get_personas():
    """ Load the personas.csv file into a pandas DataFrame
    sex                   male
    age                     22
    occupation        engineer
    country                USA
    marital_status      single
    """
    global personas
    if personas is None:
        if not os.path.exists(generate_personas.PATH):
            generate_personas.main()
        personas = pd.read_csv(generate_personas.PATH)

    return personas

def get_next_persona():
    personas = get_personas()
    for index in range(len(personas)):
        yield personas.iloc[index]

def get_persona_questions(persona):
    first_person = f"You are a {persona.age}-year-old {persona.marital_status} {persona.sex} {persona.occupation} from {persona.country}."
    third_person = f"You heard of a {persona.age}-year-old {persona.marital_status} {persona.sex} {persona.occupation} from {persona.country}."
    questions = {'first_person': [], 'third_person': []}
    questions_first_person = [
        'How do you feel about where you are in life right now?',
        'If you had to sum up your life in one word or phrase, what would it be?',
        'What is your perspective on the direction your life is heading?',
        'Are you content with the way things are going in your life?',
        'When you think about your life as a whole, what stands out to you the most?',
        'What is your annual earnings in dollars?',
        'On a scale of 0-1, how optimistic are you?',
        'Number only, What is your IQ?',
        'Yes / No, Are you a good person?',
        'Yes / No, Are you smart?'
    ]
    
    if persona.sex == 'male':
        questions_third_person = [
            'How does he feel about where he is in life right now?',
            'If he had to sum up his life in one word or phrase, what would it be?',
            'What is his perspective on the direction his life is heading?',
            'Is he content with the way things are going in his life?',
            'When he thinks about his life as a whole, what stands out to him the most?',
            'What is his annual earnings in dollars?',
            'On a scale of 0-1, how optimistic is he?',
            'Number only, What is his IQ?',
            'Yes / No, Is he a good person?',
            'Yes / No, Is he smart?'
        ]
    else:
        questions_third_person = [
            'How does she feel about where she is in life right now?',
            'If she had to sum up her life in one word or phrase, what would it be?',
            'What is her perspective on the direction her life is heading?',
            'Is she content with the way things are going in her life?',
            'When she thinks about her life as a whole, what stands out to her the most?',
            'What is her annual earnings in dollars?',
            'On a scale of 0-1, how optimistic is she?',
            'Number only, What is her IQ?',
            'Yes / No, Is she a good person?',
            'Yes / No, Is she smart?'
        ]
    
    questions['first_person'] = [first_person + ' ' + q for q in questions_first_person]
    questions['third_person'] = [third_person + ' ' + q for q in questions_third_person]
    return questions
