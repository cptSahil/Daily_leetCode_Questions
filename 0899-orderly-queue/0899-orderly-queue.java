class Solution {
    public String orderlyQueue(String s, int k) {
        int n = s.length();
        String ds = s+s;
        String ans = s;
        if(k==1){
            for(int i=1;i<n;i++){
                String sub = ds.substring(i,i+n);
                if(ans.compareTo(sub)>0)
                    ans = sub;
            }
            return ans;
        }
        char []cs= s.toCharArray();
        Arrays.sort(cs);
        return new String(cs);
    }
}