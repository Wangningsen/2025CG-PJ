import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().arc((-80,-80),(5,-59),(93,-57)).arc((-13,79),(-80,-80)).assemble().finalize().extrude(79)