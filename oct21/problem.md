

As we have twice before, we find ourselves engrossed in a robot sports competition. In the Robot Swimming Trials, 3N identical robots compete for N equivalent spots in the finals by swimming N races. Each robot precommits to spending a certain amount of its fuel in each race. After all the races are run, the spots in the finals are given to the winners of the races, moving from the fastest winner to the slowest. (Once a robot wins a race, it is ineligible to win another race.) A robot’s speed is strictly increasing in the amount of fuel it spends, and ties are broken by randomly choosing the winner among the robots that have spent the same amount of fuel.

Mathematically speaking, the 3N robots each submit a strategy, which is an N-tuple of nonnegative real number “bids” summing to 1, representing the fuel burned in each of the N races. The winners of the races are then determined from the highest bid (across all races and all robots) on down, with ties broken randomly. Once a robot wins a race their other bids are deleted, so we are guaranteed to get N distinct qualifiers for the finals.

For example, suppose N=3 and the 3N=9 robots submit their strategies as
Robot 	       Race 1	Race 2	Race 3  
Automatonya   	0.6 	0.1 	0.3
Botty 	        0.6 	0.3 	0.1
Chroma 	        0 	    1 	    0
Data    	    0.3 	0.5 	0.2
Electro 	    0.2 	0.8 	0
Fernandroid 	0.4 	0.5 	0.1
Gregulator 	    0.5 	0.5 	0
Hannanobot 	    0 	    0.9 	0.1
IO 	            0.2 	0.7 	0.1

The second race gets resolved first because Chroma’s bid of 1 is the highest overall, and Chroma is declared the winner of that time trial. Next, the first race is resolved because 0.6 is the highest remaining bid (we ignore the 0.9, 0.8, and 0.7 in the second race because it already has a winner). We flip a fair coin to determine who is the winner between Automatonya and Botty; say that Automatonya gets lucky and is declared the winner. Then the third race is decided, and Data is declared the winner, because 0.2 is the highest bid among robots that have not yet won (Automatonya’s 0.3 is ignored).

Over the storied history of the RST, the metagame settled into what was widely believed to be the Nash equilibrium: each robot uniformly randomly selects a race and devotes all of their fuel to it. Let’s call this the discrete strategy. However, rumors are circulating that this conventional wisdom is not entirely accurate: for a large enough N, the discrete strategy is not the Nash equilibrium. You’ve been tasked to find two pieces of information:

What is the smallest N for which the trial does not have the discrete strategy as the Nash equilibrium?

For this N, if the other 3N-1 robots naively play the discrete strategy and your robot plays optimally (exploiting this knowledge of your opponents’ strategies), with what probability p will you make the finals (rounded to 6 significant digits)?

Please submit your answer in the form “N, p”.

