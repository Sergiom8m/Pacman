# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from abc import ABC, abstractmethod

import util


class SearchProblem(ABC):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    @abstractmethod
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    @abstractmethod
    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """

    "*** YOUR CODE HERE ***"
    initialState = problem.getStartState()
    visitedNodes = set()
    unvisitedNodes = util.Stack()

    # Cada elemento es una tupla que tiene un estado y las acciones para llegar a él
    unvisitedNodes.push((initialState, []))

    # Recorrer los elementos de la pila
    while not unvisitedNodes.isEmpty():

        # Extraer de la pila el siguiente elemento (estado) + acciones
        actualState, actions = unvisitedNodes.pop()

        # Comprobar si el estado actual es un estado final
        if problem.isGoalState(actualState):
            # Sí es un estado final devolver las acciones para llegar a el
            return actions

            # Solo visitar aquellos nodos que no hayan sido visitados antes
        if actualState not in visitedNodes:

            # Añadir los nodos que se visitan a la lista de visitados
            visitedNodes.add(actualState)

            # Obtener los sucesores del estado actual
            successors = problem.getSuccessors(actualState)

            for successor, action, _ in successors:  # El coste no se va a usar para nada en este caso

                # Añadir sucesores con las acciones actualizadas
                unvisitedNodes.push((successor, actions + [action]))

                # Si no quedan elementos en la cola y no ha habido ningun estado final, no hay camino
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    initialState = problem.getStartState()
    visitedNodes = set()
    unvisitedNodes = util.Queue()

    # Cada elemento es una tupla que tiene un estado y las acciones para llegar a él
    unvisitedNodes.push((initialState, []))

    # Recorrer los elementos de la cola
    while not unvisitedNodes.isEmpty():

        # Extraer de la cola el siguiente elemento (estado) + acciones
        actualState, actions = unvisitedNodes.pop()

        # Comprobar si el estado actual es un estado final
        if problem.isGoalState(actualState):

            # Sí es un estado final devolver las acciones para llegar él
            return actions

        # Solo visitar aquellos nodos que no hayan sido visitados antes
        if actualState not in visitedNodes:

            # Añadir los nodos que se visitan a la lista de visitados
            visitedNodes.add(actualState)

            # Obtener los sucesores del estado actual
            successors = problem.getSuccessors(actualState)

            for successor, action, _ in successors:  # El coste no se va a usar para nada en este caso

                # Añadir sucesores con las acciones actualizadas
                unvisitedNodes.push((successor, actions + [action]))

    # Si no quedan elementos en la cola y no ha habido ningun estado final, no hay camino
    return []


def uniformCostSearch(problem):
    """*** YOUR CODE HERE ***"""

    initialState = problem.getStartState()
    visitedNodes = set()
    unvisitedNodes = util.PriorityQueue()

    # Cada elemento es una tupla que tiene otra tupla (estado, acciones, costes) y un int (valor de prioridad)
    unvisitedNodes.push((initialState, [], 0), 0)

    # Recorrer los elementos de la cola de prioridad
    while not unvisitedNodes.isEmpty():

        # Extraer de la cola de prioridad el siguiente elemento (estado + acciones + costes) + valor de prioridad
        actualState, actions, costs = unvisitedNodes.pop()

        # Comprobar si el estado actual es un estado final
        if problem.isGoalState(actualState):

            # Sí es un estado final devolver las acciones para llegar él
            return actions

        # Solo visitar aquellos nodos que no hayan sido visitados antes
        if actualState not in visitedNodes:

            # Añadir los nodos que se visitan a la lista de visitados
            visitedNodes.add(actualState)

            # Obtener los sucesores del estado actual
            successors = problem.getSuccessors(actualState)

            for successor, action, cost in successors:

                # Añadir sucesores con las acciones actualizadas
                unvisitedNodes.push((successor, actions + [action], costs + cost), costs + cost)

    # Si no quedan elementos en la cola de prioridad y no ha habido ningun estado final, no hay camino
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    initialState = problem.getStartState()
    visitedNodes = set()
    unvisitedNodes = util.PriorityQueue()

    # El valor del heuristico será la distancia desde el estado actual hasta el objetivo
    dist_heuristic = heuristic(initialState, problem)

    # Cada elemento es una tupla que tiene otra tupla (estado, acciones, costes) y un int (valor de prioridad)
    unvisitedNodes.push((initialState, [], 0), dist_heuristic)

    # Recorrer los elementos de la cola de prioridad
    while not unvisitedNodes.isEmpty():

        # Extraer de la cola de prioridad el siguiente elemento (estado + acciones + costes) + valor de prioridad
        actualState, actions, costs = unvisitedNodes.pop()

        # Comprobar si el estado actual es un estado final
        if problem.isGoalState(actualState):

            # Sí es un estado final devolver las acciones para llegar él
            return actions

        # Solo visitar aquellos nodos que no hayan sido visitados antes
        if actualState not in visitedNodes:

            # Añadir los nodos que se visitan a la lista de visitados
            visitedNodes.add(actualState)

            # Obtener los sucesores del estado actual
            successors = problem.getSuccessors(actualState)

            for successor, action, cost in successors:

                # Calcular el valor del heuristico para cada caso concreto
                dist_heuristic = heuristic(successor, problem)

                # Añadir sucesores con las acciones actualizadas
                unvisitedNodes.push((successor, actions + [action], costs + cost), costs + cost + dist_heuristic)

    # Si no quedan elementos en la cola de prioridad y no ha habido ningun estado final, no hay camino
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
