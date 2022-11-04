class Solution {
private:
    bool isvowel(char x)
    {
        return (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or
            x == 'E' or x == 'I' or x == 'O' or x == 'U');
    }
public:
    string reverseVowels(string s) 
    {
        int n = s.size();
        int i = 0 , j = n - 1;
        while(i < j)
        {
            if (isvowel(s[i]) and isvowel(s[j]))
            {
                swap(s[i],s[j]);
                i += 1;
                j -= 1;
            }
            else if (!isvowel(s[i]))
            {
                i += 1;
            }
            else if (!isvowel(s[j]))
            {
                j -= 1;
            }
        }
        return s;
    }
};