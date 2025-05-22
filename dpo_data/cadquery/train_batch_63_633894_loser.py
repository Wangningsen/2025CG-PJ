import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-25))
w1=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().segment((-51,-100),(-25,-100)).segment((-25,-46)).arc((-23,-40),(-25,-35)).segment((-25,100)).segment((-51,100)).close().assemble().finalize().extrude(35).union(w1.sketch().push([(16,69)]).rect(70,44).push([(28,80)]).circle(4,mode='s').finalize().extrude(31))