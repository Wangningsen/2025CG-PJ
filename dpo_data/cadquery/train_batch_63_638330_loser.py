import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-76,0))
r=w0.sketch().arc((-71,27),(-89,-10),(-70,-46)).arc((69,-75),(32,50)).arc((-36,98),(-71,27)).assemble().reset().face(w0.sketch().arc((-68,12),(-56,-36),(-14,-10)).arc((-42,-2),(-63,16)).arc((-65,14),(-68,12)).assemble(),mode='s').push([(34,-66)]).circle(5,mode='s').finalize().extrude(152)