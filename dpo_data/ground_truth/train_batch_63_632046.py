import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
r=w0.sketch().push([(69.5,46.5)]).rect(61,27).reset().face(w0.sketch().segment((62,48),(66,40)).segment((77,45)).segment((73,53)).close().assemble(),mode='s').finalize().extrude(-81).union(w0.sketch().segment((-100,-53),(-84,-60)).arc((-88,-48),(-100,-53)).assemble().finalize().extrude(-24))