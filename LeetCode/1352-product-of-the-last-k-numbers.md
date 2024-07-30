<h2><a href="https://leetcode.com/problems/product-of-the-last-k-numbers/">1352. Product of the Last K Numbers</a></h2><h3>Medium</h3><hr><p>Design an algorithm that accepts a stream of integers and retrieves the product of the last <code>k</code> integers of the stream.</p>

<p>Implement the <code>ProductOfNumbers</code> class:</p>

<ul>
	<li><code>ProductOfNumbers()</code> Initializes the object with an empty stream.</li>
	<li><code>void add(int num)</code> Appends the integer <code>num</code> to the stream.</li>
	<li><code>int getProduct(int k)</code> Returns the product of the last <code>k</code> numbers in the current list. You can assume that always the current list has at least <code>k</code> numbers.</li>
</ul>

<p>The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.</p>

<p>&nbsp;</p>
<p><strong class="example">Example:</strong></p>

<pre>
<strong>Input</strong>
[&quot;ProductOfNumbers&quot;,&quot;add&quot;,&quot;add&quot;,&quot;add&quot;,&quot;add&quot;,&quot;add&quot;,&quot;getProduct&quot;,&quot;getProduct&quot;,&quot;getProduct&quot;,&quot;add&quot;,&quot;getProduct&quot;]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

<strong>Output</strong>
[null,null,null,null,null,null,20,40,0,null,32]

<strong>Explanation</strong>
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 4 * 10<sup>4</sup></code></li>
	<li>At most <code>4 * 10<sup>4</sup></code> calls will be made to <code>add</code> and <code>getProduct</code>.</li>
	<li>The product of the stream at any point in time will fit in a <strong>32-bit</strong> integer.</li>
</ul>


<br>

## 풀이

- `add` 로 들어온 값은 스트림에 추가
- `getProduct` 를 실행하면 스트림에서 들어온 값 k만큼 pop해서 모두 곱하기

```python
class ProductOfNumbers(object):

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)


    def getProduct(self, k: int) -> int:
        if k > len(self.products) - 1:
            return 0
        return self.products[-1] // self.products[-k-1]
```

- 처음에는 들어온 값을 리스트에 추가한 뒤, 반복문을 이용해 k만큼 꺼내서 모두 곱했지만, 시간 초과로 실패
	- 시간복잡도: O(k)
- 각 숫자가 들어올 때마다 누적 곱을 리스트에 추가하는 방식으로 바꿈!
	- 각 연산의 시간복잡도: O(1)
	- 0이 들어올 경우 누적곱 1로 초기화
		- `getProduct` 에서 k가 현재 리스트 길이보다 짧다면 중간에 0이 들어온 것 -> 0 반환