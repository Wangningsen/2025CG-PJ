import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-86,8),(15,15),(76,-65)).arc((34,57),(-86,8)).assemble().finalize().extrude(200)