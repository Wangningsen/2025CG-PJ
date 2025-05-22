import cadquery as cq
w0=cq.Workplane('YZ',origin=(91,0,0))
r=w0.sketch().segment((-71,18),(-59,18)).arc((-52,-40),(-6,-70)).segment((-6,-100)).segment((15,-100)).segment((15,-70)).arc((70,-16),(34,55)).segment((34,100)).segment((-71,100)).close().assemble().push([(-57,41)]).circle(11,mode='s').finalize().extrude(-182)