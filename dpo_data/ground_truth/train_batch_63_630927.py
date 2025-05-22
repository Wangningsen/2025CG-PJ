import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((38,-98),(58,-98)).segment((58,-26)).arc((48,-29),(38,-26)).close().assemble().finalize().extrude(165).union(w0.workplane(offset=200/2).moveTo(-35,75).cylinder(200,23))