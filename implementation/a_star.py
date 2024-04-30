#software package for graphs.
import networkx as nx

#software package for implementing a priority queue
import heapq as hq

#for supporting type hints.
import typing as ty

#for animations.
import manim as mn

#helper class for animations.
import anim_utils as au

#the star of the show.
def a_star(graph: nx.DiGraph, 
           start_vertex: ty.List[str], 
           goal_vertices: ty.Set[str],
           anim_factory: ty.Optional[au.Animation] = None #special class used to create animations of the algorithm running.
           ) -> ty.Tuple[ty.List[str]]:
   
    #store the predecessor of each vertex along an optimal path.
    preds : ty.Dict[str, ty.Optional[str, None]] = {}
    
    #we use float for the distances to allow our default distance on infinity
    #(that's what float('inf') does), this dictionary simulates \hat{g}.
    distances: ty.Dict[str, float] = { vertex:float('inf') for vertex in graph.nodes}

    #the calculated values of \hat{f}, where each entry is a \hat{f}(v),v pair for a vertex v.
    #this will be treated as a priority queue by later functions.
    open_vertices: ty.List[ty.Tuple[int, str]] = []
    
    #add starting vertex to open_vertices and sort like a priority queue.
    hq.heappush(open_vertices, 
                (graph.nodes[start_vertex]['heuristic'], start_vertex)
               )
    
    #if creating animation, update priority queue visual.
    if anim_factory:
        anim_factory.update_pqueue(open_vertices)
    
    #the start vertex is 0 away from the end and has no predecessor.
    distances[start_vertex]: float = 0
    preds[start_vertex]: ty.Optional[str] = None
    
    #main program loop.
    while True:
        #get the vertex with current minimal value of \hat{f}.
        #we don't care about the actual value of \hate{f},
        #so we throw it away.
        
        #if we wanted to be exactly true to A*, we should make
        #sure to always break ties in favor of vertices in the goal
        #set. however, for this implementation and our examples
        #the gain is negligible for the extra computation it would cost.
        cure_vertex: str
        _, cur_vertex = hq.heappop(open_vertices)
        
        if anim_factory:
            
           #update the priority queue visual.
           anim_factory.update_pqueue(open_vertices)

           #change the color of the current vertex.
           anim_factory.vertex_config[cur_vertex]['color']: manim.color = mn.RED
           
           pred: str = preds[cur_vertex]
            
           #if not an isolated vertex, color the edge between this vertex and its predecessor.
           if pred is not None:
               anim_factory.edge_config[pred, cur_vertex]['color']: manim.color = mn.RED
           
           #step forward the animation of the graph (i.e. update colors).
           anim_factory.step()
           
        #set the current vertex to "closed".k
        graph.nodes[cur_vertex]['open']: bool = False
        
        #if a goal vertex, reconstruct the path based on the predecessors of each vertex
        #and return the path.
        if cur_vertex in goal_vertices:
            optimal_path: ty.List[str] = []
            pred: str = cur_vertex

            while pred is not None:
                
                next_pred: str = preds[pred]

                #in the animation, change the path vertices to green.
                if anim_factory:

                    anim_factory.vertex_config[pred]['color']: mn.color = mn.GREEN

                    if next_pred is not None:
                       anim_factory.edge_config[next_pred,pred]['color']: mn.color = mn.GREEN

                optimal_path.append(pred)
                pred: str = next_pred
            
            #since we constructed the path via backtracking, we need to reverse it.
            optimal_path.reverse()
            
            #change graph colors in animation.
            if anim_factory:
                anim_factory.step()

            return optimal_path
        
        #this is equivalent to applying \Gamma to the current vertex.
        for neighbor in nx.neighbors(graph, cur_vertex):
            
            #if g(cur_vertex) + cost of edge to neighbor < g(neighbor)
            #basically, if going through the current vertex gives us a 
            #shorter path to neighbor then update neighbor's predecessor.
            if distances[cur_vertex] + graph.edges[cur_vertex, neighbor]['weight'] < distances[neighbor]:
                distances[neighbor]: float = distances[cur_vertex] + graph.edges[cur_vertex, neighbor]['weight']
                preds[neighbor]: str = cur_vertex
            
            #calculate \hat{f}.
            distance_guess: int = graph.nodes[neighbor]['heuristic'] + distances[neighbor]
            
            #assuming we are using a consistent metric.
            #if the neighbor is not marked open, mark it as open.
            if not graph.nodes[neighbor]['open']:
                graph.nodes[neighbor]['open']: bool = True
            
            #dont care about weight here, so we throw away.
            #if the neighbor is not already in the priority queue, add it.
            if neighbor not in [v for (d,v) in open_vertices]:
                hq.heappush(open_vertices, (distance_guess, neighbor))
                continue
            
            #in other cases, we have already made a guess at the distance
            #so we may want to update if our new guess is better.
            #note this is different than the or in the psuedocode where
            #we reopen a maybe closed node.
            
            #each vertex is only in the queue once so doing index 0 here is okay.
            last_distance_guess: int = [d for (d,v) in open_vertices if v == neighbor][0]
           
            #update \hat{f}(neighbor) if our guess is better and then re-sort priority queue.
            if distance_guess < last_distance_guess:

                open_vertices.remove((last_distance_guess, neighbor))
                open_vertices.insert(0, (distance_guess, neighbor))
                hq.heapify(open_vertices)        

        #update priority queue if pertinent. 
        if anim_factory:
            anim_factory.update_pqueue(open_vertices)
