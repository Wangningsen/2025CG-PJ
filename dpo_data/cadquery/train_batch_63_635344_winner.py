import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
r=w0.sketch().segment((-85,-53),(-34,-53)).segment((-34,-2)).segment((-28,-2)).segment((-28,6)).segment((-34,6)).segment((-34,44)).segment((-85,44)).close().assemble().finalize().extrude(-164).union(w0.sketch().arc((0,-35),(86,-81),(32,1)).arc((-81,74),(0,-35)).assemble().push([(-31,26.5)]).rect(32,99,mode='s').finalize().extrude(-100))