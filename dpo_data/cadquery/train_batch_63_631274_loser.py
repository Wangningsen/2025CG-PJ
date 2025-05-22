import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().arc((23,59),(36,60),(36,50)).arc((40,48),(43,46)).segment((43,48)).segment((46,48)).segment((46,43)).arc((92,38),(55,2)).arc((97,54),(29,72)).segment((29,71)).segment((28,71)).arc((24,65),(23,59)).assemble().finalize().extrude(-69).union(w0.workplane(offset=99/2).moveTo(-64,-46).cylinder(99,36))