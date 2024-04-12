# Constantes para controlar o retorno da função get_token 
TK_INT = 1  # Indica lexema reconhecido como um TK_INT
TK_END = 2  # Indica lexema reconhecido como um TK_END

# Função para percorrer um lexema e reconhecer como um token, simulando o autômato
def get_token(chars):
    state = 'q0' # Começando do estado Inicial

    # Itera sobre cada caractere da lista de caracteres de cada lexema lido no arquivo

    # Esse for simula exatamente o autômato da imagem contida nesse diretório
    # Retorna -1 sempre que não for possível uma transição de estados, ou seja, interrompe o percurso direto e recusa lexema
    # Caso contrário, se o estado ao final do percurso não for 'INT' ou 'END', o token não é reconhecido
    
    for char in chars:
        if state == 'q0':
            if char.isdigit():
                state = 'q1'
            elif char in 'ABCDEF':
                state = 'q18'
            else:
                return -1
        elif state == 'q1':
            if char.isdigit():
                state = 'q3'
            elif char == '.':
                state = 'q5'
            elif char == 'x':
                state = 'q19'
            else:
                state = 'INT'
        elif state == 'q3':
            if char.isdigit():
                state = 'q4'
            elif char == '/':
                state = 'q27'
            elif char == '_':
                state = 'q13'
            elif char == '.':
                state = 'q5'
            else:
                state = 'INT'
        elif state == 'q4':
            if char.isdigit():
                state = 'q12'
            elif char == '.':
                state = 'q5'
            else:
                state = 'INT'
        elif state == 'q12':
            if char.isdigit():
                state = 'q12'
            else:
                state = 'INT'
        elif state == 'q18':
            if char == 'x':
                state = 'q19'
            else:
                return -1
        elif state == 'q19':
            if char.isdigit() or (char in 'ABCDEF'):
                state = 'q20'
            else:
                return -1
        elif state == 'q20':
            if char.isdigit() or (char in 'ABCDEF'):
                state = 'q20'
            else:
                state = 'END'

    # Verifica o estado final depois de ler a lista de caracteres do lexema
    if state == 'INT':
        return TK_INT
    elif state == 'END':
        return TK_END
    else:
        return -1 # Estado que não representa aceitação, portanto lexema não forma um token

# Leitura do arquivo e processamento caracter a caracter
try:
    # Abrir o arquivo para leitura
    with open('tests.txt', 'r') as file:
        # Ler todas as linhas do arquivo
        lexemes = file.readlines() # Transforma cada linha em um elemento da lista de lexemas
        # Iterar sobre as linhas
        for lexeme in lexemes:
            # Transformar o lexema em uma lista de caracteres
            lexeme = list(lexeme.strip()+ '$') # Remove /n e espaço em branco e adciona o $ como o '\0' do C
            # Essa varíavel é basicamente juntar o lexema porém caractere por caractere + um de terminação

            # Aqui é basicamente unir cada um dos caracteres do lexema é uma varíavel para printar no console
            contentLexeme = ''.join(lexeme).strip('$') # Unindo cada caractere do lexema em uma string única para printar, exceto o $

            # Testa o retorno da função para verificar se é um INT ou um ENDEREÇO
            if (get_token(lexeme)) == TK_INT:
                print(f'{contentLexeme} eh TK_INT')
            elif(get_token(lexeme)) == TK_END:
                print(f'{contentLexeme} eh TK_END')
            else:
                # Caso não seja os dois tipos de dados que implementei, retorna que não reconheceu
                print(f'{contentLexeme} nao eh reconhecido com TK_INT ou TK_END em cic 2024.1')

# Trata erro de arquivo não encontrado
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
# Trata qualquer outro erro que ocorra ao tentar se comunicar com o arquivo
except Exception as e:
    print("Ocorreu um erro:", e)