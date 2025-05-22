import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-86,8),(17,14),(76,-65)).arc((35,57),(-86,8)).assemble().finalize().extrude(-200)