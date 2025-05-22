import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(-95,59)]).circle(5).reset().face(w0.sketch().segment((-39,-53),(-1,-58)).segment((-1,-26)).segment((34,-26)).arc((98,-43),(40,-12)).segment((40,-10)).segment((-32,-1)).close().assemble()).finalize().extrude(-53)