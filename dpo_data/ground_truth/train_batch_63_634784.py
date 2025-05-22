import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.workplane(offset=-96/2).moveTo(64.5,55).box(33,18,96).union(w0.sketch().segment((-93,17),(-69,52)).segment((-8,10)).arc((-31,-50),(23,-83)).segment((34,-99)).segment((100,-57)).segment((50,22)).segment((36,14)).arc((18,17),(2,15)).arc((-44,99),(-93,17)).assemble().finalize().extrude(29))