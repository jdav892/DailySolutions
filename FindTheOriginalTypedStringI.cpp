class Solution {
public:
    int possibleStringCount(string word) {
        int counter = 1;
        for(int i = 1; i < word.size(); i++){
            if(word[i - 1] == word[i]){
                counter += 1;
            }
        }
        return counter;
    };
};