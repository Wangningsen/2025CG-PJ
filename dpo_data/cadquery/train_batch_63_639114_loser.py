import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
r=w0.workplane(offset=-25/2).moveTo(-22,-98).cylinder(25,2).union(w0.sketch().segment((-43,50),(-9,50)).segment((-9,41)).segment((9,41)).segment((9,50)).segment((43,50)).segment((43,91)).segment((9,91)).segment((9,100)).segment((-9,100)).segment((-9,91)).segment((-43,91)).close().assemble().finalize().extrude(65))