import java.util.Date;

class Consumer implements Runnable{
	private Buffer mbox;

	/*método construtor*/
	public Consumer(Buffer mbox){
		this.mbox = mbox;
	}

	public void run(){
		Date message;
		
		while(true){
			/*delay de 5seg.*/
			SleepUtilities.nap();
			
			/*consome o item message do buffer*/
			message = (Date)mbox.remove();

			/*exibe o conteúdo na tela (hora e data)*/
			if(message != null)
			System.out.println("Consumer consumed: "+message);
			
		}
	}
}
