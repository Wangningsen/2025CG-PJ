import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('YZ',origin=(1,0,0))
r=w0.sketch().segment((-1,-39),(7,-39)).segment((7,-66)).segment((25,-66)).segment((25,-39)).segment((34,-39)).segment((34,1)).segment((25,1)).segment((25,28)).segment((7,28)).segment((7,1)).segment((-1,1)).close().assemble().finalize().extrude(-92).union(w0.sketch().segment((34,-38),(87,-38)).segment((87,52)).segment((78,52)).arc((22,52),(34,-2)).close().assemble().finalize().extrude(-46)).union(w1.workplane(offset=57/2).moveTo(85,-58.5).box(30,57,57))