import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-93,19),(-90,-42),(-51,-88)).segment((-51,65)).segment((62,65)).arc((-1,88),(-64,64)).segment((-64,-24)).segment((-69,-24)).segment((-69,60)).arc((-80,47),(-88,32)).arc((-72,18),(-93,19)).assemble().finalize().extrude(192).union(w0.workplane(offset=200/2).moveTo(90.5,-29).box(11,50,200))