import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().arc((-37,2),(0,-100),(34,0)).arc((4,88),(-37,2)).assemble().push([(35,33)]).circle(16,mode='s').finalize().extrude(-47).union(w0.sketch().segment((-46,73),(-2,1)).segment((58,38)).segment((-8,100)).close().assemble().finalize().extrude(8))