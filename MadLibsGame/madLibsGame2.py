# -*- coding: utf-8 -*-
from random import randint
import copy

story = (
    "Um dia meu {} amigo e eu decidimos ir ao jogo de {} em {}. " +
    "Nós realmente queríamos ver {} jogar {}. " +
    "Então, nós {} nosso {} até o {} e compramos alguns {}s. " +
    "Nós nos envolvemos no jogo e foi muito divertido. " +
    "Nós comemos alguns {} {} e bebemos {} {}. " +
    "Foi ótimo! Estamos até planejando ir novamente no mês que vem." 
)

# dictionary to lookup words by type
word_dict = {
    'adjectives': ['inteligente',
                   'alegre',
                   'feliz',
                   'amigável',
                   'jovem',
                   'triste',
                   'confiante',
                   'horrível',
                   'importante',
                   'pobre',
                   'azul',
                   'pobre',
                   'grande',
                   'fácil',
                   'difícil',
                   'livre',
                   'responsável',
                   'forte',
                   'belga',
                   'israelense',
                   'fiel',
                   'civil',
                   'melhor',
                   ],
    'city names': ['Governador Valadares',
                    'Contagem',
                    'Betim',
                    'Uberlândia',
                    'Ribeirão das Neves',
                    'Ouro Preto',
                    'Tiradentes',
                    'Belo Horizonte',
                    'Pindamonhangaba',
                    'São Paulo',
                    'Bauru',
                    'Araraquara',
                    'Piracicaba',
                    'Campinas',
                    'Diadema',
                    'Osasco',
                    'Santos',
                    'Mogi das Cruzes'],
    'nouns': [
                    'homem',
                     'mulher', 
                     'criança', 
                     'idoso', 
                     'amigo', 
                     'colega', 
                     'parente', 
                     'pai', 
                     'irmão', 
                     'mãe', 
                     'prima', 
                     'menino', 
                     'menina', 
                     'cachorro', 
                     'gato', 
                     'camelo', 
                     'baleia', 
                     'pato', 
                     'tartaruga', 
                     'girafa', 
                     'elefante',  
                     'girassol', 
                     'margarida', 
                     'rosa', 
                     'orquídea', 
                     'samambaia', 
                     'manga', 
                     'uva', 
                     'melancia', 
                     'laranja', 
                     'banana',  
                     'vento', 
                     'furacão', 
                     'tempestade', 
                     'dia', 
                     'noite', 
                     'brisa', 
                     'vendaval'
    ],
    'action verbs': [
                    'pensamos',
                    'dividimos',
                    'lutamos',
                    'almoçamos',
                    'nascemos',
                    'acreditamos',
                    'cortamos',
                    'comemos',
                    'ouvimos',
                    'compramos',
                    'derrubamos',
                    'começamos',
                    'concordamos',
                    'lembramos',
                    'simpatizamos',
                    'duvidamos',
                    'gostamos',
                    'obedecemos',
                    'bebemos',
    ],
    'sports noun': [
                    'bola',
                    'rede',
                    'raquete',
                    'uniforme',
                    'capacete',
                    'jogador',
                    'torcida'
    ],
    'place': [
                    'parque',
                    'deserto',
                    'floresta',
                    'loja',
                    'restaurante',
                    'mercado',
                    'peixaria',
                    'lagoa'
    ],
}


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjectives', local_dict),
        get_word('sports noun', local_dict),
        get_word('city names', local_dict),
        get_word('nouns', local_dict),
        get_word('nouns', local_dict),
        get_word('action verbs', local_dict),
        get_word('nouns', local_dict),
        get_word('place', local_dict),
        get_word('nouns', local_dict),
        get_word('adjectives', local_dict),
        get_word('nouns', local_dict),
        get_word('adjectives', local_dict),
        get_word('nouns', local_dict),

    )

print("CASO 1: ")
story1 = create_story()
print(story1)
print()
print("CASO 2: ")
story2 = create_story()
print(story2)
