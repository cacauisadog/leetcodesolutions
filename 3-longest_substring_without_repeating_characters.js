/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let charSet = new Set();
  let left = 0;
  let longest = 0;

  for (let i = 0; i < s.length; i++) {
    while (charSet.has(s[i])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[i]);
    longest = Math.max(longest, charSet.size);
  }
  return longest;
};

console.log(lengthOfLongestSubstring("pwwkew"));
