class Solution {
    public boolean isAdditiveNumber(String num) {
        int L = num.length();
        
        for(int i=1; i<=(L-1)/2;i++){
            if(num.charAt(0) == '0' && i>=2) break;
            for(int j = i+1; L-j>=j-i && L-j>=i;j++){
                if(num.charAt(i) =='0' &&j-i>=2) break;
                long a = Long.parseLong(num.substring(0,i));
                long b = Long.parseLong(num.substring(i,j));
                String substr = num.substring(j);
                if(isAdditive(substr,a,b)) return true;
            }
        }
        return false;
    }
    public boolean isAdditive(String str,long a,long b){
        if(str.equals("")) return true;
        long sum = a+b;
        String s = ((Long)sum).toString();
        if(!str.startsWith(s)) return false;
        return isAdditive(str.substring(s.length()),b,sum);
    }
}

