package codigo;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/* Uma condição base para o algoritmo é que se o valor do troco 
 for menor que zero, ou o número de moedas disponíveis for maior que zero, o programa termina.*/

public class CalculoTroco {
	
	// Método para calcular o troco.
	static int calculaTroco(int valorTroco, List<Integer> moedas, Stack<Integer> solucao, List<Integer[]> conjSolucao) {
		// Retorna 0, se o valor do troco for maior que 0, ou se o número de moedas for zero.  
		if ((valorTroco < 0) || (moedas.size() == 0)) return 0;
		// Retorna 1, se o valor do troco for igual a zero.
		if (valorTroco == 0) {
			conjSolucao.add(solucao.toArray(new Integer[solucao.size()]));
			return 1;
		}
		
		// Pega uma moeda da lista de moedas.
		int moeda = moedas.get(0);
		solucao.push(moeda);
		// Utiliza recursão, diminuindoo valor do troco pela moeda.
		int valor1 = calculaTroco(valorTroco - moeda, moedas, solucao, conjSolucao);
		solucao.pop();
		
		List<Integer> moedasNovo = new ArrayList<Integer>(moedas);
		moedasNovo.remove(moeda);
		int valor2 = calculaTroco(valorTroco, moedasNovo, solucao, conjSolucao);
		
		return valor1 + valor2;
		
	}
	
	// TODO Método para mostrar a lista de moedas que foram selecionadas na solução.
}
