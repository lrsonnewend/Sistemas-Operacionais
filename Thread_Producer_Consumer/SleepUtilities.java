class SleepUtilities{
  
  /*tempo máximo de nap em segundos*/
  private static final int NAP_TIME = 5; 
    
    public static void nap() {
      nap(NAP_TIME);
    }
   
    public static void nap(int duration) {

      /*varável sleeptime recebe os 5 segundos multiplicado
      pelo valor de um número aleatório*/
      int sleeptime = (int) (NAP_TIME * Math.random() );
      
      System.out.println("Nap for " + sleeptime + " seconds"); 


      /*Faz com que o encadeamento em execução adormeça pelo tempo
      de 1 segundo*/
      try { 
        Thread.sleep(sleeptime*1000); 
      }

      catch (InterruptedException e) {
      }
    }
  }
