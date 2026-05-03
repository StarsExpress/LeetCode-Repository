---
title: "3430. Subarrays Max Min Sum"
---


import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from '@theme/CodeBlock';
import CppCode from './subarrays_max_min_sum.cpp?raw';
import PyCode from './subarrays_max_min_sum.py?raw';


### [Maximum and Minimum Sums of at Most Size K Subarrays](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/description/)
第3430号题纯看通过率属于 __非常硬的那种档次 才25%上下而已__

不过其实稍加思索会发现这题考的 不过就是两件事：

1. __有没有熟悉单调栈的基本特质__
2. __能不能进一步把单调栈和其他数据结构合而为一__


### 如何让遍历逻辑更加便利？
由于题目给的任务是在输入的整数数组中 __把所有长度不超过自然数$k$的子数组 各自之最大值和最小值找出来__

接著对这群最大值与最小值求和回传一个整数 那么我们遍历原始数组的时候 最轻松的作法便是由

__每次迭代到的索引$i$作为子数组的结尾 看看全部符合如此条件的子数组__

各自的最大值和最小值是多少 这样自然能不多不少刚刚好掌握正确信息

当然本题有限制了子数组的 __长度不超过$k$__ 迭代时需要 __管制当前结尾索引$i$能搭配的起始索引$j$__

我个人面对扫描子数组之类风格题目时 向来习惯 __让迭代到的索引$i$作为子数组的结尾__

往前看 __该如何过滤起始索引$j$ 包含移动、计数、求和甚至是相乘__ 这样做的最大好处是

遍历的逻辑确实变得非常便利 不仅是为了 __便利遍历__ 这种谐音梗而已😉

### 高效率的判别子数组最大值最小值
#### 1. 起点：预设情况
每当轮到索引$i$作为子数组的结尾时 我们做的第一件事就是：

一、边界管制 算出哪些索引$j$能 __合法地__ 搭配$i$ 组成长度不超过$k$的子数组

说的是那些大于等于$max(0, i - k + 1)$的索引$j$ 一旦敲定好$j$的范围后 接下来的难点是

二、我们如何高效率地算出这俩个总和呢：

1. $MaxSum_i = \Sigma_{j = max(0, i - k + 1)}^i max(nums[j: i + 1])$ 此乃索引$i$作结尾的所有合法子数组 它们各自最大值和
2. $MinSum_i = \Sigma_{j = max(0, i - k + 1)}^i min(nums[j: i + 1])$ 此乃索引$i$作结尾的所有合法子数组 它们各自最小值和

对于$MaxSum_i$ __不妨先从预设情况开始 也就是$MaxSum_i$直接拿了$MaxSum_{i - 1}$的值__ 再做两个调整：

__永远会发生的调整__：加上$nums[i]$这个新来的元素 作为最大值的贡献 毕竟现在多出一个仅有$nums[i]$的子数组了

__特定条件才上演的调整__：如果$i > k - 1$的话 那么就要把$nums[i - k]$这个元素的贡献给扣掉了

__因为$nums[i - k: i]$这个长度k的子数组__ 在子数组结尾为$i - 1$时刚好合法

现如今必须给$nums[i]$入列 __就只能请最左端的$nums[i - k]$退休__ 这也是为何会要先做边界管制

上述这些操作都安排好了 尔后再去扫描看看有没有其他要调整的加减项

#### 2. 加减过程：逐步比大小检查交接
都说了索引$i$作为结尾 那索引$i$的元素必然参与了全部这些合法的子数组 因此如果$nums[i] >= nums[i - 1]$的话 (1)

这些子数组的最大值就完全不可能是$nums[i - 1]$了 __因为它们必经索引$nums[i]$ 而$nums[i - 1]$被$nums[i]$压下去了__

至于我为何在不等式(1)中放入等号呢？咱们遍历是由左往右的

__如果相邻俩元素值一样的话 那选新来的更好啊～人家比较晚来 更加新鲜更能久留嘛😁__

由此可知 如此的情况下 $nums[i - 1]$它在索引$i - 1$为结尾的那些合法子数组中 做了那$l$遍的最大值

__这$l$遍要从此全额转交给$nums[i]$来当最大值了__ 因此会产生

__$(nums[i] - nums[i - 1]) * l$__ 这么多的净增量 给到$MaxSum_i$

刚才这样说的转交概念 要做类比的话 大概就是1992年美国男篮梦之队始祖

Michael Jordan双手放在Magic Johnson还有Larry Bird肩膀上 说的那句：

"Guys, there's a new sheriff in town." (翻译：『兄弟们，城中来了新警长，新老大嘿～你们可光荣卸任啰！😉』)

![New Sheriff](new_sheriff.png)

$nums[i]$既然能通过比较让$nums[i - 1]$退位

那么$nums[i - 2], ...., nums[max(0, i - k + 1)]$也要和$nums[i]$比一比了

比到啥时停下来？__从i - 1往左比到第一个比$nums[i]$大的元素$nums[j]$为止__

__因为后续的元素都比$nums[j]$更大 $nums[i]$自然赢不了 这不就是个单调递减栈负责的事吗？__

一路向左和那些不比自己大的元素交接 把它们打出栈后 才轮到$nums[i]$入栈

$MaxSum_i$既然能如此靠单调递减栈实时追踪数额 那$MinSum_i$当然也能靠单调递增栈搞定了

__只不过它的转交判别是反过来的 如果$nums[i] <= nums[i - 1]$的话才要发动交接仪式 (2)__

__和$MaxSum_i$的转交判别式(1) $nums[i] >= nums[i - 1]$颠倒了不等号～～__

最后题目想要我们给的答案 自然就是 __$\Sigma_{i = 0}^{n - 1} (MaxSum_i + MinSum_i)$了__

然而我前面有提到 每个迭代都要管制边界 把不在目前合法子数组范围内的元素剔除掉

__这个剔除是先进先出的过程 因此我们可把单调栈与队列合而为一 用Deque来同时拥有先进先出和后进先出的行为__

![Max Min Stacks Efficiency](3430_efficiency.png)
代码效能还是非常极速的 每个元素都仅要入双栈各一次 出双栈次数加起来最多为2 时空复杂度自然均是$O(n)$啰✌️✌️

<Tabs>
  <TabItem value="cpp" label="C++">
    <CodeBlock language="cpp">{CppCode}</CodeBlock>
  </TabItem>

  <TabItem value="python" label="Python" default>
    <CodeBlock language="python">{PyCode}</CodeBlock>
  </TabItem>
</Tabs>
