import java.util.Date;

public class Factory{
		public static void main(String[] args) {
		/*cria buffer que será compartilhado pelo Producer e Consumer*/
        Buffer sharedBuffer = new BoundedBuffer();

        /*cria os threads producer e consumer*/
		Thread producerThread = new Thread(new Producer(sharedBuffer));
		Thread consumerThread = new Thread(new Consumer(sharedBuffer));

		/*alocando memória para um novo encadeamento*/
		producerThread.start();
		consumerThread.start();

		/*instancia um novo servidor*/		
		Factory server = new Factory();
	}
}