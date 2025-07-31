class Solution {
public:
    
    bool isPowerOfTwo(long long int n) {
        if(n == 1){
            return true;
        }

        if( n < 1 || n % 2 != 0){
            return false;
        }
        return isPowerOfTwo(n/2);
    }
};
