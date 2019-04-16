package codigo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int valorTroco = 4;
		List<Integer> moedas = new ArrayList<>(Arrays.asList(1,2,3));
		Stack<Integer> solucao = new Stack<Integer>();
		List<Integer[]> conjSolucao = new ArrayList<Integer[]>();
		
		int num = CalculoTroco.calculaTroco(valorTroco, moedas, solucao, conjSolucao);
		
		System.out.println("Localizadas " + num + "maneiras de se obter o troco.");
		for (Integer[] s : conjSolucao) {
			System.out.println(Arrays.toString(s));
		}
	}

}
