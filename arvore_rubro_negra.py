class NoRN:
    def _init_(self, valor, cor='vermelho'):
        self.valor = valor
        self.cor = cor
        self.esquerda = None
        self.direita = None
        self.pai = None

    def _str_(self):
        return f"{self.valor}({self.cor[0]})"

class ArvoreRubroNegra:
    def _init_(self):
        self.NIL = NoRN(0, 'preto')
        self.NIL.esquerda = self.NIL
        self.NIL.direita = self.NIL
        self.NIL.pai = self.NIL
        self.raiz = self.NIL
    
    def inserir(self, valor):
        novo_no = NoRN(valor)
        novo_no.esquerda = self.NIL
        novo_no.direita = self.NIL
        novo_no.pai = self.NIL
        
        pai = self.NIL
        atual = self.raiz
        
        while atual != self.NIL:
            pai = atual
            if novo_no.valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        novo_no.pai = pai
        
        if pai == self.NIL:
            self.raiz = novo_no
        elif novo_no.valor < pai.valor:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no
            
        self._balancear_insercao(novo_no)
        self.raiz.cor = 'preto'
        print(f"✅ Valor {valor} inserido com sucesso!")
    
    def _balancear_insercao(self, no):
        while no.pai.cor == 'vermelho':
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                
                if tio.cor == 'vermelho':
                    no.pai.cor = 'preto'
                    tio.cor = 'preto'
                    no.pai.pai.cor = 'vermelho'
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self._rotacao_esquerda(no)
                    
                    no.pai.cor = 'preto'
                    no.pai.pai.cor = 'vermelho'
                    self._rotacao_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                
                if tio.cor == 'vermelho':
                    no.pai.cor = 'preto'
                    tio.cor = 'preto'
                    no.pai.pai.cor = 'vermelho'
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self._rotacao_direita(no)
                    
                    no.pai.cor = 'preto'
                    no.pai.pai.cor = 'vermelho'
                    self._rotacao_esquerda(no.pai.pai)
            
            if no == self.raiz:
                break
    
    def _rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        
        if y.esquerda != self.NIL:
            y.esquerda.pai = x
        
        y.pai = x.pai
        
        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        
        y.esquerda = x
        x.pai = y
    
    def _rotacao_direita(self, x):
        y = x.esquerda
        x.esquerda = y.direita
        
        if y.direita != self.NIL:
            y.direita.pai = x
        
        y.pai = x.pai
        
        if x.pai == self.NIL:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y
        
        y.direita = x
        x.pai = y
    
    def buscar(self, valor):
        resultado = self._buscar_recursivo(self.raiz, valor)
        if resultado != self.NIL:
            return resultado
        return None
    
    def _buscar_recursivo(self, no, valor):
        if no == self.NIL or valor == no.valor:
            return no
        
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        else:
            return self._buscar_recursivo(no.direita, valor)
    
    def em_ordem(self):
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado
    
    def _em_ordem_recursivo(self, no, resultado):
        if no != self.NIL:
            self._em_ordem_recursivo(no.esquerda, resultado)
            cor_abrev = 'v' if no.cor == 'vermelho' else 'p'
            resultado.append(f"{no.valor}({cor_abrev})")
            self._em_ordem_recursivo(no.direita, resultado)
    
    def imprimir_arvore(self, no=None, nivel=0, prefixo="Raiz: "):
        if no is None:
            no = self.raiz
        
        if no != self.NIL:
            cor_simbolo = "🔴" if no.cor == 'vermelho' else "⚫"
            print("  " * nivel + prefixo + f"{no.valor} {cor_simbolo}")
            
            if no.esquerda != self.NIL:
                self.imprimir_arvore(no.esquerda, nivel + 1, "Esq: ")
            if no.direita != self.NIL:
                self.imprimir_arvore(no.direita, nivel + 1, "Dir: ")
    
    def altura_preta(self, no=None):
        if no is None:
            no = self.raiz
        
        if no == self.NIL:
            return 0
        
        altura_esq = self.altura_preta(no.esquerda)
        altura_dir = self.altura_preta(no.direita)
        
        adicional = 1 if no.cor == 'preto' else 0
        return adicional + max(altura_esq, altura_dir)

