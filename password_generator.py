import random

def index():

    def gerar_senha():
        def shuffle(string):
            temp_list = list(string)
            random.shuffle(temp_list)
            return "".join(temp_list)

        def number_generator():
            number = int(random.randint(0, 9))
            return number

        def uppercase_letter_generator():
            uppercase_letter = chr(random.randint(65, 90))
            return uppercase_letter

        def lowercase_letter_generator():
            lowercase_letter = chr(random.randint(97, 122))
            return lowercase_letter

        def character_generator():
            character = random.choice('!@#$%&*.')
            return character

        uppercase_letter_1 = uppercase_letter_generator()  # ASCII code / https://www.ascii-code.com/
        uppercase_letter_2 = uppercase_letter_generator()
        uppercase_letter_3 = uppercase_letter_generator()
        uppercase_letter_4 = uppercase_letter_generator()

        lowercase_letter_1 = lowercase_letter_generator()
        lowercase_letter_2 = lowercase_letter_generator()
        lowercase_letter_3 = lowercase_letter_generator()
        lowercase_letter_4 = lowercase_letter_generator()

        number_1 = str(number_generator())
        number_2 = str(number_generator())
        number_3 = str(number_generator())
        number_4 = str(number_generator())

        character_1 = character_generator()
        character_2 = character_generator()
        character_3 = character_generator()
        character_4 = character_generator()

        password_part_1 = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + number_1 + number_2 + character_1 + character_2
        password_part_2 = uppercase_letter_3 + uppercase_letter_4 + lowercase_letter_3 + lowercase_letter_4 + number_3 + number_4 + character_3 + character_4

        password_part_1 = shuffle(password_part_1)
        password_part_2 = shuffle(password_part_2)

        password = password_part_1 + "-" + password_part_2

        print(password)

    passwords_times = int(input("Deseja gerar quantas senhas?"))

    print("Senha(s) gerada(s):")
    for password_time_selected in range(passwords_times):
            gerar_senha()


def after():
    generate_again = (input("Deseja gerar novamente? SIM (1) / NÃO (2)"))
    after_verification = False

    if generate_again == "1":
        index()
        after()
        after_verification = True
    elif generate_again == "2":
        print("Obrigado, até mais!")
        after_verification = True

    if after_verification == False:
        print("Valor inválido")
        after()

index()

after()