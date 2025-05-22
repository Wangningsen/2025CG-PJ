import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().segment((-93,-40),(-80,-64)).segment((-45,-44)).segment((-41,-44)).segment((-41,-42)).segment((10,-13)).segment((4,-2)).segment((4,100)).segment((-91,100)).segment((-91,-14)).segment((-44,-14)).close().assemble().finalize().extrude(50).union(w0.workplane(offset=110/2).moveTo(62,-61.5).box(62,77,110))