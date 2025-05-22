import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-86,0))
r=w0.sketch().segment((-64,-59),(-28,-100)).segment((-2,-77)).segment((-64,-11)).close().assemble().finalize().extrude(96).union(w0.sketch().push([(7,43)]).circle(57).reset().face(w0.sketch().segment((-44,51),(10,-5)).segment((53,29)).segment((5,94)).close().assemble(),mode='s').finalize().extrude(171))