import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((-100,-31),(-72,-31)).arc((-50,-41),(-29,-31)).segment((-5,-31)).segment((-5,-14)).segment((79,-44)).segment((100,29)).segment((10,53)).segment((-5,-2)).segment((-5,7)).segment((-29,7)).arc((-50,17),(-72,7)).segment((-100,7)).close().assemble().finalize().extrude(-34).union(w1.workplane(offset=-54/2).moveTo(-17.5,-6.5).box(71,61,54))