import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().push([(69.5,46.5)]).rect(61,27).reset().face(w0.sketch().segment((62,47),(66,40)).segment((77,45)).segment((73,53)).close().assemble(),mode='s').finalize().extrude(-82).union(w0.sketch().segment((-100,-53),(-83,-60)).arc((-86,-50),(-100,-53)).assemble().finalize().extrude(-25))