import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.workplane(offset=-111/2).moveTo(11,77).box(60,14,111).union(w0.workplane(offset=-87/2).moveTo(37.5,82).box(111,12,87)).union(w0.sketch().segment((-92,-23),(-46,-88)).segment((20,-41)).segment((-26,26)).close().assemble().push([(-36.5,-31)]).rect(61,28,mode='s').finalize().extrude(89))