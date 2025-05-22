import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().push([(-42,13)]).rect(70,18).push([(35,58)]).circle(42).reset().face(w0.sketch().arc((18,54),(27,23),(37,54)).close().assemble(),mode='s').finalize().extrude(66).union(w0.workplane(offset=66/2).moveTo(22,-58).cylinder(66,42))