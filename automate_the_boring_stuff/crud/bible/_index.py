#   Generate bible numbers and verses

pairs = {
    'Genenis 1:1': 'In the beginning, God created the heavens and the earth',
    'Genesis 1:2': 'And the earth was without form',
    'Exodus 33:14': 'And I will go with you, and I will give you rest',
    'Exodus 33:15': 'Send us not away, if your presence will not go with us',
    'Exodus 33:16': 'How then shall they know, that weve found grace in thy sight',
    'Numbers 14:28': 'Thus said the lord, whatever you say unto my ears, that ll do unto thee',
    'Duetoromy 28': 'Bless shall be when that goeth in and thou comest out, bless shall be the baskets and the fruits',
    'Joshua 1:9': 'Havent I commanded thee? Be strong and be of god courage, be not afraid, nor of dismain, for I will be with you whenever thou goeth',
    'Isaiah 60:1': 'Arise, shine, for the light has comeand the glory of the lord has risen up upon thee',
}

# Generate the quiz papers and anwsers
for i in range(3):
    quiz = open(f'quiz{i+1}', 'w')
    answer = open(f'answer{i+1}', 'w')

    quiz.write(' '*20 + f'Quiz form {i+1}\n\n')
    quiz.write('STUDENT NAME:\nSTUDENT NUMBER:\n\n')

    answer.write(' '*20 + f'Answer form {i+1}\n')

    for i in range(3):
        #   Question
        quiz.write(
            f'\n{i+1} What does {list(pairs.keys())[i]} say in the bible?\n\n')
        # 4 Options
        for i in range(4):
            quiz.write('ABCD'[i] + '.' f' {list(pairs.values())[i]}\n')

        answer.write(
            f"{i + 1}. {'ABCD'[list(pairs.keys()).index(list(pairs.keys())[i])]}\n")

    quiz.close()
    answer.close()
