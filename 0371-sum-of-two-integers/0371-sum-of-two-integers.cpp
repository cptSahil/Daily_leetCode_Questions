class Solution {
public:
    int getSum(int a, int b) {
        while(b!=0){
            int sum = a ^ b;
            unsigned c = (a & b);
            a ^= b;
            b = c<<1;
        }
        return a;
    }
};