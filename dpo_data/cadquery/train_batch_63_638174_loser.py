import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
w1=cq.Workplane('YZ',origin=(42,0,0))
r=w0.sketch().push([(-68,-62)]).circle(32).circle(14,mode='s').finalize().extrude(-115).union(w0.workplane(offset=-101/2).moveTo(41,-34).box(118,6,101)).union(w0.sketch().segment((20,53),(32,39)).segment((32,10)).segment((74,10)).segment((74,40)).segment((86,52)).segment((74,65)).segment((74,94)).segment((32,94)).segment((32,64)).close().assemble().finalize().extrude(24)).union(w1.workplane(offset=7/2).moveTo(62.5,52).box(43,12,7))