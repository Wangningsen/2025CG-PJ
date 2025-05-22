import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=59/2).moveTo(-57,69).cylinder(59,31).union(w0.sketch().arc((31,-51),(46,-91),(88,-97)).arc((49,-87),(31,-51)).assemble().finalize().extrude(90))