class Solution {
    public int openLock(String[] deadends, String target) {
            Set<String> deadEndsSet = new HashSet<String>();
            // Set<String> visited = new HashSet<String>();
            for(String val:deadends){
                deadEndsSet.add(val);
            }
            String current = "0000";
            if (deadEndsSet.contains(target) || deadEndsSet.contains(current)){return -1;}
            if (current.equals(target)){return 0;}
            
            Deque<String> que = new ArrayDeque<>();
            que.add(current);
            
            int step = 0;
            
            while(!que.isEmpty()){
                int size = que.size();
                for(int j=0; j<size; j++){
                    current = que.pop();
                    
                    for(int i=0; i<4; i++){
                        int currentValAtIndex = current.charAt(i) - '0';
                        
                        String add = current.substring(0,i) + (currentValAtIndex+1+10)%10 + current.substring(i+1,4);
                        String subtract = current.substring(0,i) + (currentValAtIndex-1+10)%10 + current.substring(i+1,4);
                        
                        if(!deadEndsSet.contains(add)){
                            que.add(add);
                            deadEndsSet.add(add);
                        }
                        if(!deadEndsSet.contains(subtract)){
                            que.add(subtract);
                            deadEndsSet.add(subtract);
                        }
                        
                        if(add.equals(target) || subtract.equals(target)){
                            return step+1;
                        }
                        
                    }
                }
                step++;
            }
            
            return -1;
    }
}