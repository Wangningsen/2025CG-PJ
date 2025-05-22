import cadquery as cq
w0=cq.Workplane('YZ',origin=(-51,0,0))
w1=cq.Workplane('ZX',origin=(0,9,0))
r=w0.workplane(offset=-41/2).moveTo(16,96).box(142,8,41).union(w0.workplane(offset=-2/2).moveTo(-87,39).cylinder(2,8)).union(w0.sketch().arc((-58,-6),(75,-59),(-49,12)).segment((-45,12)).segment((-45,-6)).close().assemble().finalize().extrude(142)).union(w1.workplane(offset=86/2).moveTo(-27.5,-56.5).box(13,35,86))