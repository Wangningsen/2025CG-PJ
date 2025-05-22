import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().segment((-100,-10),(-46,-10)).arc((0,-47),(46,-10)).segment((100,-10)).segment((100,10)).segment((46,10)).arc((0,47),(-46,10)).segment((-100,10)).close().assemble().finalize().extrude(-44).union(w0.sketch().rect(152,72).push([(50.5,17.5)]).rect(13,29,mode='s').finalize().extrude(50))