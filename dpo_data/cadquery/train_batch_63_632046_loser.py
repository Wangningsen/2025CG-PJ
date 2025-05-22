import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().push([(69.5,46.5)]).rect(61,27).reset().face(w0.sketch().segment((63,46),(65,42)).segment((77,45)).segment((74,54)).segment((63,50)).arc((63,48),(64,47)).close().assemble(),mode='s').finalize().extrude(-82).union(w0.sketch().segment((-100,-53),(-84,-60)).arc((-87,-48),(-100,-53)).assemble().finalize().extrude(-25))