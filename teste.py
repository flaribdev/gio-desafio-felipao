import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
  
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = r"\(\d{2}\) \d{5}-\d{4}"
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
       result = "Número de telefone válido."
       return result
    else:
       result = "Número de telefone inválido."
       return result
        
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
       
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result =validate_numero_telefone(phone_number)
# Imprime o resultado:
print(result)