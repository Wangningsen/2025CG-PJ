import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((-89,-40),(-87,-100)).segment((-79,-100)).segment((-81,-40)).close().assemble().finalize().extrude(-87).union(w1.sketch().push([(28,55)]).rect(122,90).reset().face(w1.sketch().segment((25,30),(30,30)).segment((30,44)).arc((28,43),(25,44)).close().assemble(),mode='s').reset().face(w1.sketch().arc((25,66),(28,67),(30,66)).segment((30,80)).segment((25,80)).close().assemble(),mode='s').finalize().extrude(30))