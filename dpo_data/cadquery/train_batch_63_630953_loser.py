import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.workplane(offset=-73/2).moveTo(-46,35.5).box(92,47,73).union(w0.sketch().segment((17,100),(50,66)).arc((39,93),(17,100)).assemble().finalize().extrude(-43)).union(w0.sketch().push([(-46.5,35.5)]).rect(15,11).push([(47.5,-57)]).rect(89,86).finalize().extrude(55)).union(w1.sketch().segment((-45,-7),(-45,-6)).arc((-49,-75),(-22,-11)).segment((-22,-14)).segment((-23,-14)).segment((-23,-10)).segment((-23,-8)).arc((-33,-5),(-43,-4)).segment((-43,-7)).close().assemble().finalize().extrude(-37))