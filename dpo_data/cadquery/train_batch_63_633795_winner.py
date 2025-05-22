import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.workplane(offset=-137/2).cylinder(137,69).union(w1.sketch().arc((27,-18),(55,41),(27,100)).segment((27,64)).arc((42,41),(27,18)).close().assemble().finalize().extrude(25))