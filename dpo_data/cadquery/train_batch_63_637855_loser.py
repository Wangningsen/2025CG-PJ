import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().segment((-89,-40),(-87,-100)).segment((-79,-100)).segment((-81,-40)).close().assemble().finalize().extrude(-87).union(w1.sketch().push([(28,55)]).rect(122,90).rect(4,50,mode='s').finalize().extrude(-30))