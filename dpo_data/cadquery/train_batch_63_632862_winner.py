import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((-100,-31),(-72,-31)).arc((-50,-41),(-28,-31)).segment((-1,-31)).segment((-1,-23)).segment((80,-44)).segment((100,29)).segment((11,53)).segment((-1,6)).segment((-1,7)).segment((-28,7)).arc((-50,17),(-72,7)).segment((-100,7)).close().assemble().finalize().extrude(-34).union(w1.workplane(offset=-54/2).moveTo(-17.5,-6.5).box(71,61,54))