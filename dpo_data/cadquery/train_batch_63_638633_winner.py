import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().segment((-100,-2),(-70,-2)).arc((0,-70),(70,-2)).segment((100,-2)).segment((100,2)).segment((70,2)).arc((69,7),(68,10)).arc((12,8),(17,68)).arc((-45,54),(-70,2)).segment((-100,2)).close().assemble().finalize().extrude(80)