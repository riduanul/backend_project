#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int longestSubarrayWithSum(vector<int>& nums, int k) {
  unordered_map<int,int> m;
  int n = nums.size();
  int sum = 0;
  int ans=0;
  
  for(int i=0; i<n; i++){
      sum+= nums[i];
      
      if(sum == k){
        ans = i+1;
      }
      
      if(m.find(sum) == m.end()){ //sub array start from 0th index
        m[sum] = i;
      }
      
      if(m.find(sum-k) != m.end()){
        ans = max(ans, i-m[sum-k]);
      }
      
  }
  return ans;
}

int main() {
    vector<int> nums = {1, -1, 5, -2, 3};
    int target = 3;

    int result = longestSubarrayWithSum(nums, target);
    cout << "Length of the longest subarray: " << result << endl;

    return 0;


}

// we are using only 1 loop t.c = O(n)
// we are using 1 map s.c = O(n)

