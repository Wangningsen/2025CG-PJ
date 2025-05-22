import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-83,-47),(10,-47)).arc((96,-25),(48,50)).segment((48,60)).segment((-83,60)).close().assemble().push([(-37,41)]).circle(13,mode='s').finalize().extrude(-29).union(w0.sketch().arc((-100,-45),(-86,-23),(-63,-10)).arc((-77,9),(-100,18)).close().assemble().finalize().extrude(33))