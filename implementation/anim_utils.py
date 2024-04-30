from manim import *
import typing as ty
import numpy as np
import networkx as nx

class LabeledEdge(Line):
    def __init__(self, start, end, label, **kwargs) -> None:
        
        super().__init__(start, end, **kwargs)
        
        cost_label = Text(label).scale(0.5)
        cost_label.next_to((self.start+self.end)/2, UP)
        cost_label.rotate(self.get_angle())

        self.add(cost_label)


class VertexWithHeuristic(LabeledDot):
    def __init__(self, heuristic, label_pos, **kwargs,) -> None:
        
        super().__init__(**kwargs)
        
        heuristic_label = Text(heuristic, color=BLUE).scale(0.5)
        heuristic_label.next_to(self.arc_center, label_pos,buff=0.7)

        self.add(heuristic_label)

class AnimationFactory:
    def __init__(self, 
                 graph: nx.DiGraph, 
                 partitions: ty.List[ty.List[str]],
                 heuristic_label_pos: ty.Dict[str, np.ndarray],
                 scene: Scene) -> None:
        
        self.nxgraph = graph

        self.partitions = partitions

        self.edge_config = { (v,w):{'label': str(graph.edges[v,w]['weight'])} for v,w in graph.edges }
        
        self.vertex_config = { v:{'heuristic': str(graph.nodes[v]['heuristic']), 
                                  'label_pos': heuristic_label_pos[v]
                                  } for v in graph.nodes } 

        self.scene = scene

        self.cur_graph = self.graph_factory()

        self.scene.add(self.cur_graph)

        self.cur_graph.shift(RIGHT)
        
        self.pqueue = VGroup()

        self.pqueue_title = Text('Priority Queue', weight=BOLD).scale(0.5)

        self.pqueue_title.next_to(self.cur_graph, LEFT, buff=1)

        self.pqueue.add(self.pqueue_title)
        
        self.pqueue_contents = VGroup()

        self.pqueue.add(self.pqueue_contents)

        self.pqueue_contents.next_to(self.pqueue_title, DOWN)

        self.scene.add(self.pqueue)

        self.scene.play(Create(self.cur_graph))

        self.scene.wait()

    def graph_factory(self) -> DiGraph: 
        return DiGraph.from_networkx(self.nxgraph, 
            labels=True, 
            layout_scale=3,
            layout='partite',
            partitions=self.partitions,
            edge_type=LabeledEdge,
            edge_config=self.edge_config,
            vertex_type=VertexWithHeuristic,
            vertex_config=self.vertex_config
            )

    def step(self) -> None:
        new_graph = self.graph_factory()
        
        self.scene.add(new_graph)

        new_graph.shift(RIGHT)

        self.scene.play(ReplacementTransform(self.cur_graph, new_graph))
        self.cur_graph = new_graph

    def update_pqueue(self, new_queue: ty.List[ty.Tuple[int, str]]) -> None:

        new_pqueue_contents = VGroup()

        if len(new_queue) != 0:

            prev_item = MathTex(new_queue[0][1] + r',\quad\hat{f}(' + f'{new_queue[0][1]}) = {new_queue[0][0]}').scale(0.5)
            new_pqueue_contents.add(prev_item)
            
            if len(new_queue) > 1:
                for fhat_val, vertex in new_queue[1::]:
                    entry = MathTex(vertex + r',\quad\hat{f}(' + f'{vertex}) = {fhat_val}').scale(0.5)
                    entry.next_to(prev_item, DOWN)
                    new_pqueue_contents.add(entry)
                    prev_item = entry

        
        self.scene.play(FadeOut(self.pqueue_contents))
        self.pqueue.add(new_pqueue_contents)
        new_pqueue_contents.next_to(self.pqueue_title, DOWN)
        self.pqueue.remove(self.pqueue_contents)
        self.scene.play(FadeIn(new_pqueue_contents))
        self.scene.wait(duration=2.0)

        self.pqueue_contents = new_pqueue_contents
