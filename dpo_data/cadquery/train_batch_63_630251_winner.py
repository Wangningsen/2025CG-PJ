import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().circle(100).push([(-85.5,25)]).rect(7,18,mode='s').reset().face(w0.sketch().segment((-34,-78),(22,-78)).segment((22,-55)).arc((-6,-55),(-34,-46)).close().assemble(),mode='s').finalize().extrude(14)