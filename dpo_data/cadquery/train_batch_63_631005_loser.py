import cadquery as cq
w0=cq.Workplane('YZ',origin=(-7,0,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.workplane(offset=101/2).moveTo(43,83).cylinder(101,17).union(w1.sketch().segment((-64,-46),(-64,-9)).arc((-99,-47),(-62,-69)).segment((-62,-81)).segment((22,-81)).segment((22,-94)).segment((61,-94)).segment((61,-46)).segment((-62,-46)).segment((-62,-47)).segment((-64,-47)).close().assemble().finalize().extrude(-97))