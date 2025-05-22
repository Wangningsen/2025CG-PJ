import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
w1=cq.Workplane('XY',origin=(0,0,-60))
r=w0.sketch().segment((-45,81),(-38,81)).segment((-38,72)).segment((-39,72)).arc((-18,95),(-45,81)).assemble().finalize().extrude(-92).union(w1.sketch().segment((-36,-74),(-36,-71)).arc((-25,-72),(-13,-71)).segment((-13,-74)).arc((52,0),(-13,74)).segment((-13,71)).arc((-25,72),(-36,71)).segment((-36,74)).arc((-100,0),(-36,-74)).assemble().finalize().extrude(119))