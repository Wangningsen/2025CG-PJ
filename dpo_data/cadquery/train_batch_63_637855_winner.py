import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((-89,-40),(-87,-100)).segment((-79,-100)).segment((-81,-40)).close().assemble().finalize().extrude(-87).union(w1.sketch().push([(28,55)]).rect(122,90).reset().face(w1.sketch().segment((26,32),(29,32)).segment((29,31)).segment((30,31)).segment((30,32)).segment((33,32)).segment((33,38)).segment((30,38)).segment((30,40)).segment((29,40)).segment((29,38)).segment((26,38)).close().assemble(),mode='s').push([(28,73.5)]).rect(4,13,mode='s').finalize().extrude(30))