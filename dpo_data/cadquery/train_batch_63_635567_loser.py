import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.workplane(offset=-109/2).moveTo(3,43).cylinder(109,19).union(w0.sketch().segment((-22,-54),(-14,-62)).segment((4,-46)).segment((-3,-38)).arc((-9,-45),(-17,-51)).segment((-17,-52)).segment((-19,-52)).arc((-20,-53),(-22,-54)).assemble().finalize().extrude(91))