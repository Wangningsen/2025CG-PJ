import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().push([(-41,-15)]).circle(17).reset().face(w0.sketch().segment((52,-6),(53,-12)).segment((58,-12)).segment((57,-6)).close().assemble()).finalize().extrude(-84).union(w1.sketch().segment((-33,28),(-33,29)).segment((-32,29)).segment((-32,28)).arc((-30,31),(-33,28)).assemble().finalize().extrude(140))