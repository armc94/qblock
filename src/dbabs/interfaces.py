from django.shortcuts import redirect
from py2neo import Graph, Node, Relationship
import time
import random
from py2neo.ogm import Model, Property, RelatedTo, RelatedFrom, Repository


def create_block(board, column, title, **kwargs):
    graph = Graph(host="127.0.0.1", port=7687, password='useruser22', user='neo4j')

    b = graph.nodes.match('Board', title=board).first()

    block = Node('Block', title=title, timestamp=int(time.time()))
    rel = Relationship(b, "contains", block)

    graph.create(block)
    # graph.create(rel)

    column = graph.nodes.match('Column', title=column).first()

    graph.create(Relationship(column, "contains", block))

def create_column(board, title, **kwargs):
    graph = Graph(host="127.0.0.1", port=7687, password='useruser22', user='neo4j')
    board = graph.nodes.match('Board', title=board).first()
    column = Node('Column', title=title, timestamp=int(time.time()))
    graph.create(column)
    graph.create(Relationship(board, "contains", column))

def create_board(title):
    graph = Graph(host="127.0.0.1", port=7687, password='useruser22', user='neo4j')
    graph.create(Node('Board', title=title))



def test5():
    graph = Graph(host="127.0.0.1", port=7687, password='useruser22', user='neo4j')

    task1 = Node("Task", title="do this...2", storypoints=4)
    task2 = Node("Task", title="do that...2", storypoints=8, date="few daysago")
    task1.add_label('ToDo')
    graph.create(task1)
    graph.create(task2)

    rel = Relationship(task1, "done_before", task2)
    rel['when'] = 'soon'
    graph.create(rel)

def test(request):
    with open("dbabs/test.json", "r") as f:
        content = f.readlines()
        for line in content:
            print(line)

    return redirect('home')

def test2(request):
    new_task = Node('Task', title="do this", stamp=time.time())
    graph.create(new_task)

    return redirect('home')



def get_all_blocks():
    pass
