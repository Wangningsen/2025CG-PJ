import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().segment((20,78),(42,68)).segment((46,76)).segment((27,85)).segment((27,78)).close().assemble().finalize().extrude(-16).union(w0.workplane(offset=68/2).moveTo(8,89).cylinder(68,11)).union(w1.sketch().segment((-100,-87),(15,-87)).segment((15,-65)).arc((65,-10),(8,38)).segment((8,87)).segment((-77,87)).segment((-77,-16)).segment((-38,-16)).arc((-32,-39),(-16,-56)).segment((-100,-56)).close().assemble().finalize().extrude(-58))