def menu_interativo():
    arvore = ArvoreRubroNegra()
    
    while True:
        print("\n" + "="*50)
        print("🌳 MENU ÁRVORE RUBRO-NEGRA")
        print("="*50)
        print("1. Inserir valor")
        print("2. Buscar valor")
        print("3. Mostrar árvore")
        print("4. Listar em ordem")
        print("5. Mostrar altura preta")
        print("6. Inserir vários valores")
        print("7. Demonstração automática")
        print("0. Sair")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            try:
                valor = int(input("Digite o valor para inserir: "))
                arvore.inserir(valor)
            except ValueError:
                print("❌ Erro: Digite um número válido!")
        
        elif opcao == "2":
            try:
                valor = int(input("Digite o valor para buscar: "))
                resultado = arvore.buscar(valor)
                if resultado:
                    cor = "vermelho" if resultado.cor == 'vermelho' else "preto"
                    print(f"✅ Valor {valor} encontrado! Cor: {cor}")
                else:
                    print(f"❌ Valor {valor} não encontrado!")
            except ValueError:
                print("❌ Erro: Digite um número válido!")
        
        elif opcao == "3":
            print("\n📊 ESTRUTURA DA ÁRVORE:")
            if arvore.raiz == arvore.NIL:
                print("Árvore vazia!")
            else:
                arvore.imprimir_arvore()
        
        elif opcao == "4":
            valores = arvore.em_ordem()
            if valores:
                print(f"\n📈 Valores em ordem: {', '.join(valores)}")
            else:
                print("Árvore vazia!")
        
        elif opcao == "5":
            altura = arvore.altura_preta()
            print(f"\n📏 Altura preta da árvore: {altura}")
        
        elif opcao == "6":
            try:
                entrada = input("Digite os valores separados por espaço: ")
                valores = [int(x.strip()) for x in entrada.split()]
                print(f"\n📥 Inserindo {len(valores)} valores...")
                for valor in valores:
                    arvore.inserir(valor)
                print("✅ Todos os valores foram inseridos!")
            except ValueError:
                print("❌ Erro: Digite números válidos separados por espaço!")
        
        elif opcao == "7":
            print("\n🎬 INICIANDO DEMONSTRAÇÃO AUTOMÁTICA")
            demo_valores = [10, 20, 30, 40, 50, 60, 70, 25, 35, 45]
            print(f"Valores: {demo_valores}")
            
            for valor in demo_valores:
                arvore.inserir(valor)
            
            print("\n⭐ DEMONSTRAÇÃO CONCLUÍDA!")
            arvore.imprimir_arvore()
            print(f"Em ordem: {arvore.em_ordem()}")
            print(f"Altura preta: {arvore.altura_preta()}")
        
        elif opcao == "0":
            print("👋 Saindo do programa...")
            break
        
        else:
            print("❌ Opção inválida! Tente novamente.")

def entrada_rapida():
    """Modo de entrada rápida para testes"""
    arvore = ArvoreRubroNegra()
    
    print("🌳 MODO ENTRADA RÁPIDA")
    print("Digite 'sair' para finalizar")
    print("Digite 'mostrar' para ver a árvore")
    print("Digite números para inserir")
    print("-" * 40)
    
    while True:
        entrada = input("\n➡️  Digite um valor ou comando: ").strip().lower()
        
        if entrada == 'sair':
            break
        elif entrada == 'mostrar':
            print("\n📊 ÁRVORE ATUAL:")
            arvore.imprimir_arvore()
            print(f"Em ordem: {arvore.em_ordem()}")
        elif entrada == 'altura':
            print(f"Altura preta: {arvore.altura_preta()}")
        else:
            try:
                valor = int(entrada)
                arvore.inserir(valor)
            except ValueError:
                print("❌ Entrada inválida! Digite um número ou comando válido.")

# PROGRAMA PRINCIPAL
if _name_ == "_main_":
    print("🌳 ÁRVORE RUBRO-NEGRA - SISTEMA INTERATIVO")
    print("=" * 55)
    
    while True:
        print("\nEscolha o modo de execução:")
        print("1. Menu Interativo (completo)")
        print("2. Entrada Rápida (simples)")
        print("3. Sair")
        
        modo = input("\nSelecione o modo (1-3): ").strip()
        
        if modo == "1":
            menu_interativo()
        elif modo == "2":
            entrada_rapida()
        elif modo == "3":
            print("👋 Programa finalizado!")
            break
        else:
            print("❌ Modo inválido! Tente novamente.")
