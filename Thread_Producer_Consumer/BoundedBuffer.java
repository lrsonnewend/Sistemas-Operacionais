class BoundedBuffer implements Buffer{ 
    
      private static final int BUFFER_SIZE = 3; 
      private int count;
      private int in;
      private int out;
      private Object[] buffer;
      
      /*método construtor iniciando o buffer vazio*/ 
      public BoundedBuffer(){
         count = 0;
         in = 0;
         out = 0;
         buffer = new Object[BUFFER_SIZE];
      }
   
      /*método usado na classe Producer*/
      public void insert(Object item) {
         while (count == BUFFER_SIZE){
         /*não faz nada se o buffer estiver cheio*/
         }
         
      /*adicionando conteúdo no buffer*/
         ++count;
         buffer[in] = item;

      /*a variável in recebe o resto da divisão de (in+1)
      pelo tamanho do buffer*/
         in = (in + 1) % BUFFER_SIZE; 
         
      /*informações do feedback do buffer*/
         if (count == BUFFER_SIZE){
            System.out.println("BUFFER FULL "
               + "Producer inserted \"" + item 
               + "\" count=" + count + ", "
               + "in=" + in + ", out=" + out);
         }

         else{
            System.out.println("Producer inserted \"" + item 
               + "\" count=" + count + ", "
               + "in=" + in + ", out=" + out);
         }
      }
   
      /*método usado na classe Consumer*/
       public Object remove() {
         Object item;

         /*caso o buffer esteja vazio, não faz nada*/
         while (count == 0){ 

         }
      
      /*removendo conteúdo do buffer*/
         --count;
         item = buffer[out];

      /*out recebe o resto da divisão de (out+1) pelo tamanho 
      do tamanho do buffer*/
         out = (out + 1) % BUFFER_SIZE;
      
      /*informações do feedback do buffer*/
         if (count == 0){
            System.out.println("BUFFER EMPTY "
               + "Consumer removed \"" + item 
               + "\" count=" + count + ", "
               + "in=" + in + ", out=" + out);
         }

         else{
            System.out.println("Consumer removed \"" + item 
               + "\" count=" + count + ", "
               + "in=" + in + ", out=" + out);
         }

         return item;
      }
   }