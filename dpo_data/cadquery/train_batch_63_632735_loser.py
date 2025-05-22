import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('XY',origin=(0,0,-30))
r=w0.sketch().segment((-1,-39),(7,-39)).segment((7,-66)).segment((25,-66)).segment((25,-39)).segment((34,-39)).segment((34,1)).segment((25,1)).segment((25,28)).segment((7,28)).segment((7,1)).segment((-1,1)).close().assemble().finalize().extrude(-92).union(w0.sketch().segment((22,-38),(87,-38)).segment((87,52)).segment((81,52)).arc((26,57),(22,3)).close().assemble().finalize().extrude(-46)).union(w1.workplane(offset=-57/2).moveTo(30,85).box(56,30,57))