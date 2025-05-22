import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().segment((-92,-26),(-50,55)).arc((-95,24),(-92,-26)).assemble().reset().face(w0.sketch().arc((-45,-50),(1,-16),(-4,31)).close().assemble()).push([(90.5,-11)]).rect(19,88).push([(87.5,23)]).rect(13,10,mode='s').finalize().extrude(52)