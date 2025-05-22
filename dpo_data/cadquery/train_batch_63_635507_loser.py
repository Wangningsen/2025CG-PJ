import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((-50,-92),(-38,-74)).segment((-18,-87)).segment((-25,-97)).arc((36,-55),(3,11)).segment((28,34)).segment((22,81)).segment((18,80)).segment((18,89)).segment((-12,86)).segment((-10,62)).segment((-4,26)).arc((-75,-20),(-50,-92)).assemble().finalize().extrude(-107).union(w0.sketch().segment((61,-22),(79,-22)).segment((79,11)).arc((70,10),(61,11)).close().assemble().finalize().extrude(32)).union(w1.workplane(offset=77/2).moveTo(49,79).cylinder(77,21))