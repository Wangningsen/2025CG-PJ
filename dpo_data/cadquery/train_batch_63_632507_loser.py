import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().segment((61,-17),(97,-17)).segment((97,17)).segment((62,17)).arc((62,0),(61,-17)).assemble().finalize().extrude(74).union(w1.sketch().arc((-80,-80),(-10,-61),(89,-59)).arc((-11,79),(-80,-80)).assemble().finalize().extrude(-79))