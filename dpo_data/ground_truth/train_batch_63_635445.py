import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().segment((-59,-85),(59,-85)).segment((59,-75)).arc((55,-74),(51,-71)).arc((5,-62),(43,-34)).arc((50,-25),(59,-19)).segment((59,85)).segment((-59,85)).close().assemble().finalize().extrude(-161).union(w0.workplane(offset=39/2).cylinder(39,32))