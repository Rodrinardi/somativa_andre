import { BACKEND_URL } from "~/models/emprestimo";
import type { Emprestimo, EmprestimoLivros, EmprestimoLivrosBody } from "~/models/emprestimos";

export const salvarEmprestimo = (venda: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimos/`, {
    method: 'POST',
    body: venda
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};


export const salvarEmprestimoLivros = (vendas: Array<EmprestimoLivrosBody>): Promise<EmprestimoLivros | null> => {
  return useFetch<EmprestimoLivros>(`${BACKEND_URL}/emprestimo-livros/`, {
    method: 'POST',
    body: vendas
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};