import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-86,8),(14,15),(76,-65)).arc((36,56),(-86,8)).assemble().finalize().extrude(-200)