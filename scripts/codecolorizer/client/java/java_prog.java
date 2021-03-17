class Stack {
   private LinkedList linkedList;
    
   Stack() {
      linkedList = new LinkedList();
   }
   
   public void push(int newData) {
      // Create a new node and prepend
      Node newNode = new Node(newData);
      linkedList.prepend(newNode);
   }
   
   public int pop() {
      // Copy list head's data
      int poppedItem = linkedList.getHeadData();
      
      // Remove list head
      linkedList.removeAfter(null);
      
      // Return popped item
      return poppedItem;
   }
   
   public void print() {
      linkedList.printList();
   }
}

public class StackDemo {
   public static void main(String[] args) {
      int[] numbers = { 91, 66, 9, 46, 23, 65, 6, 77 };
      
      // Initialize a new Stack and add numbers
      Stack numStack = new Stack();
      for (int number : numbers) {
          numStack.push(number);
      }

      // Output stack
      System.out.print("Stack after push: ");
      numStack.print();
      
      // Pop 77 and print
      numStack.pop();
      System.out.print("Stack after first pop: ");
      numStack.print();
      
      // Pop 6 and print
      numStack.pop();
      System.out.print("Stack after second pop: ");
      numStack.print();
   }
}