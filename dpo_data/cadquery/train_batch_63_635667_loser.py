import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((75,-91),(100,-91)).segment((100,-51)).arc((86,-51),(75,-43)).close().assemble().reset().face(w0.sketch().arc((75,-22),(80,-16),(85,-11)).arc((81,-10),(75,-10)).close().assemble()).finalize().extrude(23).union(w0.sketch().segment((-5,65),(-5,84)).arc((-69,-32),(17,66)).close().assemble().finalize().extrude(46))