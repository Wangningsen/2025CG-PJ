import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=59/2).moveTo(-57,69).cylinder(59,31).union(w0.sketch().arc((31,-51),(49,-93),(88,-97)).segment((69,-97)).arc((46,-84),(31,-59)).close().assemble().finalize().extrude(90))