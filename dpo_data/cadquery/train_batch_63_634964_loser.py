import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,45))
w1=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().segment((0,-67),(100,-67)).segment((100,2)).arc((59,-24),(19,5)).segment((19,17)).segment((0,17)).close().assemble().reset().face(w0.sketch().arc((28,43),(61,60),(95,43)).segment((95,67)).segment((28,67)).close().assemble()).finalize().extrude(-116).union(w0.workplane(offset=-6/2).moveTo(-58,23).cylinder(6,35)).union(w1.workplane(offset=-105/2).moveTo(20,55.5).box(70,31,105))