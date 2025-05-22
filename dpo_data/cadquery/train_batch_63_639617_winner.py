import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.sketch().segment((5,-16),(14,-28)).segment((31,-16)).close().assemble().finalize().extrude(-68).union(w0.workplane(offset=-51/2).moveTo(81.5,-26).box(37,22,51)).union(w0.sketch().arc((-100,37),(-85,26),(-71,37)).close().assemble().finalize().extrude(9))