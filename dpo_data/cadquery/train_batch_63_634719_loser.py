import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('YZ',origin=(-17,0,0))
r=w0.workplane(offset=-123/2).moveTo(-36,-34).cylinder(123,6).union(w0.sketch().segment((-56,100),(-49,64)).segment((36,64)).segment((35,100)).close().assemble().finalize().extrude(-103)).union(w1.sketch().segment((-100,-1),(-36,-1)).segment((-36,-14)).segment((48,-14)).segment((48,17)).segment((32,17)).segment((32,72)).segment((-100,72)).close().assemble().push([(6,-1)]).circle(2,mode='s').finalize().extrude(74))