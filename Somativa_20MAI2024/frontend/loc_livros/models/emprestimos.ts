import type { Livro } from "./livros";
import type { Usuario } from "./usuario";

export enum PAGAMENTOS {
    'PENDENTE' = "P",
    'APROVADO' = "A",
    'CANCELADO' = "C",
    'RECUSADO' = "R",
}

export enum EMPRESTIMO {
    'PENDENTE' = "P",
    'APROVADO' = "A",
    'CANCELADO' = "C",
    'RECUSADO' = "R",
}

export type Emprestimo = {
    id?: number,
    usuarioFK: string;
    dataEmprestimo?: string;
    devolucaoPrevista: string;
    status1: EMPRESTIMO;
    status2: PAGAMENTOS;
} 


export type EmprestimoLivros = {
    livroFK: Livro;
    emprestimoFK: Emprestimo;
}


export type EmprestimoLivrosBody = {
    livroFK: Livro;
    emprestimoFK: Emprestimo;
}