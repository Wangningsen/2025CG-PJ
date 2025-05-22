import cadquery as cq
w0=cq.Workplane('YZ',origin=(-93,0,0))
r=w0.sketch().segment((-71,-51),(-71,89)).arc((-100,19),(-71,-51)).assemble().reset().face(w0.sketch().arc((-60,-61),(-42,-72),(-22,-79)).segment((-22,-89)).segment((22,-89)).segment((22,-79)).arc((42,-72),(60,-61)).close().assemble()).reset().face(w0.sketch().arc((71,-51),(100,19),(71,89)).close().assemble()).finalize().extrude(186)