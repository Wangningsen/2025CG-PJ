import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().arc((-38,-9),(-98,-54),(-23,-56)).segment((-19,-56)).arc((-21,-55),(-22,-53)).arc((-21,-36),(-27,-20)).arc((-24,-14),(-19,-9)).close().assemble().finalize().extrude(-80).union(w0.sketch().push([(-29.5,77)]).rect(25,10).rect(9,8,mode='s').finalize().extrude(39)).union(w1.sketch().segment((24,-10),(73,-10)).segment((73,54)).segment((24,54)).segment((24,51)).arc((25,48),(24,44)).close().assemble().finalize().extrude(69))