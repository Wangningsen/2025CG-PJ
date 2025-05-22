import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-82))
w1=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().push([(-35,-34)]).circle(65).push([(-22,-89.5)]).rect(14,9,mode='s').finalize().extrude(150).union(w1.sketch().arc((-35,12),(-25,-85),(60,-37)).arc((63,84),(-35,12)).assemble().finalize().extrude(-66))