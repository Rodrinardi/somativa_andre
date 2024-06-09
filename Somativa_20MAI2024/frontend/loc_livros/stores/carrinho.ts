import type { Livro } from "~/models/livros";

export type CarrinhoItem = {
    livro: Livro;
    quantidade: number;
}

export type Carrinho = {
    livros: Array<CarrinhoItem>;    
}

export const carrinho = defineStore('carrinhoStore', {
    state: (): Carrinho => ({
        livros: []
    }),
    actions: {
      adicionarNoCarrinho(novoLivro: Livro){
            const livroJaExiste = this.getLivroDoCarrinho(novoLivro);
            if(livroJaExiste){
                livroJaExiste.quantidade += 1;
                this.livros = [
                    ...this.livros.filter(item=>item.livro.id !== livroJaExiste.livro.id),
                    livroJaExiste
                ];
            }
            
            else{
                this.livros.push({
                    quantidade: 1,
                    livro: novoLivro
                });
            }
      },
      removerDoCarinho(carrinhoItem: CarrinhoItem){
        const posicaoNoCarrinho = this.getLivroDoCarrinhoIndex(carrinhoItem.livro);
        //remover o item inteiro do carrinho
        this.livros.splice(posicaoNoCarrinho,1);

        if(carrinhoItem.quantidade){
            this.livros = [
                ...this.livros,
                carrinhoItem
            ];
        }
      },
      esvaziarCarrinho(){
        this.livros = [];
      }
    },
    getters: {
        estaNoCarrinho: (carrinho:Carrinho) => (livroParaEncontrar: Livro): boolean =>{
            return carrinho.livros.findIndex(item=>item.livro.id === livroParaEncontrar.id) !== -1;
        },
        getLivroDoCarrinho: (carrinho:Carrinho) => (livroParaEncontrar: Livro)=>{
            return carrinho.livros.find(item=>item.livro.id === livroParaEncontrar.id);
        },
        getLivroDoCarrinhoIndex: (carrinho:Carrinho) => (livroParaEncontrar: Livro)=>{
            return carrinho.livros.findIndex(item=>item.livro.id === livroParaEncontrar.id);
        },
        getCarrinho: (carrinho: Carrinho) => () : Array<CarrinhoItem> => {
            return carrinho.livros;
        },
        getValorTotalDoCarrinho: (carrinho: Carrinho) => () : Number => {
            let soma = 0;
            carrinho.livros.forEach(item=>{
                soma += (item.livro.valor * item.quantidade)
            })
            return soma;
        }
    }
  })