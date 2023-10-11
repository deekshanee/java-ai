class StackUtility {
    int arr [] = new int [100001];
   
    int track = -1;
    public StackUtility() {
        
    }
    //O(1)
    public void push(int val) {
        track = track+1; // so that i can give u new index O(1)
        arr[track] = val; //O(1)
    }
    
    //O(1)
    public void pop() {
        if(!isEmpty())
        track = track -1;  //O(1)  
        
    }
    
    //O(1)
    public int top() {
        return arr[track]; //O(1)
    }
    public boolean isEmpty(){
        if(track == -1){
            return true;
        } else {
            return false;
        }
    }
}
class MinStack {
    
    StackUtility mainStack; // it will store all element
    StackUtility auxStack; //it will store only min element

    
    public MinStack() {
        mainStack = new StackUtility();
        auxStack = new StackUtility();

    }
    //O(1)
    public void push(int val) {
       mainStack.push(val);
       if(auxStack.isEmpty()){
           auxStack.push(val); //because this is first element
       } else{
         if(auxStack.top() >= val){
           auxStack.push(val);
       }
       }
       
    }
    
    //O(1)
    public void pop() {
        if(mainStack.top() == auxStack.top()){
            auxStack.pop();
        }
        mainStack.pop();
    }
    
    //O(1)
    public int top() {
      return mainStack.top();
    }
    
    public int getMin() {
        return auxStack.top();    
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
**/
