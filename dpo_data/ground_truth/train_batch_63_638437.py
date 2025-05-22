import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).cylinder(200,20).union(w0.sketch().circle(38).push([(-28,-6)]).circle(9,mode='s').finalize().extrude(-63))