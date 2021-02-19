#include <stdio.h>
#include <stdlib.h>

int main()
{
	//cria todas as variaveis necessarias
	int resp, nf, fatorial, soma, opc, n, elevado, x, y, num, teste, imedia, pega, select;
	int areaQ, ladoQ, areaT, alturaT, baseT, areaR, alturaR, baseR;
	int resto, n2D, n1D, nFib, info, ano1, mes1, dia1, ano2, mes2, dia2, resAno, resMes, resDia;
	int Natual = 1, ultimo = 1, penultimo = 1;
	float Km, Min, Valorcorrida;
	int numero, und, dez, cen, mil;
	float v1, v2, total;
	char simbolo;

	printf("***BEM VIMDO AO KIT DE FERRAMENTAS TECLE 1 PARA PROSSEGUIR OU OUTRO NUNERO PARA SAIR:***\n");
	scanf("%d", &resp);

	system("cls");
	while (resp == 1) //A variavel resp controla a volta ao menu ou saida do programa quando solicitado pelo usuario
	{
		printf("Escolha O Que Deseja Fazer Agora:");

		printf("\n\n(1) Verificar a Primalidade de um Numero:");
		printf("\n(2) Calcular Area de Uma Figura:");
		printf("\n(3) Calcular o E-nesimo Elemento da Sequencia de Fibonacci:");
		printf("\n(4) Calcular Fatorial:");
		printf("\n(5) Calcular Valor de X Elevado a Y:");
		printf("\n(6) Apresentar a Media de N Numeros Inseridos:");

		printf("\n(7) Calcular Maximo Divisor Comun Entre Dois Numeros:");
		printf("\n(8) Calculadora:");
		printf("\n(9) Calculo da Diferenca Entre Duas Datas:");
		printf("\n(10) Converso de Numero Decimal em Nunero Romano");
		printf("\n(11) Calcular o valor de uma corrida de Uber\n\n");

		scanf("%d", &opc);
		system("clear");

		switch (opc)
		{
		case 1:

			printf("Digite um Numero:\n");
			scanf("%d", &n);

			if ((n % 1 == 0) && (n % n == 0) && (n % 2 != 0) && (n != 1) || (n == 2)) //Verifica se o numero atende ou nao aos criterios da primalidade
			{
				printf("%d Eh um Numero Primo\n\n", n);
			}
			else
			{
				printf("%d Nao Eh um Nunero Primo\n\n", n);
			}

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp); //Da ao usuario a opcao de voltar ao menu ou sair do programa

			system("cls");

			break;

		case 2:

			printf("Informe a Area de Qual Figura Deseja Calcular \n-- Quadrado = 1 \n-- Triangulo = 2 \n--Retangulo = 3\n"); //Solicita ao usuario que escolha a area de qual figura deseja calcular

			scanf("%d", &info);

			if (info == 1)
			{
				printf("Vamos Calcular a  Area do Quadrado\n\n");
				printf("Digite o Tamanho dos Lados do Quadrado\n");
				scanf("%d", &ladoQ);

				areaQ = ladoQ * ladoQ; //Realiza o calculo da area do quadrado e a armazena em areaQ

				printf("A Area do Quadrado eh:%d\n\n", areaQ);
			}

			if (info == 2)
			{
				printf("Vamos Calcular a Area do Triangulo\n\n");

				printf("Digite a Base do Triangulo\n");
				scanf("%d", &baseT);

				printf("Digite a Altura do Triangulo\n");
				scanf("%d", &alturaT);

				areaT = (baseT * alturaT) / 2; //Calcula a area do triangulo e armazena em areaT
				printf("A Area do Triangulo eh:%d\n\n", areaT);
			}

			if (info == 3)
			{
				printf("Vamos Calcular a Area do Retangulo\n\n");

				printf("Digite a Base do Retangulo\n");
				scanf("%d", &baseR);

				printf("Digite a Altura do Retangulo\n");
				scanf("%d", &alturaR);

				areaR = baseR * alturaR; //Calcula a area do retangulo e armazena em areaR

				printf("A Area do Retangulo eh:%d\n\n", areaR);
			}
			if (info != 1 && info != 2 && info != 3) //Se o usuario digitar alguma opcao de calculo da area diferente das disponiveis apresenta uma tela de erro
			{
				printf("Comando Invalido- Retornando ao Menu\n");
			}

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");
			break;

		case 3:

			printf("Vamos  Exibir o E-nesimo Termo de Um Numero na Sequencia de Fibonacci\n");

			Natual = 1, ultimo = 1, penultimo = 1; // As variaveis sao iniciadas com 1 pois seram somadas

			printf("Digite um Numero\n");
			scanf("%d", &nFib);

			for (int j = 0; j < nFib - 2; j++) // Enquanto j for menor que o numero digitado - 2
			{
				Natual = ultimo + penultimo; // O numero atual recebe o valor de ultimo + penultimo
				penultimo = ultimo;			 //Penultimo ira guardar sempre o ultimo valor armazenado pela variavel ultimo para soma lo a essa mesma variavel que recebera o numero atual para soma lo na proxima operacao (Confuso mais é isso kkk)
				ultimo = Natual;
			}
			printf("O E-nesimo termo eh: %d\n\n", Natual);

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");

			break;

		case 4:

			printf("Para Realizar o Calculo do Fatorial Digite um Numero:\n");
			scanf("%d", &nf);

			if (nf == 0) //Fatorial de 0 é 1
			{
				printf("O Fatorial de %d eh: 1\n\n", nf);

				printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
				scanf("%d", &resp);

				system("cls");
				break;
			}

			if (nf < 0) //Nao calcula o fatorial se o numero for negativo
			{
				printf("%d Numero Negativo\n\n", nf);
			}
			else
			{
				for (fatorial = 1; nf > 1; nf = nf - 1) //Faz o calculo ate que a variavel nf seja = 1, a cada nova repeticao a variavel nf recebe seu antecessor
				{
					fatorial = fatorial * nf;
				}

				printf("O Fatorial eh:%d\n\n", fatorial);
			}
			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");

			break;

		case 5:

			printf("Informaremos o Valor de X Elevado a Y.\n");
			printf("Para Isso Informe os Valores a Seguir:\n\n");
			printf("Digite o Valor de X:\n");
			scanf("%d", &x);
			printf("Digite o Valor de Y:\n");
			scanf("%d", &y);

			elevado = 1; //inicia a variavel elevado com 1 e nao com 0, ja que todo numero multiplicado a 0 é 0

			for (int i = y; i > 0; i--) // inicia variavel i com y e o decrementa ate que seja = 0
			{
				elevado = elevado * x; // multiplica o x pela quantidade de vezes que y sera decrementado
			}

			printf("O Valor de X: %d Elevado a Y: %d eh:%d\n\n", x, y, elevado);

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");

			break;

		case 6:

			printf("Iremos Calcular a Media da Soma de Varios Numeros\n\n");
			imedia = 0;
			soma = 0;

			num = 1; // iniciado com 1 , pois a condicao de parada ocorre quando num for igual a 0

			while (num != 0) //Enquanto num for diferente de 0 sera solicitado ao usuario que digite um numero
			{
				printf("Digite Um Numero ou Para interromper o Loop Digite 0:\n");
				scanf("%d", &num);

				soma = soma + num; // A variavel soma tem como funcao somar cada novo numero digitado pelo usuario
				imedia++;		   //um contador que conta a quantidade de numeros digitados
			}

			teste = imedia - 1; //A variavel recebe o contador - 1, visto que este esta contando o zero que é tido somente como condiçao de parada

			printf("\nA Soma dos Numeros: %d \nQuantidade de Numeros Digitados: %d \nMedia dos Numeros eh:%d\n\n", soma, imedia - 1, soma / teste);

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");
			break;

		case 7:

			printf("Vamos Calcular o Maximo Divisor Comun Entre Dois Numeros.\n\n");
			printf("Digite o Primeiro Numero:\n");
			scanf("%d", &n1D);

			printf("Digite o Segundo Numero:\n");
			scanf("%d", &n2D);

			resto = n1D % n2D; //Divide os numeros e guardar o resto da divisao

			while (resto != 0) //Enquanto o resto da dvisao for diferente de 0
			{
				n1D = n2D;		   //Numero 1 vai receber o numero 2
				n2D = resto;	   //Numero dois ira receber o resto da divisao
				resto = n1D % n2D; // A partir disso a divisao sera refeita ate que o resto seja igual a 0
			}

			//Apos isso o valor armazenado por n2D sera exibido, sendo este o ultimo numero pela qual foi possivel realizar a divisao
			printf("\nO Maximo Divisor Comun Entre Esses Numeros eh: %d\n\n", n2D);

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);

			system("cls");

			break;

		case 8:

			select = 0;
			pega = 0;

			printf("Bem Vindo A Calculadora.\n\n");

			while (select == 0) //refaz TODA a operacao caso o usuario deseje
			{
				while (pega == 0) //refaz SOMENTE  o primeiro calculo caso o usuario solicite
				{
					printf("Digite Dois Numeros Para Realizar a Primeira Operacao:\n");
					scanf("%f %f", &v1, &v2);
					printf("Informe a Operacao: + , - , * , /\n");
					scanf("%s", &simbolo);
					if (simbolo == '+' || simbolo == '-' || simbolo == '*' || simbolo == '/' && v2 != 0) //Verifica se o simbolo digitado pelo usuario corresponde a alguma operacao
					{
						//Faz o calculo de valor 1(v1) + valor 2(v2) de acordo com a operacao escolhida e armazena em total
						switch (simbolo)
						{
						case '+':

							total = v1 + v2;
							printf("%.2f + %.2f = %.2f\n", v1, v2, total);
							printf("\nPrimeira Operacao Realizada \n0 = Refazer Operacao \n1 = Prosseguir Para Proxima Operacao\n");
							scanf("%d", &pega);
							break;

						case '-':
							total = v1 - v2;
							printf("%.2f - %.2f = %.2f\n", v1, v2, total);
							printf("Primeira Operacao Realizada \n0 = Refazer Operacao \n1 = Prosseguir Para Proxima Operacao\n");
							scanf("%d", &pega);
							break;

						case '*':
							total = v1 * v2;
							printf("%.2f x %.2f = %.2f\n", v1, v2, total);
							printf("Primeira Operacao Realizada \n0 = Refazer Operacao \n1 = Prosseguir Para Proxima Operacao\n");
							scanf("%d", &pega);
							break;

						case '/':
							if (v2 != 0) //Se o numero for igual a 0 a divisao nao pode ser realizada(Impossivel dividir algum numero por 0)
							{
								total = v1 / v2;
								printf("%.2f / %.2f = %.2f\n", v1, v2, total);
							}
							else
							{
								printf("Impossivel Dividir Por Zero\n");
							}

							printf("Primeira Operacao Realizada \n0 = Refazer Operacao \n1 = Prosseguir Para Proxima Operacao\n");
							scanf("%d", &pega);
							break;

						default:

							printf(" Operador invalido\n\n ");
							break;
							printf("Primeira Operacao Realizada! \n0 = Refazer Operacao. \n1 = Prosseguir Para Proxima Operacao.\n");
							scanf("%d", &pega);
						}
					}
				}

				//Informa ao usuario que a primeira operacao foi realizada e seu resultado armazenado

				printf("Salvamos o Valor Da Operacao Feita Anteriormente.\nVamos a Proxima!!!\n");
				printf("Digite um Valor Para Ser Calculado ao Resultado Anterior:\n");
				scanf("%f", &v2);

				printf("Informe a Nova Operacao: + , - ,* , / \n");
				scanf(" %s", &simbolo);

				// Pega o resultado da operacao feita anteriormemte e a calcula com o novo numero de acordo com a nova operacao (-,+,*,/)
				switch (simbolo)
				{
				case '+':

					printf("Resultado Anterior: %.2f + %.2f = %.2f\n", total, v2, total + v2);
					break;

				case '-':
					printf("Resultado Anterior: %.2f - %.2f = %.2f\n", total, v2, total - v2);
					break;

				case '*':
					printf("Resultado Anterior: %.2f x %.2f = %.2f\n", total, v2, total * v2);
					break;

				case '/':
					if (v2 != 0)
						printf("Resultado Anterior: %.2f / %.2f = %.2f\n", total, v2, total / v2);
					else
						printf("Impossivel Realizar a Divisao por 0\n");
					break;

				default:
					printf(" Operador Invalido\n ");
					break;
				}

				//Permite ao usuario repetir todo o processo da Calculadora.
				printf("Opcoes:\n0 = Repetir Processo\n1: Sair do Item Calculadora:\n");
				scanf("%d", &select);
				if (select == 0)
				{
					pega = 0;
				}
			}
			printf("\n");
			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair do Programa:\n");
			scanf("%d", &resp);
			system("cls");

			break;

		case 9:

			//Solicita ao usuario que digite duas datas
			printf("Digite a Primeira Data com Dia/Mes/Ano:\n");
			printf("Ano:\n");
			scanf("%d", &ano1);
			printf("Mes:\n");
			scanf("%d", &mes1);
			printf("Dia:\n");
			scanf("%d", &dia1);

			printf("\nDigite a Segunda Data com Dia/Mes/Ano:\n");
			printf("Ano:\n");
			scanf("%d", &ano2);
			printf("Mes:\n");
			scanf("%d", &mes2);
			printf("Dia:\n");
			scanf("%d", &dia2);

			//Faz a subtracao de uma data pela outra
			resAno = ano1 - ano2;
			resMes = mes1 - mes2;
			resDia = dia1 - dia2;

			// Verifica se o resultado de alguma operacao anterior resultou em um numero negativo, se sim o multiplica por -1 a fim de torna lo positivo

			if (resAno < 0)
			{
				resAno = resAno * (-1);
			}

			if (resMes < 0)
			{
				resMes = resMes * (-1);
			}

			if (resDia < 0)
			{
				resDia = resDia * (-1);
			}

			printf("A diferenca entre as datas eh de %d ano(s)/ %d mes(es)/ %d dia(s)\n\n", resAno, resMes, resDia);

			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);
			system("cls");

			break;

		case 10:

			printf("Bem Vindo a Convercao De Numeros Decimais Para Romano\n");
			printf("Digite um numero: \n");
			scanf("%d", &numero);

			und = numero % 10; //utiliza o resto de uma divisao por dez para separar a casa das unidades

			numero = numero / 10;

			dez = numero % 10; //Agora separa a casa das dezenas

			numero = numero / 10;

			cen = numero % 10; //Separa a casa das centenas

			numero = numero / 10;

			mil = numero % 10; //separa a casa dos milhares

			numero = numero / 10;

			printf("Resultado da Conversao: ");

			//switch responsavel por apresentar o resultado na casa dos milhares
			switch (mil)
			{
			case 1:
				printf("M");
				break;
			case 2:
				printf("MM");
				break;
			case 3:
				printf("MMM");
				break;
			}

			//switch responsavel por apresentar o resultado na casa das centenas
			switch (cen)
			{
			case 1:
				printf("C");
				break;
			case 2:
				printf("CC");
				break;
			case 3:
				printf("CCC");
				break;
			case 4:
				printf("CD");
				break;
			case 5:
				printf("D");
				break;
			case 6:
				printf("DC");
				break;
			case 7:
				printf("DCC");
				break;
			case 8:
				printf("DCCC");
				break;
			case 9:
				printf("CM");
				break;
			}

			//switch responsavel por apresentar o resultado na casa das dezenas
			switch (dez)
			{
			case 1:
				printf("X");
				break;
			case 2:
				printf("XX");
				break;
			case 3:
				printf("XXX");
				break;
			case 4:
				printf("XL");
				break;
			case 5:
				printf("L");
				break;
			case 6:
				printf("LX");
				break;
			case 7:
				printf("LXX");
				break;
			case 8:
				printf("LXXX");
				break;
			case 9:
				printf("XC");
				break;
			}

			//switch responsavel por apresentar o resultado na casa das unidades
			switch (und)
			{
			case 1:
				printf("I");
				break;
			case 2:
				printf("II");
				break;
			case 3:
				printf("III");
				break;
			case 4:
				printf("IV");
				break;
			case 5:
				printf("V");
				break;
			case 6:
				printf("VI");
				break;
			case 7:
				printf("VII");
				break;
			case 8:
				printf("VIII");
				break;
			case 9:
				printf("IX");
				break;
			}
			printf("\n");

			printf("\nDigite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);
			system("cls");

			break;

		case 11:

			printf("Digite a Distancia a ser Percorrida em Km:\n");
			scanf("%f", &Km);
			printf("Digite a Duração da Corrida em Minutos:\n");
			scanf("%f", &Min);

			//Recebe os dados e faz o calculo do valor da corrida .. somando 2 + os Km percorridos x 1,4 + a quantidade de minutos que durou a viagem  x 0.26

			Valorcorrida = 2 + Km * 1.4 + Min * 0.26;
			printf("\nA sua corrida foi : R$%.2f\n", Valorcorrida);
			printf("\n");
			printf("Digite 1 Para Retornar ao Menu ou Outro Numero Para Sair:\n");
			scanf("%d", &resp);
			system("cls");
			break;
		}
	}
	printf("Programa Encerrado\n"); //Encerra o programa
	return 0;
}

