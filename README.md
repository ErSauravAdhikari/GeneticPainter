# GeneticPainter
An application of genetic algorithm for painter's problem.

![image](https://user-images.githubusercontent.com/69170305/227861668-fdec49f4-4276-4e0e-8f3a-6eb2a4e13343.png)

Fig: AI Generated art of Prompt `Genetic Painter`

### NOTE
I coded this in a hurry, Assignment is due today and there's an exam tommorow so there might be sth wrong with this.

But I think it works, finds the solution in resonable time

### Solution
There can be numerous solution. Every time you try, you might find a new one

Here are the few I found
```
[3, 1, 0, 1, 0, 3, 0, 0, 0, 1, 0, 2, 0, 0, 2, 3, 0, 1, 2, 2, 1, 2, 2, 1, 2, 0, 3, 1, 0, 2, 3, 1, 3, 1, 3, 3, 0, 2, 0, 3, 1, 1, 3, 2, 1, 2, 3, 2, 2, 2, 0, 1, 2, 0]
```

```
[1, 2, 1, 1, 1, 0, 0, 3, 3, 2, 2, 3, 0, 2, 1, 0, 0, 2, 0, 3, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 1, 2, 2, 2, 3, 0, 0, 3, 3, 1, 0, 2, 0, 0, 2, 3, 3, 3, 1, 0]
```

```
[2, 2, 0, 3, 0, 0, 2, 3, 1, 1, 2, 0, 2, 3, 0, 3, 0, 0, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 3, 0, 3, 1, 1, 0, 3, 1, 3, 3, 1, 1, 2, 3, 3, 3, 2, 3, 3, 3, 3, 2, 1, 2, 3]
```

```
[1, 0, 1, 1, 3, 2, 0, 2, 2, 2, 3, 3, 0, 3, 2, 3, 0, 2, 2, 1, 0, 2, 3, 1, 2, 1, 0, 2, 3, 3, 2, 2, 2, 3, 3, 2, 2, 3, 2, 3, 0, 1, 2, 2, 2, 2, 1, 2, 2, 3, 2, 0, 0, 1]
```

### Output
```ps
C:\Users\Saura\PycharmProjects\GALab\venv\Scripts\python.exe C:\Users\Saura\PycharmProjects\GALab\main.py 
The best individual in generation 1 is: 0.96625
The best individual in generation 2 is: 0.9275
The best individual in generation 3 is: 0.8725
The best individual in generation 4 is: 0.91625
The best individual in generation 5 is: 0.92125
The best individual in generation 6 is: 0.9775
The best individual in generation 7 is: 0.96125
The best individual in generation 8 is: 0.97625
The best individual in generation 9 is: 0.99
The best individual in generation 10 is: 0.97375
The best individual in generation 11 is: 0.9775
The best individual in generation 12 is: 0.97875
The best individual in generation 13 is: 0.98625
The best individual in generation 14 is: 0.9975
The best individual in generation 15 is: 0.98375
The best individual in generation 16 is: 0.98625
The best individual in generation 17 is: 0.9875
The best individual in generation 18 is: 0.995
The best individual in generation 19 is: 0.9975
The best individual in generation 20 is: 0.9975
The best individual in generation 21 is: 0.99625
The best individual in generation 22 is: 0.9975
The best individual in generation 23 is: 1.0
Found Solution:  [1, 0, 1, 1, 3, 2, 0, 2, 2, 2, 3, 3, 0, 3, 2, 3, 0, 2, 2, 1, 0, 2, 3, 1, 2, 1, 0, 2, 3, 3, 2, 2, 2, 3, 3, 2, 2, 3, 2, 3, 0, 1, 2, 2, 2, 2, 1, 2, 2, 3, 2, 0, 0, 1]

Process finished with exit code 0
```


### Qn.
Scenario and Problem to be solved
Let’s imagine, we have a painter robot similar to the robot which picked up cans in the lectures.
We will use this robot to paint the floor of a room. To make it interesting, the painter starts at a
random place in the room, and paints continuously. We will also imagine that there is exactly
enough paint to cover the floor. This means that it is wasteful to visit the same spot more than
once or to stay in the same place. To see if there is a optimal set of rules for the painter to follow,
you will create a genetic algorithm. You may write your own code from scratch or use
painter_play.m or painter_play.py as starting points.
As inputs, this function receives
1. A chromosome: A 1x54 array of numbers between 0 and 3 that shows how to respond
(0: no turn, 1:turn left, 2:turn right, 3: random turn left/right) in each of the 54 possible
states. The state is the state of the squares forward/left/right and the current square. Let
[c, f, l, r] denote states of the current square, forward square, left square and right square
respectively. Write 0 for empty, 1 for wall/obstruction and 2 for painted.
Note that c ∈ {0, 2} and f, l, r ∈ {0, 1, 2} so there are 2 × 33 = 54 possible states.
2. An environment: A 2D array representing a rectangular room. Empty (paintable) space is
represented by a zero, while furniture or extra walls are represented by ones. Outside
walls are automatically created by painter_play().

The function painter_play() then uses the rule set to guide a painter, initially placed in the room
with a random position and direction, until the paint can is empty. Note that the painter does not
move when it tries to walk into a wall or furniture. The efficiency (total fraction of paintable
space covered) is then given as an output, as well as the X-Y trajectory (i.e. the positions of the
painter at each time step) of the painter. To see that the painter works, you can try passing it an
empty room for an environment and a trivial chromosome. For example, a chromosome
consisting of all 3s produces a kind of random walk. 
