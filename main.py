from cadastro import salvar_fotos, load_images_from_folder
from reconhecer_faces import recenhecimento_faces_cadastradas
from modelagem_dados import carregar_imagens_rotulos
from modelo import model

def run():
    
    opção = int(input("""
    1- Cadastro de face
    2- Reconhecer face
    """))

    if opção == 1:
        nome = str(input('Digite o seu nome completo: '))
        caminho_pasta = salvar_fotos(nome)
        imagens, rotulos = carregar_imagens_rotulos(caminho_pasta)

        
        
    elif opção == 2:
        recenhecimento_faces_cadastradas()


if __name__ == '__main__':
    run()