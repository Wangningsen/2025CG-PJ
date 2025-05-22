import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.workplane(offset=-73/2).moveTo(92,-96).cylinder(73,4).union(w0.sketch().segment((-17,-5),(-17,70)).segment((8,70)).arc((-93,62),(-17,-5)).assemble().finalize().extrude(74))