<div id="chebyshev_optimization">
<h2><a href="https://github.com/leoncyao/chebyshev_optimization">Integer Chebyshev Problem</a></h2>

Let the supremum norm of a polynomial over the domain <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/21fd4e8eecd6bdf1a4d3d6bd1fb8d733.svg?invert_in_darkmode" align=middle width=8.51598pt height=22.46574pt/> be given by 

<p align="center"><img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/fef6b455bc6467a0acfdc1adca262926.svg?invert_in_darkmode" align=middle width=145.24785pt height=26.99862pt/></p>

We want to find the polynomial the minimizes this norm. 
<br>
Formally, this means we want to solve the problem

<p align="center"><img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/77eff370de2749bbbc35708cdce65090.svg?invert_in_darkmode" align=middle width=178.6125pt height=31.415505pt/></p>

where the optimal value for a given <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.867pt height=14.15535pt/> is denoted <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/1d642a0bc678e4c10415af2c79eee9cf.svg?invert_in_darkmode" align=middle width=47.760735pt height=24.6576pt/>. <br>
We can then take the limit as <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/5b1d0e6cb391219b21d53d5848fe80a9.svg?invert_in_darkmode" align=middle width=51.876pt height=14.15535pt/> and we will call this limit the <b>Integer Chebyshev Constant</b> denoted,

<p align="center"><img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/a0944b5203ba3c9cc7f70d56b7b4819a.svg?invert_in_darkmode" align=middle width=138.177765pt height=22.19184pt/></p>

Inside this <a href="https://github.com/leoncyao/chebyshev_optimization">repo</a>, you can find a python script called <b>chebyshev.py</b> which uses the gurobi library to solve this problem. <br><br>
Specifically, you can run <br><br>

<b>python chebyshev.py</b> <br><br>

to calculate the optimum value for <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/a2b83378f3a851a69124cae9e0f695fc.svg?invert_in_darkmode" align=middle width=40.003755pt height=21.18732pt/> <br><br>

The script doesn't actually calcluate the above equation, as taking the min of function which itself is a max of a polynomial is quite tricky to optimize. Instead, becomes of how nice polynomials are, we can directly calculate the minimum and maximum values of the polynomial. 

For the case of <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/da60d8ce586cf444dfc2735588ee6cab.svg?invert_in_darkmode" align=middle width=40.003755pt height=21.18732pt/>, we know that the maximum and minimum values of the quadratic <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/83941ef837b20958734f13c92418df5b.svg?invert_in_darkmode" align=middle width=141.5733pt height=26.76201pt/> must either be at the endpoints <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/bfd4c9c32b22716d81631274ca94c912.svg?invert_in_darkmode" align=middle width=65.856285pt height=24.6576pt/>, or at the center, which has <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/09c1b62c2e6a1f700c7b4b072f26124d.svg?invert_in_darkmode" align=middle width=59.753595pt height=28.92648pt/>. <br>
Note that center point can be calculated with calculus, ie take the derivative <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/c1b3df4af3827a23698601369289d043.svg?invert_in_darkmode" align=middle width=110.42988pt height=24.71634pt/> and set it to <img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode" align=middle width=8.219277pt height=21.18732pt/>. \\

It then follows that 
<p align="center"><img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/ae6579657d322cdf41e723cb2d422202.svg?invert_in_darkmode" align=middle width=319.9911pt height=37.206015pt/></p> 
Next, I found that it was difficult to minimize 3 values at once in gurobi, so instead I minimized the squared sum of them 

<p align="center"><img src="https://rawgit.com/leoncyao/chebyshev_optimization/main/svgs/0f693fbc079a8922d5f5f5b8d45bed2c.svg?invert_in_darkmode" align=middle width=173.7054pt height=27.804315pt/></p>


TODO: 
<ul>
<li>Add cases n > 2 </li>
<li>Add option to increase n until value converges within given range</li>
</ul>

<h3>References:</h3>
<ul>
<li>Hare, K. G. , & Hodges, P. W. . (Accepted). <a href="https://uwaterloo.ca/scholar/kghare/publications/applications-integer-and-semi-infinite-programming-integer-chebyshev-problem">Applications of Integer and Semi-Infinite Programming to the Integer Chebyshev Problem</a>. Experimental Mathematics. Retrieved from https://doi.org/10.1080/10586458.2019.1691089
</li>

</ul>




</div>