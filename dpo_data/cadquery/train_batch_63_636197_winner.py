import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,74))
r=w0.sketch().segment((-74,-21),(-32,-21)).segment((-32,-78)).segment((32,-78)).segment((32,-21)).segment((74,-21)).segment((74,21)).segment((32,21)).segment((32,78)).segment((-32,78)).segment((-32,21)).segment((-74,21)).close().assemble().finalize().extrude(-174).union(w0.workplane(offset=26/2).cylinder(26,49))