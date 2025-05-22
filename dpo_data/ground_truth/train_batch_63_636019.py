import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
r=w0.workplane(offset=-112/2).cylinder(112,4).union(w0.workplane(offset=88/2).cylinder(88,23))