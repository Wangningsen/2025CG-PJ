import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().segment((-26,-100),(26,-100)).segment((26,-11)).arc((52,69),(-26,-11)).close().assemble().push([(-16,-83)]).rect(6,4,mode='s').finalize().extrude(-37).union(w0.sketch().segment((-26,-74),(-18,-84)).segment((31,-42)).segment((24,-32)).segment((3,-50)).arc((-3,-50),(-5,-56)).close().assemble().finalize().extrude(70))