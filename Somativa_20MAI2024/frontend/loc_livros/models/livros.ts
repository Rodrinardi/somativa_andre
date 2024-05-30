export type GeneroLivro = {
    id: number;
    nome: string;
}
export type Livro = {
    id: number;
    titulo: string;
    valor: number;
    quantidade: number;
    autor: string;
    GeneroLivroFK: GeneroLivro;
    descricao: string;
    editora: string;
    idade: number;
    dataLancamento: number;
    publicacao: number;
    fotoFK: Array<string>;
    numeroPaginas: number;
    formato: string;
    codEdicao: number;
    aprovado: string;
}

