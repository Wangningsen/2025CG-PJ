import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((23,67),(26,57)).arc((33,65),(42,71)).segment((27,54)).segment((28,52)).segment((47,72)).arc((91,42),(55,2)).segment((54,-6)).arc((96,55),(23,67)).assemble().finalize().extrude(-69).union(w0.workplane(offset=98/2).moveTo(-64,-46).cylinder(98,36))