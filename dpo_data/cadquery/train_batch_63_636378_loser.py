import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
r=w0.workplane(offset=-114/2).moveTo(-21.5,84).box(115,32,114).union(w0.workplane(offset=-97/2).moveTo(66,-10).cylinder(97,13)).union(w0.sketch().push([(-51.5,-44.5)]).rect(31,111).push([(-39,-38)]).circle(2,mode='s').finalize().extrude(22))