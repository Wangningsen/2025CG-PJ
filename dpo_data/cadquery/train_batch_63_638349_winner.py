import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().segment((-26,-100),(26,-100)).segment((26,-11)).arc((0,100),(-26,-11)).close().assemble().push([(-15.5,-83)]).rect(5,10,mode='s').finalize().extrude(-37).union(w0.sketch().segment((-26,-74),(-18,-84)).segment((31,-42)).segment((22,-32)).close().assemble().finalize().extrude(69))