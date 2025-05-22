import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().segment((-59,-85),(59,-85)).segment((59,-75)).arc((4,-55),(59,-24)).segment((59,85)).segment((-59,85)).close().assemble().finalize().extrude(-161).union(w0.workplane(offset=39/2).cylinder(39,32))