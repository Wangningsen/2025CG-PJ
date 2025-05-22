import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().push([(-48,-74)]).circle(26).reset().face(w0.sketch().segment((-67,74),(-36,9)).segment((19,34)).segment((-11,100)).close().assemble()).reset().face(w0.sketch().segment((23,-2),(28,-10)).segment((74,17)).segment((69,25)).close().assemble()).finalize().extrude(-82)