import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().segment((-62,-62),(-51,-62)).segment((-51,-100)).segment((51,-100)).segment((51,-62)).segment((62,-62)).segment((62,62)).segment((51,62)).segment((51,100)).segment((-51,100)).segment((-51,62)).segment((-62,62)).close().assemble().push([(19,13)]).circle(34,mode='s').finalize().extrude(-63)