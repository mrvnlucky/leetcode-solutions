class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> distinctCandies(candyType.begin(), candyType.end());
        int maxDistinctTypes = distinctCandies.size();
        int totalCandies = candyType.size();
        
        return min(maxDistinctTypes, totalCandies/2);
    }
};