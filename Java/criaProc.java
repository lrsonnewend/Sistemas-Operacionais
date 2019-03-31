import java.io.*;

class criaProc {

	public static void main(String[] args) throws IOException{

		if(args.length != 1){

			System.out.println("Usage: java OSProcess <command>");

			System.exit(0);
		}

		/*a variável pb recebe um novo processo criado
		com o comando ProcessBuilder()*/
		//args[0] is the command
		ProcessBuilder pb = new ProcessBuilder(args[0]);

		/*Cria uma nova instância do processo criado acima*/
		Process proc = pb.start();

		
		/*Pega o conteúdo gerado na leitura de dados na criação do processo*/
		InputStream is = proc.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);

		/*Lê o que foi inserido na variável isr*/
		BufferedReader br = new BufferedReader(isr);

		
		//read what is returned by the command
		/*Declaração de uma variável do tipo string*/
		String line;

		/*A variável line recebe o conteúdo lido pela variável br 
		enquanto a variável line for diferente de vazio, ela 
		imprime na tela o seu conteúdo até que tal condição seja
		contrária e o arquivo seja fechado.*/
		while((line = br.readLine()) != null)
			System.out.println(line);

		br.close();
	}
}