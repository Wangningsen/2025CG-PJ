import cadquery as cq
w0=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((-78,14),(75,14)).segment((75,100)).segment((-78,100)).segment((-78,79)).arc((-75,78),(-78,77)).close().assemble().finalize().extrude(-117).union(w0.sketch().segment((33,-100),(78,-100)).arc((77,-94),(77,-89)).segment((33,-89)).close().assemble().finalize().extrude(-75))