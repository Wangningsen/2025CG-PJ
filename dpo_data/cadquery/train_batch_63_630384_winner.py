import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().segment((-63,21),(-39,21)).arc((-24,-13),(12,-27)).arc((16,-25),(19,-28)).segment((19,-100)).segment((63,-100)).segment((63,14)).segment((59,14)).arc((54,44),(28,68)).segment((28,78)).segment((-34,78)).segment((-34,100)).segment((-63,100)).close().assemble().push([(-59,75.5)]).rect(6,5,mode='s').finalize().extrude(-81)