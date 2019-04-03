import java.util.Date;

class Producer implements Runnable{
	private Buffer mbox;

	/*método construtor*/
	public Producer(Buffer mbox){
		this.mbox = mbox;
	}

	public void run(){
		Date message;
		
		while(true){
			/*delay de 5seg.*/
			SleepUtilities.nap();
			
			/*a variável message recebe a data e a hora do dia atual*/
			message = new Date();

			/*imprime na tela os dados de message*/
			System.out.println("Producer produced: "+message);
			
			/*enviando mensagem*/
			mbox.insert(message);
		}
	}
}