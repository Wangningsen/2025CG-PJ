import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.sketch().push([(-57.5,-48.5)]).rect(19,103).reset().face(w0.sketch().arc((-11,59),(-25,18),(15,25)).arc((58,86),(-11,59)).assemble()).reset().face(w0.sketch().arc((-11,49),(-19,29),(0,29)).arc((-6,39),(-11,49)).assemble(),mode='s').finalize().extrude(-82)