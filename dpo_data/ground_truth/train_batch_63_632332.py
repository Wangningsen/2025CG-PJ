import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-95))
r=w0.workplane(offset=-5/2).moveTo(-31,-49).cylinder(5,42).union(w0.sketch().segment((-47,-42),(73,-42)).segment((73,91)).segment((47,91)).segment((39,79)).segment((34,82)).arc((14,79),(-3,91)).segment((-47,91)).close().assemble().finalize().extrude(195))