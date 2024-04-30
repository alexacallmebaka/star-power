# A* brought to life! 💫

To run my implementation, you will need to install the modules in `requirements.txt`.
If you only care about the algorithm itself, `a_star.py` is the only file you need to concern yourself with.
However, `examples.py` might be useful to read through as well as I created a couple different NetworkX
graphs that could be input to the algorithm to test it. Within, you can see how heuristics are attached to the
vertices of a graph.

Not only does my implementation run `A*`... it also generates animations of `A*` being run using
[3Blue1Brown](https://www.3blue1brown.com/)'s mathematical animation library [manim](https://www.manim.community/).
It does this *while* the algorithm is being run. This is how I got the animations for my talk!
I won't ramble about that too much in this file, but the rest of the files here correspond to 
that stuff (also anything you see corresponding to `anim_factory` in the `A*` implementation). 

Enjoy! 🍻
