import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().arc((46,55),(60,31),(77,55)).close().assemble().finalize().extrude(7).union(w0.sketch().push([(-63,43)]).rect(74,96).push([(-52.5,-25.5)]).rect(57,11).reset().face(w0.sketch().segment((-24,-91),(100,-91)).segment((100,-18)).segment((28,-18)).segment((28,58)).segment((-8,58)).segment((-8,-20)).segment((-24,-20)).close().assemble()).finalize().extrude(79)).union(w1.sketch().push([(60,2)]).circle(30).circle(15,mode='s').finalize().extrude(7))