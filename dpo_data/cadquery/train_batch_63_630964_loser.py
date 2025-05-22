import cadquery as cq
w0=cq.Workplane('YZ',origin=(-24,0,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().push([(-44,37)]).circle(56).reset().face(w0.sketch().arc((60,-86),(80,-93),(100,-86)).close().assemble()).reset().face(w0.sketch().segment((60,-40),(100,-40)).arc((80,-33),(60,-40)).assemble()).finalize().extrude(48).union(w1.workplane(offset=25/2).moveTo(-44,37).cylinder(25,23))