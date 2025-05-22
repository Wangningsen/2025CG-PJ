import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().push([(15.5,-21.5)]).rect(37,85).reset().face(w0.sketch().segment((4,18),(18,-45)).segment((29,-42)).segment((14,20)).close().assemble(),mode='s').finalize().extrude(-26).union(w0.sketch().segment((-100,31),(-64,-43)).segment((-8,-16)).segment((-8,-49)).segment((39,-49)).segment((39,6)).segment((-5,6)).segment((-32,64)).close().assemble().finalize().extrude(64)).union(w1.sketch().push([(56,-55)]).rect(88,18).push([(68,-52)]).circle(1,mode='s').finalize().extrude(-38))