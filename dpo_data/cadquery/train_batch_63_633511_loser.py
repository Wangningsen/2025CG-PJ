import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().arc((22,-100),(36,-84),(31,-63)).close().assemble().finalize().extrude(84).union(w0.workplane(offset=90/2).moveTo(-25,88).cylinder(90,12))