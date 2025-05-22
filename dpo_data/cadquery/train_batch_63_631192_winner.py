import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
w1=cq.Workplane('YZ',origin=(-45,0,0))
r=w0.workplane(offset=-58/2).moveTo(-89,-43).cylinder(58,11).union(w1.workplane(offset=99/2).moveTo(-7,48.5).box(30,103,99))