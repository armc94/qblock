from py2neo import Graph, Node, Relationship

graph = Graph(host="127.0.0.1", port=7687, password='useruser22', user='neo4j')

task1 = Node("Task", title="do this...2", storypoints=4)
task2 = Node("Task", title="do that...2", storypoints=8, date="few days ago")
task1.add_label('ToDo')
graph.create(task1)
graph.create(task2)

rel = Relationship(task1, "done_before", task2)
rel['when'] = 'soon'
graph.create(rel)
