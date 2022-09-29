class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque
def adicionar_alfabeto(deque, alfabeto):
        for item in alfabeto:
          deque.add_front(item)
        return None
def decifrar(deque,texto_cifrado, chave):
    lista_decifrada=[]
    for i in texto_cifrado:
        c=0
        while c==0: 
            a= deque.remove_rear()
            deque.add_front(a)
            if a==i:
                b=0
                while b<=chave:
                    l=deque.remove_front()
                    deque.add_rear(l)
                    b+=1
                c=1            
        lista_decifrada.append(l)
    text_decifrado=''.join(map(str,lista_decifrada))
    return text_decifrado
def selecionar_subconjunto_missoes():
    w=int(input())
    m=int(input())
    o=int(input())
    alfabeto=input()
    chave=int(input())
    n=int(input())
    missoes_cifradas=[]
    missoes_decifradas=[]
    dados_missoes=[]
    d=Deque()
    contador=n
    aparece=m
    tempo_inicial=w
    while contador>0:
        missoes_cifradas.append(input()[1:-1])
        contador-=1
    #print(missoes_cifradas)
#     def adicionar_alfabeto(deque, alfabeto):
#         for item in alfabeto:
#           deque.add_front(item)
#         return None
#     def decifrar(deque,texto_cifrado, chave):
#         lista_decifrada=[]
#         for i in texto_cifrado:
#             c=0
#             while c==0: 
#                 a= deque.remove_rear()
#                 deque.add_front(a)
#                 if a==i:
#                     b=0
#                     while b<=chave:
#                         l=deque.remove_front()
#                         deque.add_rear(l)
#                         b+=1
#                     c=1            
#             lista_decifrada.append(l)
#         text_decifrado=''.join(map(str,lista_decifrada))
#         return text_decifrado
    adicionar_alfabeto(d, alfabeto)
    for item in missoes_cifradas:
        missoes_decifradas.append(decifrar(d,item,chave))
    #print (missoes_decifradas)
    for item in missoes_decifradas:
        dados_missoes.append(item.split(','))
   #criar listas com os tempos e os valores
    #tempo
    tempos=[]
    for lista in dados_missoes:
        tempos.append(int(lista[1]))
    valores=[]
    for lista in dados_missoes:
        valores.append(int(lista[2]))
    #fazer a mochila das missões
    def mochila(limite, tempo, valor, c,o):
        from operator import itemgetter, attrgetter
        indices=[]
        resultado=[]
        m = [[0 for w in range(limite + 1)] for i in range(c + 1)]
        for i in range(c + 1):
            for w in range(limite + 1):
                if i == 0 or w == 0:
                    m[i][w] = 0
                elif tempo[i - 1] <= w:
                    m[i][w] = max(valor[i - 1] + m[i - 1][w - tempo[i - 1]], m[i - 1][w])
                else:
                    m[i][w] = m[i - 1][w]  
        maior = m[c][limite]
        resultado.append(maior)      
        w = limite
        for i in range(c, 0, -1):
            if maior <= 0:
                break
            if maior == m[i - 1][w]:
                continue
            else:
                indices.append(i - 1)           
                maior = maior - valor[i - 1]
                w = w - tempo[i - 1]
#         print(resultado)
#         print(indices)
#         fazer o output das missões
        if aparece==1:
            lista_tuplas=[]
            output_missoes=[]
            for lista in dados_missoes:
                    lista_tuplas.append(tuple(lista))
            for i in indices:
                output_missoes.append(missoes_decifradas[i])
            if o==0:        
                output_missoes=sorted(output_missoes)
                for i in output_missoes:
                    i=i.replace(',',', ')
                    print(i)
            if o==1:
#                 lista_tuplas=[]
                for lista in dados_missoes:
                    lista[1]=int(lista[1])
#                 for lista in dados_missoes:
#                     lista_tuplas.append(tuple(lista))
                lista_tuplas_alfabetica=sorted(lista_tuplas)
                lista_tuplas_ordenada=sorted(lista_tuplas_alfabetica, key=lambda tempo: tempo[1])           
                for tupla in lista_tuplas_ordenada:
                    print(*list(tupla), sep=", ")
            if o==2:
#                 lista_tuplas=[]
                for lista in dados_missoes:
                    lista[2]=int(lista[2])
#                 for lista in dados_missoes:
#                     lista_tuplas.append(tuple(lista))
                lista_tuplas_alfabetica=sorted(lista_tuplas)
                lista_tuplas_ordenada=sorted(lista_tuplas_alfabetica, key=lambda valor: valor[2])           
                for tupla in lista_tuplas_ordenada:
                    print(*list(tupla), sep=", ")
            if o==3:
#                 lista_tuplas=[]
#                 for lista in dados_missoes:
#                     lista_tuplas.append(tuple(lista))
                lista_tuplas_alfabetica=sorted(lista_tuplas)
                lista_print=[]
                for lista in dados_missoes:
                    lista_tuplas.append(tuple(lista))
                    
                lista_tuplas_alfabetica=sorted(lista_tuplas)
                for tupla in lista_tuplas_alfabetica:
                    if tupla[3]=='easy':
                        lista_print.append(lista_tuplas_alfabetica.pop(lista_tuplas_alfabetica.index(tupla)))
                lista_tuplas_alfabetica=sorted(lista_tuplas_alfabetica)
                for tupla in lista_tuplas_alfabetica:
                    if tupla[3]=='medium':
                        lista_print.append(lista_tuplas_alfabetica.pop(lista_tuplas_alfabetica.index(tupla)))
                lista_tuplas_alfabetica=sorted(lista_tuplas_alfabetica)
                for tupla in lista_tuplas_alfabetica:
                    if tupla[3]=='hard':
                        lista_print.append(lista_tuplas_alfabetica.pop(lista_tuplas_alfabetica.index(tupla)))
                for i in lista_print:        
                    print(*list(i), sep=", ")
                        
           #tempo restante
        tempos_gastos=[]
        for i in indices:
            tempos_gastos.append(tempos[i])
        tempo_gasto_total=sum(tempos_gastos)
        tempo_restante=tempo_inicial-tempo_gasto_total
        print('Tempo restante:',(tempo_restante))
        print('Valor:',(*resultado))
            
            
                
                
                
                
                
                
            
    limite=w
    c=n
    (mochila(limite, tempos, valores, c,o))

    #calcular o tempo restante
      
selecionar_subconjunto_missoes()

