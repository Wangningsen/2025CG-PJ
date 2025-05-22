import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(-95,60)]).circle(5).reset().face(w0.sketch().segment((-39,-52),(-1,-58)).segment((-1,-26)).segment((34,-25)).arc((99,-40),(39,-11)).segment((39,-9)).segment((-32,0)).close().assemble()).finalize().extrude(-54)