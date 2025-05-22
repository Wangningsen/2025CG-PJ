import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
r=w0.workplane(offset=-100/2).box(50,30,100).union(w0.sketch().segment((-53,-34),(-38,-34)).arc((0,-51),(38,-34)).segment((53,-34)).segment((53,34)).segment((38,34)).arc((0,51),(-38,34)).segment((-53,34)).close().assemble().finalize().extrude(100))