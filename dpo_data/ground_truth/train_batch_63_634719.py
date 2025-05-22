import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.workplane(offset=-123/2).moveTo(-35,-34).cylinder(123,6).union(w0.sketch().arc((-56,100),(-50,82),(-49,64)).segment((36,64)).segment((36,100)).close().assemble().finalize().extrude(-103)).union(w1.sketch().segment((-100,-1),(-36,-1)).segment((-36,-14)).segment((48,-14)).segment((48,17)).segment((32,17)).segment((32,72)).segment((-100,72)).close().assemble().push([(6.5,1.5)]).rect(3,3,mode='s').finalize().extrude(73))