import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-76,0))
r=w0.sketch().arc((-71,26),(-89,-17),(-59,-52)).arc((71,-73),(31,51)).arc((-35,99),(-71,26)).assemble().reset().face(w0.sketch().arc((-63,13),(-55,-37),(-15,-5)).arc((-42,-2),(-63,13)).assemble(),mode='s').push([(30.5,-67.5)]).rect(3,9,mode='s').finalize().extrude(153)