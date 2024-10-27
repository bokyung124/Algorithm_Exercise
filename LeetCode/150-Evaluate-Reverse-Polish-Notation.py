class Solution(object):
    import operator

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        def is_number(s):
            return s.lstrip('-').isdigit()
        
        st = []
        op = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(float(x) / y) 
        }
        
        for i in tokens:
            if is_number(i):
                st.append(int(i))
            else:
                num2 = st.pop()
                num1 = st.pop()
                st.append(op[i](num1, num2))

        return st[0]