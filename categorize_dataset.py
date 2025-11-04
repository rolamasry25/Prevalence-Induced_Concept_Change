
import re

def categorize_text(text):
    text_lower = text.lower()
    
    unethical_keywords = [
        'kill', 'dead', 'die', 'murder', 'drown', 'shock', 'abuse', 'harm', 'pain', 'vomit', 'yell at a child',
        'suicide', 'traumatic', 'distress', 'anxiety', 'fear', 'disgust', 'prison', 'solitary confinement',
        'uncomfortable', 'embarrassment', 'frustration', 'insult', 'violent', 'weapon', 'gun', 'knife',
        'steal', 'cheat', 'lie', 'deceive', 'manipulate', 'racist', 'sexist', 'homophobic', 'pornography',
        'sexual', 'arousal', 'genitals', 'masturbate', 'nude', 'naked', 'urine', 'feces', 'vomit',
        'disorder', 'depression', 'paralyzes', 'hallucinogenic', 'drug', 'intoxicated', 'alcohol',
        'marijuana', 'heroin', 'sedatives', 'poison', 'contaminate', 'blood', 'needle', 'surgery',
        'mutilation', 'torture', 'burn', 'drown', 'suffocate', 'electrocute', 'execute', 'assault',
        'violation', 'harassment', 'stalking', 'threaten', 'intimidate', 'coerce', 'force',
        'humiliate', 'degrade', 'dehumanize', 'exploit', 'betray', 'abandon', 'isolate', 'ostracize',
        'exclude', 'reject', 'bully', 'shame', 'guilt', 'regret', 'remorse', 'sorrow', 'grief',
        'sadness', 'unhappy', 'cry', 'scream', 'yell', 'shout', 'terror', 'horror', 'panic',
        'agony', 'suffering', 'anguish', 'despair', 'hopelessness', 'helplessness', 'powerlessness',
        'vulnerability', 'defenselessness', 'insecurity', 'worthlessness', 'inadequacy',
        'inferiority', 'superiority', 'prejudice', 'discrimination', 'bigotry', 'hatred',
        'animosty', 'enmity', 'hostility', 'malevolence', 'malice', 'spite', 'vengeance',
        'revenge', 'retaliation', 'punishment', 'justice', 'injustice', 'fairness',
        'unfairness', 'equality', 'inequality', 'rights', 'freedom', 'liberty',
        'oppression', 'slavery', 'genocide', 'war', 'terrorism', 'atrocity',
        'heinous', 'abhorrent', 'detestable', 'despicable', 'vile', 'wicked',
        'evil', 'immoral', 'unethical', 'unjust', 'wrong', 'bad', 'sinful',
        'criminal', 'illegal', 'unlawful', 'illicit', 'illegitimate', 'improper',
        'inappropriate', 'unacceptable', 'unprofessional', 'unbecoming', 'unseemly',
        'disgraceful', 'shameful', 'dishonorable', 'disreputable', 'despicable',
        'contemptible', 'abominable', 'monstrous', 'outrageous', 'scandalous',
        'shocking', 'appalling', 'horrifying', 'terrible', 'awful', 'dreadful',
        'frightful', 'ghastly', 'grisly', 'gruesome', 'hideous', 'repulsive',
        'revolting', 'repugnant', 'offensive', 'distasteful', 'disgusting',
        'nauseating', 'sickening', 'unpalatable', 'unsavory', 'unwholesome',
        'noxious', 'toxic', 'poisonous', 'venomous', 'lethal', 'fatal', 'deadly',
        'dangerous', 'hazardous', 'perilous', 'risky', 'unsafe', 'unhealthy',
        'harmful', 'injurious', 'detrimental', 'damaging', 'destructive', 'ruinous',
        'calamitous', 'catastrophic', 'disastrous', 'tragic', 'unfortunate',
        'unlucky', 'ill-fated', 'doomed'
    ]
    
    ambiguous_keywords = [
        'deceive', 'mislead', 'trick', 'fool', 'hoax', 'bluff', 'feign', 'fake',
        'pretend', 'impersonate', 'disguise', 'camouflage', 'mask', 'veil',
        'shroud', 'cloak', 'obscure', 'ambiguous', 'vague', 'unclear', 'equivocal',
        'cryptic', 'enigmatic', 'puzzling', 'perplexing', 'baffling', 'bewildering',
        'confusing', 'misleading', 'deceptive', 'delusive', 'illusory', 'fantastical',
        'chimerical', 'fictitious', 'fabricated', 'concocted', 'invented', 'unreal',
        'untrue', 'false', 'bogus', 'phoney', 'spurious', 'counterfeit', 'forged',
        'fraudulent', 'sham', 'mock', 'imitation', 'ersatz', 'surrogate',
        'artificial', 'synthetic', 'man-made', 'unnatural', 'affected', 'assumed',
        'put-on', 'contrived', 'studied', 'labored', 'strained', 'forced',
        'unspontaneous', 'insincere', 'hypocritical', 'two-faced', 'double-dealing',
        'duplicitous', 'treacherous', 'perfidious', 'disloyal', 'unfaithful',
        'traitorous', 'recreant', 'apostate', 'renegade', 'turncoat', 'deserter',
        'betrayer', 'informer', 'stool-pigeon', 'whistle-blower'
    ]
    
    if any(keyword in text_lower for keyword in unethical_keywords):
        return 'unethical'
    elif any(keyword in text_lower for keyword in ambiguous_keywords):
        return 'ambiguous'
    else:
        return 'harmless'

dataset_path = 'dataset.js'

with open(dataset_path, 'r') as f:
    file_content = f.read()

texts_str = re.search(r'\[(.*)\]', file_content, re.DOTALL).group(1)
texts = re.findall(r'"(.*?)"', texts_str, re.DOTALL)

categorized_texts = []
for text in texts:
    text = text.strip().replace('\\t', '').replace('\\n', '')
    if not text:
        continue
    category = categorize_text(text)
    categorized_texts.append({'text': text, 'category': category})

new_dataset_content = 'window.ethicalTexts = ' + str(categorized_texts) + ';'

with open(dataset_path, 'w') as f:
    f.write(new_dataset_content)
