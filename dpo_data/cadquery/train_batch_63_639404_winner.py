import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.sketch().push([(-57.5,-48.5)]).rect(19,103).reset().face(w0.sketch().arc((-11,60),(-29,22),(12,25)).arc((59,85),(-11,60)).assemble()).reset().face(w0.sketch().arc((-9,47),(-19,29),(2,31)).arc((-4,39),(-9,47)).assemble(),mode='s').finalize().extrude(-82)