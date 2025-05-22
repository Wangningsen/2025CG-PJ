import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
w1=cq.Workplane('YZ',origin=(-11,0,0))
r=w0.workplane(offset=-97/2).moveTo(64.5,55).box(33,18,97).union(w0.sketch().segment((-93,17),(-74,45)).segment((-10,12)).segment((-32,-23)).segment((-28,-23)).arc((-22,-65),(20,-83)).segment((35,-99)).segment((100,-57)).segment((50,22)).segment((36,13)).arc((20,17),(4,15)).arc((-43,99),(-93,17)).assemble().finalize().extrude(28)).union(w1.workplane(offset=12/2).moveTo(-17,35).cylinder(12,2))