import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().push([(-32,-64)]).circle(36).reset().face(w0.sketch().segment((-6,50),(68,50)).segment((68,80)).segment((31,80)).arc((18,96),(-4,99)).arc((5,91),(9,80)).segment((-6,80)).close().assemble()).push([(32,65)]).circle(11,mode='s').finalize().extrude(-27).union(w1.sketch().segment((12,-18),(15,-18)).arc((-7,-1),(16,-17)).segment((16,-10)).segment((12,-10)).close().assemble().finalize().extrude(-41))