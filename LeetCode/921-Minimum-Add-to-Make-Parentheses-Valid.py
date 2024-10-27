class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        st = []
        ans = 0

        for i in s:
            if i == "(":
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    ans += 1
        ans += len(st)
        return ans