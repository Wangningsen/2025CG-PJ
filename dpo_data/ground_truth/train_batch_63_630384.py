import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().segment((-63,21),(-39,21)).arc((-21,-16),(19,-26)).segment((19,-100)).segment((63,-100)).segment((63,14)).segment((58,14)).arc((53,46),(28,68)).segment((28,78)).segment((-34,78)).segment((-34,100)).segment((-63,100)).close().assemble().push([(-58.5,76)]).rect(3,6,mode='s').finalize().extrude(-81)