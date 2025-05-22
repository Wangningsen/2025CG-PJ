import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().segment((-4,-17),(5,-34)).segment((23,-24)).segment((14,-8)).arc((6,-16),(-4,-17)).assemble().finalize().extrude(57).union(w1.sketch().arc((-80,-80),(2,-59),(93,-57)).arc((-16,79),(-80,-80)).assemble().finalize().extrude(-79))