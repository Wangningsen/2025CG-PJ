import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,76,0))
r=w0.sketch().arc((-71,27),(-88,-19),(-58,-52)).arc((70,-74),(31,51)).arc((-36,98),(-71,27)).assemble().reset().face(w0.sketch().arc((-62,11),(-55,-37),(-14,-12)).arc((-41,-3),(-62,11)).assemble(),mode='s').push([(33.5,-66.5)]).rect(9,7,mode='s').finalize().extrude(-152)