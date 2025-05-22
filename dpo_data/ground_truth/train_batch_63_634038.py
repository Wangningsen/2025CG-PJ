import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().push([(-82,-3.5)]).rect(36,93).reset().face(w0.sketch().segment((53,17),(92,44)).arc((62,46),(53,17)).assemble()).reset().face(w0.sketch().arc((59,8),(90,6),(98,35)).close().assemble()).finalize().extrude(45)