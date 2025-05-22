import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
w1=cq.Workplane('XY',origin=(0,0,35))
r=w0.sketch().segment((-60,-59),(-7,-100)).segment((34,-48)).segment((-20,-7)).close().assemble().reset().face(w0.sketch().segment((-15,30),(-2,13)).segment((-2,4)).segment((4,4)).segment((25,-23)).segment((60,4)).segment((42,26)).segment((42,100)).segment((-2,100)).segment((-2,40)).close().assemble()).finalize().extrude(-15).union(w1.workplane(offset=-89/2).moveTo(-30,-15).cylinder(89,27))