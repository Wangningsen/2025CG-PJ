import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((-98,13),(-25,-11),(-9,-89)).segment((100,-89)).segment((100,59)).segment((48,59)).segment((48,69)).segment((9,69)).arc((-6,83),(-25,87)).arc((-84,69),(-98,13)).assemble().finalize().extrude(-61).union(w1.workplane(offset=-4/2).moveTo(11,25).box(56,100,4))