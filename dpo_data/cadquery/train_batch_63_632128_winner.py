import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().arc((41,-82),(88,-88),(63,-46)).arc((-23,-17),(41,-82)).assemble().finalize().extrude(-73).union(w0.sketch().push([(-8,15)]).circle(85).circle(12,mode='s').finalize().extrude(49)).union(w1.workplane(offset=-67/2).moveTo(17,24).box(60,104,67))